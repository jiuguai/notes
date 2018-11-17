from urllib.parse import parse_qs,urlparse
import json

def beautiful_collections(colle,indent=4):
	s = json.dumps(colle,indent=4)
	return s


class URLQueryDiff:
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


	@staticmethod
	def parse_query(url,dropli=True):
		ParseResult = urlparse(url)
		d = parse_qs(ParseResult.query)
		def remove_li(v):
			if isinstance(v,(list,tuple)):
				return ','.join(v)
			return v
		
		if dropli:
			return {k:remove_li(d[k]) for k in d}
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








UQD = URLQueryDiff


url1 = 'https://data.bilibili.com/v/flashplay/h5_player_op?pname=6&mid=236367692&statue=3&playmethod=2&avid=25296249&eventparam=464&progress=327&displayid=85fae993b2e8407043041d226940d6b8&eventid=http_connection_time&trackerid=&cid=42859600&fver=HTML5PlayerNewccf43e3&seasonid=&epid=&videotype=1&fid=web_player&ctime=1541777708655&readystate=1'


url2 = 'https://data.bilibili.com/v/flashplay/h5_player_op?pname=6&mid=236367692&statue=3&playmethod=2&avid=25296249&eventparam=6349&progress=227&displayid=85fae993b2e8407043041d226940d6b8&eventid=end_load&trackerid=&cid=42859600&fver=HTML5PlayerNewccf43e3&seasonid=&epid=&videotype=1&fid=web_player&ctime=1541777449105&readystate=4'

url3 = 'https://data.bilibili.com/v/flashplay/h5_player_op?pname=6&mid=236367692&statue=3&playmethod=2&avid=25296249&eventparam=6349&progress=227&displayid=85fae993b2e8407043041d226940d6b8&eventid=end_load&trackerid=&cid=42859600&fver=HTML5PlayerNewccf43e3&seasonid=&epid=&videotype=1&fid=web_player&ctime=1541777449105&readystate=3'
p = UQD(url1,url2)
print(p)
p.surl = url3
print(p)

