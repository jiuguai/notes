import re
import os
import json
import asyncio
import aiohttp

import redis
import requests
REDIS_MALL_ORDER_DIC = {
    "host":'127.0.0.1',
    "port":6379,
    "db":0,
    "decode_responses":True  #设置为True返回的数据格式就是时str类型
}







def download_m3u8(url):
    rc = redis.Redis(**REDIS_MALL_ORDER_DIC)
    if "m3u8:t" in rc.keys():
        rc.delete('m3u8:t')





    rep = requests.get(url)
    txt = rep.text

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

        file_dir = r"E:\test"
        with open(os.path.join(file_dir,d['order']),'wb') as f:
            f.write(rep.content)


if __name__ == "__main__":

    url = "https://pl-ali.youku.com/playlist/m3u8?vid=XNDIxOTM2NzUzNg&type=flv&ups_client_netip=71f67d9a&utid=zCHQFjs6DVsCAd7wcizXMEpY&ccode=0502&psid=b7ec7a42c76734775fc792eb7e8f8f94&app_ver=2.1.4&duration=975&expire=18000&drm_type=1&drm_device=7&play_ability=5376&dyt=1&btf=&ups_ts=1590495919&onOff=0&encr=0&ups_key=afbd1d8646765017e9294465a16213f7"

    download_m3u8(url)