

### requests
```python
import requests
requests.reuqest(methond,url,**kwargs) 
reqeusts.get(url,params=None,**kwargs) # 常用
requests.header(url,**kwargs)
requests.post(url,data=None,json=None,**kwargs)
requests.put(url,data=None,**kwargs)
requests.patch(url,data=None,**kwargs)
requests.delete(url,**kwargs)

# **kwargs
params
data
json
files

header
proxies

auth
cookies #写于headers当中即可
timeout

allow_redirects : 是否重定向  default:True
stream:获取内容立即下载 default:True
verify: 认证SSL证书开关 default:True
cert: 本地SSL证书路径
```
