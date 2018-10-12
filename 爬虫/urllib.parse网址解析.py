#coding:utf-8
from urllib import request , parse
url = 'http://www.baidu.com/s;hellow?wd=Python&username=abc#1'
result = parse.urlparse(url)
print(result)
print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)
print('params:',result.params)
print('query:',result.query)
print('fragment:',result.fragment)
print('--------------------')

result = parse.urlsplit(url)
print('scheme:',result.scheme)
print('netloc:',result.netloc)
print('path:',result.path)

print('query:',result.query)
print('fragment:',result.fragment)