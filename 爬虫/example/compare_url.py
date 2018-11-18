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


url1 = 'https://cn-zjwz3-dx-v-07.acgvideo.com/upgcxcode/48/13/63401348/63401348-1-30080.m4s?expires=1542564600&platform=pc&ssig=YC5TzyDmgZwrOB4E5InNiA&oi=3740590929&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=&trid=c2dc525ad1cd437d98525e04a61ba798&nfc=1'


url2 = 'https://cn-zjwz3-dx-v-07.acgvideo.com/upgcxcode/48/13/63401348/63401348-1-30080.m4s?expires=1542564600&platform=pc&ssig=YC5TzyDmgZwrOB4E5InNiA&oi=3740590929&hfb=Yjk5ZmZjM2M1YzY4ZjAwYTMzMTIzYmIyNWY4ODJkNWI=&trid=c2dc525ad1cd437d98525e04a61ba798&nfc=1'

p = UQD(url1,url2)
print(p)

