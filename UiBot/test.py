import re


com = re.compile('(?<=-)(?i:z (\w+))(?i:(?=Tj{1,2}))', re.X)

s = "-ZeroTJ"

z = com.search(s)

if z:
	print(z.group())
	print(z.groups())