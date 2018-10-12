#coding:utf-8
from urllib import request , parse
# resp = request.urlopen('http://www.2xkt.com/python/py_constructor.html')
# t = resp.read()

# 下载网络数据
# request.urlretrieve('http://img.zcool.cn/community/013e6858146b58a84a0d304f951f9b.jpg@1280w_1l_2o_100sh.jpg','index.jpg')

# urlencode
# 例1
# params = {'name': '张三' ,'age':17,'great':'hello world'}
# result = parse.urlencode(params)
# print(result)
#例2
# url = 'http://www.baidu.com/s?'
# params = {'wd':'刘德华'}
# qs = parse.urlencode(params)
# url = url + qs
# resp = request.urlopen(url)
# print(resp.read())

#parse_qs
params = {'name': ['张三'] ,'age':17,'great':'hello world'}

result = parse.urlencode(params)

print(type(result))
print(result)
result = parse.parse_qs(result)

print(type(result))
print(result)

print(parse.quote_from_bytes('age 我'.encode()))





