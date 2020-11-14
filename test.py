
import json
from urllib.parse import urljoin
import requests


PATH_MAP = {
    "get_token":"gettoken",
    "upload":"/media/upload",
    "send_file":"/topapi/message/corpconversation/asyncsend_v2",
    "get_send_process":"/topapi/message/corpconversation/getsendprogress",
    "get_send_result":"/topapi/message/corpconversation/getsendresult",
    "getbymobile":"/topapi/v2/user/getbymobile"
}


class dd_api():
    def __init__(self, app_key, app_secret, agent_id):
        self.url = "https://oapi.dingtalk.com/"
        self.app_key = app_key
        self.app_secret = app_secret
        self.agent_id = agent_id
        self.get_token()

    def get_token(self):

        url = urljoin(self.url,PATH_MAP['get_token'])
        params = {
            "appkey":self.app_key,
            "appsecret":self.app_secret
        }
        rep = requests.get(url,params=params)
        info = rep.json()
        print(info)
        self.token = info.get('access_token', None)
        return info

    def upload(self,file_path,name,mimetype):
        
        url = urljoin(self.url,PATH_MAP['upload'])
        
        url = url + '?access_token=%s&type=file' % self.token
        print(url)
        files = {'media': (name  ,  open(file_path, 'rb'), mimetype)}

        rep = requests.post(url, files=files)
        js = rep.json()
        return js

    def send_file(self, mediaid, userid_list):
        url = urljoin(self.url,PATH_MAP['send_file'])
        url= url + "?access_token=%s" %self.token

        data={
            "agent_id":self.agent_id,
            "msg":{
                "msgtype":"file",
                "file":{
                    "media_id":mediaid
                }
            },
            "userid_list":','.join(userid_list)
        }

        rep=requests.post(url,data=json.dumps(data))
        return rep.json()

    def get_send_process(self,task_id):

        url = urljoin(self.url,PATH_MAP['get_send_process'])
        url= url + "?access_token=%s" %self.token
        data = {
            "agent_id":self.agent_id,
            "task_id":task_id
        }
        rep = requests.post(url,data)
        return rep.json()
    def get_send_result(self,task_id):
        url = urljoin(self.url,PATH_MAP['get_send_result'])
        url= url + "?access_token=%s" %self.token
        data = {
            "agent_id":self.agent_id,
            "task_id":task_id
        }
        rep = requests.post(url,data)
        return rep.json()
    def getbymobile(self,mobile):
        url = urljoin(self.url,PATH_MAP['getbymobile'])
        url= url + "?access_token=%s" %self.token
        params = {
            "mobile":mobile
        }
        rep = requests.get(url,params=params)
        return rep.json()

appkey = "dingpv9finvxgtimp7iv"
appsecret = "rZHvahoTtGJ2QB2DimD6Y291e6YmlxSEC2lvxVnEJw4oG5J7Mfzyn3SVRifeEENX"
agent_id = 968351362
api = dd_api(appkey,appsecret,agent_id)
# print(api.token)
# file_path = r'C:\Users\Administrator\Desktop\三湘财务\智慧财务.md'  # 文件地址
# js = api.upload(file_path,"智慧1.md","application/mp4")
# print(js)
# mediaid = js['media_id']
# print(mediaid)
# userid_list = ["manager9034"]
# js = api.send_file(mediaid,userid_list)
# task_id = js['task_id']

# print(js)

# print('----- 发送进度-----')
# print(api.get_send_process(task_id))
# print('-----发送结果-------')
# print(api.get_send_result(task_id))

print(api.getbymobile('18774979616'))
print(api.getbymobile('18797780947'))