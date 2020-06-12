import re

import pandas as pd
import requests
PAGE_SIZE = 10
MAX_SIZE = 5000


class EmploymentSys():
    def __init__(self, cookie):
        
        self.headers = {
    
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            # "Content-Length": "546",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Cookie": "%s" %cookie,
            "Host": "222.240.173.92:7001",
            "Origin": "http://222.240.173.92:7001",
            "Pragma": "no-cache",
            "Referer": "http://222.240.173.92:7001/hnpes/unemployment/unemployment!unemploymentListUI.action",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
            "X-Requested-With": "XMLHttpRequest",

        }
     
        self.data = {
            "transMap.ajr003": "1",
            "transMap.ajr002": "3",
            "transMap.aae027": "430111005000",
            "transMap.aac002": "",
            "transMap.aac003": "",
            "transMap.aac021": "",
            "transMap.aac004": "",
            "transMap.begin_sy": "",
            "transMap.after_sy": "",
            "transMap.begin_sydj": "",
            "transMap.after_sydj": "",
            "page": "1",
            "pagesize": "1",
            "sort": "aae036",
            "dir": "desc",  
 
        }
    
    def set_cookie(self, cookie):
        self.headers.update({
                "Cookie":cookie
            }) 

    def get_employment(self, area_code,page=1, page_size=PAGE_SIZE):
        """就业登记访问
        
        默认访问区域为雨花区
        
        Keyword Arguments:

            page {number} -- 第几页 (default: {1})
            page_size {number} -- 每页多少条数据 (default: {100})
        """
        url = "http://222.240.173.92:7001/hnpes/unemployment/unemployment!employmentListData.action"

        self.data.update({
                "transMap.ajr002":"1",
                "transMap.aae027":area_code,
                "page": page,
                "pagesize": page_size,
        })
        self.headers.update({
            "Referer": "http://222.240.173.92:7001/hnpes/unemployment/unemployment!employmentListUI.action"
        })

        rep = requests.post(url, headers=self.headers, data=self.data)
        content_type = rep.headers.get('Content-Type',"")
        if content_type.startswith('application/json;'):
            return {"code":0, "data":rep.json()}
        else:
            txt = rep.text
            if "验证码" in rep.text:
                return {"code":2, "err_msg":"cookie过期"}
            return {"code":3, 'err_msg':txt}

    def get_employment_details(self,):
        url = "http://222.240.173.92:7001/hnpes/unemployment/unemployment!detailEmploymentUI.action"
        params = {
            "transMap.ajr002": "1",
            "transMap.aje001": "00000005744797"

        }
        self.headers.update({
            "Referer": "http://222.240.173.92:7001/hnpes/unemployment/unemployment!employmentListUI.action"
        })
        rep = requests.get(url, params=params, headers=self.headers)
        return rep.text

    def get_unemployment(self, area_code,page=1, page_size=PAGE_SIZE):
        """访问失业登记
        
        默认区域为雨花区
        
        Keyword Arguments:
            page {number} -- 第几页 (default: {1})
            page_size {number} -- 每页多少条 (default: {100})
        """

        url = "http://222.240.173.92:7001/hnpes/unemployment/unemployment!unemploymentListData.action"

        self.data.update({
                "transMap.ajr002":"3",
                "transMap.aae027":area_code,
                "page": page,
                "pagesize": page_size,
        })
        self.headers.update({
            "Referer": "http://222.240.173.92:7001/hnpes/unemployment/unemployment!unemploymentListUI.action"
        })

        rep = requests.post(url, headers=self.headers, data=self.data)
        content_type = rep.headers.get('Content-Type',"")
        if content_type.startswith('application/json;'):
            return {"code":0, "data":rep.json()}
        else:
            txt = rep.text
            if "验证码" in rep.text:
                return {"code":2, "err_msg":"cookie过期"}
            return {"code":3, 'text':txt}



    def get_unemployment_details(self, serial):
        url = "http://222.240.173.92:7001/hnpes/unemployment/unemployment!detailEmploymentUI.action"
        params = {
            "transMap.ajr002": "3",
            "transMap.ajn001": serial
        }
        self.headers.update({
            "Referer": "http://222.240.173.92:7001/hnpes/unemployment/unemployment!unemploymentListUI.action"
        })
        rep = requests.get(url, params=params, headers=self.headers)
        
        return self.extract_unemployment_details(rep.text)


    def extract_unemployment_details(self, txt):
        groups = ['人员基础信息','失业登记信息','就业意向信息登记','培训意向信息登记'][::-1]
        gender_map = {
            '1':"男",
            '2':"女",
            '9':"未说明性别"
        }


        val_com = re.compile('<input.+?type="text".+?value="(.*?)"')
        def extract(txt):
            
            r = val_com.search(txt)
            if r:
                return r.group(1)
            else:
                return ""
        patt = '<td class="tdLabel"[^>]*?>\s?<label[^>]+?>(.+?)</td>\s+<td class="tdInput"[^>]*?>(.+?)</td>'
        count = 0
        col_com = re.compile('[^<（\(]+')

        data = {}
        for r in re.finditer(patt,txt,re.S):
            g = r.groups()
            col = col_com.search( g[0]).group()
            if col == "备注":
                col = groups.pop() + "备注"
            data[col] = extract(g[1])
                


        data['性别'] = gender_map[data['性别']]

        return data


