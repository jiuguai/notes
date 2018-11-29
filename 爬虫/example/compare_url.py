from urllib.parse import parse_qs, urlparse, parse_qsl
import json

def beautiful_collections(colle,indent=4):
	s = json.dumps(colle,indent=4)
	return s

def parse_query(url,dropli=True):
		"""解析url
		
		将url中的query字段解析出来
		
		Arguments:
			url {string} -- 需要解析的url
		
		Keyword Arguments:
			dropli {bool} -- 使用urllib 中parse_qs 解析出来的结果默认为列表 (default: {True})
		
		Returns:
			dict -- 将键值对以字典形式返回
		"""
		ParseResult = urlparse(url)
		d = parse_qs(ParseResult.query)
		def remove_li(v):
			if isinstance(v,(list,tuple)):
				return ','.join(v)
			return v
		
		if dropli:
			return {k:remove_li(d[k]) for k in d}
		return d

class URLQueryDiff:
	"""
	解析比较两URL query 字段

	"""
	__map = {
		'furl':'fq',
		'surl':'sq'
	}

	def __init__(self,furl,surl):
		self.furl = furl
		self.surl = surl
		
	def query_diff(self):
		d = {
			'fq_sq_diff':{},
			'fq_unique':{},
			'sq_unique':{},
		}
		
		for k,v in self.fq.items():

			if k in self.sq:
				if self.fq[k] != self.sq[k]:
					d['fq_sq_diff'][k] = (self.fq[k],self.sq[k])
			else:
				d['fq_unique'][k] = self.fq[k]

		for k in (set(self.sq) - set(self.fq)):
			d['sq_unique'][k] = self.sq[k]

		self.diff = d
		self.diff_beauty = beautiful_collections(self.diff)


	

	def __repr__(self):

		return self.diff_beauty


	def __setattr__(self,name,value):
		if name in self.__map.keys():
			self.__dict__[name] = value
			self.__dict__[self.__map[name]] = parse_query(value)
			if 'furl' in self.__dict__ and 'surl' in self.__dict__:
				self.query_diff()

		else:
			super().__setattr__(name,value)



if __name__ == '__main__':
	UQD = URLQueryDiff

	url1 = 'https://note.youdao.com/yws/api/group/10042410/file/187069773?method=download&inline=true&version=1&shareToken=A4EB9037044F4694B41708140F5A9FED'

	url2 = 'https://note.youdao.com/yws/api/group/10042410/file/187069775?method=download&inline=true&version=1&shareToken=A4EB9037044F4694B41708140F5A9FED'

	p = UQD(url1,url2)
	print(p)

	"""外部函数测试
	
	外部函数的返回值
	"""
	# q = urlparse(url1)
	# print(q.query)
	# x = parse_qs(q.query)
	# print(x)
	# x = parse_qsl(q.query)
	# print(x)

