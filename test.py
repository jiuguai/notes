import requests
import json
def get_code(file_path):
    
    with open(file_path,"rb") as f:
        image = f.read()
        api_url = "http://127.0.0.1:7788/"
        resp = requests.post(url=api_url, data=image)
        code = json.loads(resp.text)['code']
        return code


code = get_code(r'C:\Users\zero\Desktop\vcode.png')
print(code)