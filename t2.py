import sys
import requests
import importlib
l = [[1,[2]],[3,4]]

for p,m in l:
	print(p, m)

sys.path.insert(0,r"E:\重要\插件\wx\requests")
print(sys.modules['requests'])
importlib.reload(requests)
print(sys.modules['requests'])
print(requests.__version__)
print(__file__)