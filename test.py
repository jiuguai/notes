import hashlib

s = "5fdb03c61e13ddc3e7cb9bc57c9e5c4e"


md5 = hashlib.md5()
md5.update(b'ttes')
s = md5.hexdigest()
print(s)