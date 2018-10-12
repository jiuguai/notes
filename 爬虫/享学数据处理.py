import json

try:
    with open('享学data.json','r',encoding='utf-8') as f:
       x= json.load(f)
finally:
    f.close()
print(len(x),x,sep='\n')

#加工处理
for i in x:
    i[0] = 'http://www.2xkt.com' + i[0]

try:
    with open('享学data.json','w',encoding='utf-8') as f:
        json.dump(x,f)
finally:
    f.close()