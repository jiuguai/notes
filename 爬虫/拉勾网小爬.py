#coding:utf-8
from urllib import request , parse
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'X-Anit-Forge-Code': 0,
    'X-Anit-Forge-Token':'None',
    'X-Requested-With': 'XMLHttpRequest'
}
data = {
    'fist':'true',
    'pn':1,
    'kd':'python'
}
datau = parse.urlencode(data).encode('utf-8')
req = request.Request(url,headers=headers,method='POST',data = datau)
resp = request.urlopen(req)
t = resp.read().decode()
print(t)

