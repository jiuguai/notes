#encoding:utf-8
from urllib import request

url = 'http://httpbin.org/ip'
# resp = request.urlopen(url)
# print(resp.read())

handler = request.ProxyHandler({'http':'119.28.194.66:8888'})
opener = request.build_opener(handler)
req = request.Request(url)
resp = opener.open(req)
print(resp.read())

