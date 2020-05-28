import os
import re

result = os.popen('rfsnu -l').read()
print(result)
print(type(result))


# com = re.compile('(?<=[\[-])\d{1,3}(?:\.\d{1,3}){3}')
com = re.compile('(?<=\[)\d{1,3}(?:\.\d{1,3}){3}')

r = com.findall(result)
print(r)
