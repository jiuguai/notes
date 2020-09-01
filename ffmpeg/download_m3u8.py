import re
import os
import json


import redis
import requests
REDIS_MALL_ORDER_DIC = {
    "host":'47.105.186.249',
    "port":6379,
    "db":0,
    "decode_responses":True,  #设置为True返回的数据格式就是时str类型
    "password":"r-jiuguai"
}


def download_m3u8(url,file_dir):
    rc = redis.Redis(**REDIS_MALL_ORDER_DIC)

    if "m3u8:t" in rc.keys():
        rc.delete('m3u8:t')


    rep = requests.get(url)
    print(rep.status_code)
    txt = rep.text
    # print(txt)
    i = 1

    for path in re.finditer("(?P<path>[^\r\n]+?\.ts[^\r\n]*?)(?=\r?\n)",txt,re.S):
        d = {
            "url":  path.groupdict()['path'],
            "order":("%s.ts" %(i)).zfill(8) 
        }

    #     print(d)
        rc.lpush("m3u8:t",json.dumps(d))

        i += 1


    for i in range(rc.llen("m3u8:t")):
        d = json.loads(rc.brpop('m3u8:t',3)[1])
        print(d['url'])
        
        rep = requests.get(d['url'])
        
        print(rep.status_code)

        
        with open(os.path.join(file_dir,d['order']),'wb') as f:
            f.write(rep.content)


if __name__ == "__main__":

    url = "https://pl-ali.youku.com/playlist/m3u8?vid=XMzQzMjA3NjkwNA&type=hd2&ups_client_netip=def76cbe&utid=BGylF6%2BN83kCAa8KEMc8jpjk&ccode=0502&psid=dea4a717708e86bd878dc444f5b0860941ae9&ups_userid=69926557&ups_ytid=610813753&app_ver=2.1.17&duration=269&expire=18000&drm_type=1&drm_device=7&play_ability=5376&dyt=1&btf=&rid=2000000030AA2C2DF746F401A557499324D59E6C02000000&ups_ts=1598361759&onOff=0&encr=0&ups_key=eab6deb33de183905beeee7047f1baea"
    file_dir = r"E:\video\V"
    download_m3u8(url,file_dir)