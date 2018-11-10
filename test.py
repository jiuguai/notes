from urllib.parse import parse_qs,urlparse
import json

class ParseURLQuery:
	__map = {
		'furl':'fq',
		'surl':'sq'
	}
	def __init__(self,furl,surl):
		self.furl = furl
		self.surl = surl
		

	def get_json(self,indent=4):
		s = json.dumps(self.diff,indent=4)
		self.diff_beauty = s

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
		self.get_json()


	@staticmethod
	def parse_query(url,dropli=True):
		ParseResult = urlparse(url)
		d = parse_qs(ParseResult.query)
		def drop_li(v):
			if isinstance(v,(list,tuple)):
				return ','.join(v)
			return v
		
		if dropli:
			return {k:drop_li(d[k]) for k in d}
		return d

	def __repr__(self):

		return self.diff_beauty


	def __setattr__(self,name,value):
		if name in self.__map.keys():
			self.__dict__[name] = value
			self.__dict__[self.__map[name]] = self.parse_query(value)
			if 'furl' in self.__dict__ and 'surl' in self.__dict__:
				self.query_diff()

		else:
			super().__setattr__(name,value)








PUQ = ParseURLQuery


url1 = 'https://data.bilibili.com/v/flashplay/h5_player_op?pname=6&mid=236367692&statue=3&playmethod=2&avid=25296249&eventparam=464&progress=327&displayid=85fae993b2e8407043041d226940d6b8&eventid=http_connection_time&trackerid=&cid=42859600&fver=HTML5PlayerNewccf43e3&seasonid=&epid=&videotype=1&fid=web_player&ctime=1541777708655&readystate=1'


url2 = 'https://data.bilibili.com/v/flashplay/h5_player_op?pname=6&mid=236367692&statue=3&playmethod=2&avid=25296249&eventparam=6349&progress=227&displayid=85fae993b2e8407043041d226940d6b8&eventid=end_load&trackerid=&cid=42859600&fver=HTML5PlayerNewccf43e3&seasonid=&epid=&videotype=1&fid=web_player&ctime=1541777449105&readystate=4'

url3 = 'https://data.bilibili.com/v/flashplay/h5_player_op?pname=6&mid=236367692&statue=3&playmethod=2&avid=25296249&eventparam=6349&progress=227&displayid=85fae993b2e8407043041d226940d6b8&eventid=end_load&trackerid=&cid=42859600&fver=HTML5PlayerNewccf43e3&seasonid=&epid=&videotype=1&fid=web_player&ctime=1541777449105&readystate=3'
p = PUQ(url1,url2)
print(p)
p.surl = url3
print(p)
# fq = parse_query(url1)
# sq = parse_query(url2)
# print(fq)
# print(sq)


	
# fq = {k:drop_li(fq[k]) for k in fq}
# sq = {k:drop_li(fq[k]) for k in sq}
# print('='*30)
# print(fq)
# print(sq)

# d = query_diff(fq,sq)
# s = get_json(d)
# print(s)

