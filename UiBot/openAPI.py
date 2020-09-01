"""commander open api方法封装
可用open api方法列表：
    set_parameter_by_open_api: 设置参数
    get_parameter_by_open_api: 获取参数
    push_queue_by_open_api: 往队列中压入数据
    pull_queue_by_open_api: 从队列中取出数据
    create_task_by_open_api: 创建任务
    get_task_status_by_open_api: 获取任务状态
"""
# coding = utf-8
import os
import json
import time
import random
import string
import logging
import hashlib
import requests
from typing import Dict, Tuple, List


try:
    import UiBot
except ImportError as e:

    class UiBotSimulator(object):
        """UiBot模拟器，方便单独运行Python脚本"""

        def GetString(self, strPath):
            return "unload exception config"

        def GetCommanderInfo(self):
            info = {"url": "http://192.168.0.25:4100", "token": "None", "task_id": 0}
            return json.dumps(info)

    UiBot = UiBotSimulator()


# 开启调试模式，每个请求都打印日志
ECHO_RESULT = os.environ.get("ECHO_RESULT")

# open api认证信息
AUTH_INFO = {
    "static_str": "afd8426953b54e23b925a63dff4bf7ed",
    "app_key": "",
    "app_secret": "",
    "web_api_prefix": "/api/commander",
    "open_api_prefix": "/api/open",
    "commander_url": "http://192.168.0.25:4100",
    "loginName": "",
    "password": "",
    "verify_code": None,
}


# open api请求句柄
client = requests.sessions.Session()
# 日志句柄
logger = logging.getLogger("openAPI")


def get_auth_info() -> dict:
    """获取认证信息"""
    return AUTH_INFO


def set_auth_info(auth_info: dict) -> None:
    """设置open api认证信息"""
    AUTH_INFO.update(auth_info)


def get_random_string(length: int = 32) -> str:
    """获取随机字符串"""
    return "".join(random.choices(string.ascii_letters + string.digits, k=length))


def get_timestamp(length: int = 10) -> str:
    """获取系统时间时间戳"""
    assert length in (10, 13), "时间戳长度参数错误，只有10位与13位时间戳"
    current_timestamp = time.time()
    return str(current_timestamp * 1000)[:length]


def get_absolute_url_open_api(url):
    return f"{AUTH_INFO['commander_url']}{AUTH_INFO['open_api_prefix']}{url}"


def check_response(response: requests.Response, operate=r"请求") -> bool:
    """检查response是否成功"""
    operate = operate.split("\n")[0]
    if isinstance(response, requests.Response):
        if response.status_code == 200 and response.json().get("code") == 0:
            status = True
        elif response.status_code == 200 and response.json().get("success"):
            status = True
        else:
            logger.error(f"{operate}失败，错误详情：{response.text}")
            status = False
    else:
        status = False
        logger.error(f"参数response类型不符，预期requests.Response对象，实际为{type(response)}")
    # 根据请求结果与调试标志输出
    if not status or ECHO_RESULT:
        format_output(response)
    return status


def format_output(obj):
    if isinstance(obj, (dict, list, tuple)):
        logger.debug(json.dumps(obj, ensure_ascii=False, indent=4))
    elif isinstance(obj, requests.Response):
        logger.debug(f"{obj.status_code}, {obj.reason}, {obj.url}")
        if obj.headers.get("Content-Type") and "application/json" in obj.headers.get(
            "Content-Type"
        ):
            logger.debug(json.dumps(obj.json(), ensure_ascii=False, indent=4))
        else:
            logger.debug(obj.text)
    else:
        logger.debug(obj)


def get_open_api_sign() -> Dict[str, str]:
    """获取签名字符串"""
    timestamp = get_timestamp(length=10)
    random_string = get_random_string(length=32)
    sign_raw = (
        AUTH_INFO["static_str"] + AUTH_INFO["app_secret"] + random_string + timestamp
    )
    sign_bytes = sign_raw.encode("utf-8")
    sign = hashlib.sha1(sign_bytes).hexdigest()
    params = {
        "appKey": AUTH_INFO["app_key"],
        "nonce": random_string,
        "timestamp": timestamp,
        "sign": sign,
    }
    return params


def request_open_api(
    url: str, operate, payload: dict = None, method="post"
) -> Tuple[requests.Response, bool]:
    """请求OpenAPI接口"""
    params = get_open_api_sign()
    if method.lower() == "get":
        res = client.get(url=get_absolute_url_open_api(url), params=params)
    else:
        res = client.post(
            url=get_absolute_url_open_api(url), params=params, json=payload
        )
    status = check_response(res, operate=operate)
    return res, status


def set_parameter_by_open_api(
    param_name: str, value: str or int or bool
):
    """通过openAPI设置参数"""
    url = "/parameter/set"
    payload = {"paramName": param_name, "value": value}
    _, status = request_open_api(
        url=url, payload=payload, operate=set_parameter_by_open_api.__doc__
    )
    return status


def get_parameter_by_open_api(param_name: str):
    """通过openAPI获取参数"""
    url = "/parameter/get"
    payload = {"paramName": param_name}
    res, status = request_open_api(
        url=url, payload=payload, operate=get_parameter_by_open_api.__doc__
    )
    if status:
        return res.json()["data"]["value"]
    else:
        return None


def push_queue_by_open_api(
    queue_name: str, content: str, delay: int, expired: int
):
    """通过openAPI入队"""
    url = "/queue/push"
    payload = {
        "queueName": queue_name,
        "content": content,
        "delay": delay,
        "expired": expired,
    }
    _, status = request_open_api(
        url=url, payload=payload, operate=push_queue_by_open_api.__doc__
    )
    return status


def pull_queue_by_open_api(queue_name: str):
    """通过openAPI出队"""
    url = "/queue/pull"
    payload = {"queueName": queue_name}
    res, _ = request_open_api(
        url=url, payload=payload, operate=pull_queue_by_open_api.__doc__
    )
    return res.json()["data"]["content"]


def create_task_by_open_api(
    flow_code, args={}, worker_name=None, callback_url=None, is_now=None
):
    """通过openAPI创建任务"""
    url = "/task/create"
    payload = {
        "flowCode": flow_code,
        "args": args,
        "callbackUrl": callback_url,
        "workerName": worker_name,
        "isNow": is_now,
    }
    # for key, value in list(payload.items()):
    #     if value is None:
    #         del payload[key]
    res, status = request_open_api(
        url=url, payload=payload, operate=create_task_by_open_api.__doc__
    )
    if status:
        return res.json()["data"]
    else:
        return False


def get_task_status_by_open_api(task_id: str):
    """通过openAPI获取任务状态"""
    url = f"/task/status/{task_id}"
    res, status = request_open_api(
        url=url, method="get", operate=get_task_status_by_open_api.__doc__
    )
    if status:
        return res.json()["data"]
    else:
        return False


if __name__ == "__main__":
    print(get_task_status_by_open_api.__doc__)


    print(get_random_string())