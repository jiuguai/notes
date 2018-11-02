
+ haslib


+ gzip
    + 網絡傳輸中經常用到

```python
import gzip

x = gzip.compress('我是'.encode())
print(x)
x = gzip.decompress(x).decode()
print(x)

```

+ 編碼判斷
    + cchardet
        + 更快 
    + chardet
    
```python
import chardet
path = r'F:\crawler\qsbk\qsbk\pipelines.py'
with open(path,'rb') as f:
    result = chardet.detect(f.read())
    print(result)

import cchardet
path = r'F:\crawler\qsbk\qsbk\pipelines.py'
with open(path,'rb') as f:
    result = cchardet.detect(f.read())
    print(result)

print(chardet.detect('哈哈哈哈'.encode('UTF-8')))
print(cchardet.detect('哈哈哈哈'.encode('UTF-8')))
print(chardet.detect('哈哈哈哈'.encode('gb2312')))
print(cchardet.detect('哈哈哈哈'.encode('gb2312')))
# result
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
# {'encoding': 'ASCII', 'confidence': 1.0}
# {'encoding': 'utf-8', 'confidence': 0.938125, 'language': ''}
# {'encoding': 'UTF-8', 'confidence': 0.9381250143051147}
# {'encoding': 'EUC-JP', 'confidence': 0.99, 'language': 'Japanese'}
# {'encoding': 'WINDOWS-1252', 'confidence': 0.5}
```



+ **base64**
    1. 用途
        1. 验证码识别的服务接口 需要 base64编码提交
        2. code 为阿里云接口验证码识别
```python
import requests
from base64 import b64encode
img_path = r'C:\Users\zero\Desktop\validate.png'
with open(img_path,'rb') as f:
    img_b64 = b64encode(f.read())

url = 'https://302307.market.alicloudapi.com/ocr/captcha'
appcode = '24af2d3fcbd344479567721917741893'
headers = {
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
    'Authorization': 'APPCODE ' + appcode
}
formdata = {
    'image':img_b64.decode(),
    'type':1001
}
rep = requests.post(url,headers=headers,data=formdata)
print(rep.json())
```

