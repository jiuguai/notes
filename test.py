import hmac
import hashlib

s = 'wezero'
h = hmac.new(key=b'come',msg=b'first',digestmod='md5')
h.update(s.encode())
print(h.digest())
print(h.hexdigest())


print(bytes((x ^ 0x36) for x in range(256)))