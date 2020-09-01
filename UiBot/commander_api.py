import time
import datetime
import random
import json
from pprint import pprint
from hashlib import sha1

import requests

EXPIRED = 2 * 60 * 1000
BASE_STR = ''.join([chr(i) for i in range(48,123)])

def aq_sign(func):
	def inner(self, *args, **kargs):

		self.acquire_sign()
		try:
			return func(self , *args, **kargs)
		except Exception as e:
			return "%s" %e

	return inner

class CommanderAPI():
	def __init__(self, url, static_str, app_key, app_secret):
		self.static_str = static_str
		self.app_key = app_key
		self.app_secret = app_secret
		self.url = url
		self.headers = {"Content-Type":"application/json"}

	def acquire_sign(self):
		self.unix_time = str(int(time.time()))
		self.nonce = self.gen_rand_str()
		self.token = self.static_str + self.app_secret + self.nonce + self.unix_time

		self.sign = sha1(self.token.encode()).hexdigest()
		self.params = {
			"appKey":self.app_key,
			"nonce":self.nonce,
			"timestamp":self.unix_time,
			"sign":self.sign
		}

	def gen_rand_str(self, length=32):

		
		return ''.join(random.sample(BASE_STR,32))

	@aq_sign
	def add_task(self, flow_code,  worker_name, args={}, env=None, is_now=1, call_back_url=None):
		path = "/api/open/task/create"
		api = self.url + path
		data = {
			"flowCode" : flow_code,
			"args":args,
			"callbackUrl":call_back_url,
			"workerName":worker_name,
			"envName":env,
			"isNow":is_now

		}
		# print(data)
		rep = requests.post(api,params=self.params,
				data = json.dumps(data), headers=self.headers
			)
		return rep.json()

	@aq_sign
	def query_task(self, task_id):
		path = "/api/open/task/status/%s"
		api = self.url + path %task_id
		rep = requests.get(api, params=self.params, headers=self.headers)
		return rep.json()

	@aq_sign
	def pget(self, param, env):

		path = "/api/open/parameter/get"
		api = self.url + path
		data = {
			'paramName':param,
			'envName':env
		}

		rep = requests.post(url=api,params=self.params,headers=self.headers,data=json.dumps(data))
		return rep.json()

	@aq_sign
	def pset(self, param, env, value):
		# self.acquire_sign()
		path = "/api/open/parameter/set"
		api = self.url + path
		data = {
			'paramName':param,
			'envName':env,
			'value':value
		}
		rep = requests.post(url=api,params=self.params,headers=self.headers,data=json.dumps(data))
		return rep.json()

	@aq_sign
	def push(self, name, env,  content, delay=0, expired=EXPIRED):
		path = "/api/open/queue/push"
		api = self.url + path
		data = {
			"queueName":name,
			"envName":env,
			"content":content,
			"delay":delay,
			"expired":expired
		}

		rep = requests.post(api,params=self.params, headers=self.headers, data=json.dumps(data))
		return rep.json()

	@aq_sign
	def pull(self, name, env):
		path = "/api/open/queue/pull"
		api = self.url + path
		data = {
			"queueName":name,
			"envName":env,

		}

		rep = requests.post(api,params=self.params, headers=self.headers, data=json.dumps(data))
		return rep.json()

if __name__ == "__main__":
	static_str = "afd8426953b54e23b925a63dff4bf7ed"
	app_key = "b7844db63e9b48cca1c72e67769f8714"
	app_secret = "b5f8594647aa43318e6764a3af485a6d"
	flow_code = "cea5e4afb3a611eaa04a0242ac110002"
	callbackUrl = ''
	req_url = "http://test01.uibot.com.cn"

	api = CommanderAPI(req_url,static_str,app_key,app_secret)
	# print(api.push('list6','test',"{'T':'就是干'}"))
	# 
	# x = api.pull('list6','test')
	# print(x)
	# print(type(x))

	task_id = api.add_task(flow_code,"test_res",args={"A":1},)
	# print(task_id)
	# print(api.query_task(task_id['data']['taskId']))

	# {'success': False, 'message': "The value '{'data': {'taskId': 1688}, 'code': 0, 'message': ''}' is not valid.", 'data': None}
	# print(api.pset('param3','jiuguai', {"Z":"dota"}))
	# print(api.pget('param3','test'))










