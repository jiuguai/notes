import re

s = "asdf123a4213asdf124asdf"
comp = re.compile( r'(?P<zero>f\d??)')

print(comp.search(s))




# ser = comp.search(s)
# print(ser.groupdict())
# print(ser)
# re.I

# for serc in comp.finditer(s):
# 	print(serc.groupdict())

# print("/asdf123a/cmder/安装.md".rsplit("/",maxsplit=1))

