#coding:utf-8
from urllib import request
import json
import re
url = 'http://www.2xkt.com/python/py_constructor.html'
reg = '<div.+?class="views-row views-row-(?:[9][1-9]|1\d\d) views-row-.+?".*?>.+?<div.+?<span.+?<a href="(.+?)".*?>(.+?)<.+?a>.+?span>.+?div>.+?div>'
resp = request.urlopen(url)
t = resp.read().decode()
x = re.findall(reg,t,re.I|re.S)
try:
    with open('享学data.json','w',encoding='utf-8') as f:
        json.dump(x,f)
finally:
    f.close()