es = None
def init(cookie):
    global es
    es = EmploymentSys(cookie)

def get_unemployment_new_data(area, id_card, date_time):
    """寻找失业新增的一条数据
    
    Arguments:
        area {[str]} -- 区域
        id_card {[str]} -- 身份证
        date_time {[str]} -- 时间
    
    Returns:
        [dict] -- [返回一个结果集合]
    """
    dt = pd.to_datetime(date_time)
    count = 0
    page_size = PAGE_SIZE
    while True:

        result = es.get_unemployment(area ,page_size=page_size)

        if result['code'] != 0:
            return result

        data = result['data']
        df = pd.DataFrame(data['rows'])
        df.rename(columns={
            "aac002":"id_card",
            "aae036":"handle_time",
            "ajn001":"serial"
        },inplace=True)
        df = df[['id_card','handle_time','serial']]
        df['handle_time'] = pd.to_datetime(df['handle_time'])
        result_df = df [(df['id_card'] == id_card) & (df['handle_time'] == dt)]


        if len(result_df) != 0:
            index = result_df.index.to_list()[0]
            if index == 0:
                return {"code":-1,"msg":"无更新数据"}
            else:
                serial = df.iloc[85]['serial']
                return {"code":0,"data":es.get_unemployment_details(serial)}
        
        if page_size > len(df) :
            raise 'NOT FOUND'
        
        if page_size > MAX_SIZE:
            raise "超过范围阈值%s条 未找到建议采用其他策略填取" %MAX_SIZE
        
        page_size += page_size * 2
        
if __name__ == "__main__":
    from pprint import pprint
    # 430111005000 雨花区
    # 430103105005 天心区
    # transMap.aae027: 430103105005  代表区域
    # transMap.ajr002: 1  1:代表就业 3代表失业

    #  
    area = "430111005000"
    dt = "2020-04-10 11:50:42"
    id_card = "430103196407071532"
    cookie = "loginUser=cs0412; UserToken=307C637330343132; UserIndentity=ACPfeaoDT1LrPSHJ0j291gfgBB8CWnt9B6PumSfmULWWubap/vECHA=="
    # init(cookie)
    # print(get_unemployment_new_data(area,id_card,dt))


    # loginUser=cs0412; UserToken=307C637330343132; UserIndentity=uIeGK21FiZEOfCOgc7HjrlplOx+Epg5e2n8Sp1it1Jqprk1ndbBHMw==
    es = EmploymentSys(cookie)
    # pprint(es.get_employment("430111005000",page_size=2))
    # pprint(es.get_unemployment("430111005000"))
    # txt = es.get_unemployment_details("00316033018864")
    txt = es.get_employment_details("15912545268343887")
    print(txt)
    # pprint(es.extract_unemployment_details(txt))