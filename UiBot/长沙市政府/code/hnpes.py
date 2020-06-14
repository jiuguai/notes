import requests
from requests.packages.urllib3.util import Retry
import numpy as np
import pandas as pd


def save_hnpes(save_path,cookie):
    url = "http://222.240.173.92:7001/hnpes/comm/queryAreaTreeOpr.action"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": "5",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": cookie,
        "Host": "222.240.173.92:7001",
        "Origin": "http://222.240.173.92:7001",
        "Pragma": "no-cache",
        "Referer": "http://222.240.173.92:7001/hnpes/unemployment/unemployment!addUnemploymentUI.action",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4168.3 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
    }



    rep = requests.post(url,headers=headers,data={"pid":0})

    provinces = rep.json()

    provinces = [{'level':1,'name':prov['name'], 'is_parent':prov['isParent'],'id':prov['id'],'pid':prov['pid']} for prov in provinces['data']]



    url = "http://222.240.173.92:7001/hnpes/comm/queryAreaChildTreeOpr.action"


    def get_addrs(addrs,level):
        return [{'level':level,'name':addr['name'], 'is_parent':addr['isParent'],'id':addr['id'],'pid':addr['pid']} for addr in addrs]


    data = []
    addr_stack = []
    # addr_stack.append(chagnsha)
    addr_stack.extend(provinces[::-1])
    while True:
        try:
            addr = addr_stack.pop()
        except:
            print('download over')
            break
        
        data.append(addr)
        if addr['is_parent'] == False:
            continue
        
        print("--->",addr)

        i = 0
        try:
            rep = requests.post(url,headers=headers,data={'pid':addr['id']})
        except:
            i += 1
            if i == 3:
                raise '网络异常'

        addrs = get_addrs(rep.json()['data'], addr['level']+1)
        addr_stack.extend(addrs[::-1])


    df = pd.DataFrame(data)
    df.to_excel(save_path,index=False)
    print('save over')

if __name__ == "__main__":
    cookie = "loginUser=cs0412; UserToken=307C637330343132; UserIndentity=kTL8DUgNbz5Tru0fLSb9FEBcfBcex2w3fgWpawPjVnNeapJ3cE4yVw=="

    save_path = r"C:\Users\zero\Desktop\address.xlsx"

    save_hnpes(save_path, cookie)