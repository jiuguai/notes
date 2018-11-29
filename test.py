code = '''
import os 
print(os.path.abspath('.'))
'''
code = '''
print(123)
a = 20
print(a)
'''
a = 10
exec(code,{'print':print},)
print(a)