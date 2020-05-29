import json
import os
import sys
import datetime
import warnings

warnings.filterwarnings('ignore')

import pymysql
import numpy as np
import pandas as pd

from settings import *
from commander_api import CommanderAPI
print(MYSQL_CON_DIC)


#  BankData, LogInformation, SubAccount, TarikhBil

class InitTaskData():

    def __init__(self):
        self.con = pymysql.connect(**MYSQL_CON_DIC)

        self.cursor = self.con.cursor()

    def __del__(self):
        try:
            self.con.close()
        except:
            pass

    def get_df(self, sql):
        self.cursor.execute(sql)
        
        cols  = [col[0] for col in self.cursor.description]
        return pd.DataFrame(list(self.cursor.fetchall()),columns=cols)


    def alloc_task(self):
        """
            ID,
            `STATUS`,
            bankName,
            customerId,
            operator,
            loginKeyboxId,
            loginKeyboxIndex,
            
            flowID,
            workerName,
            dataQueueName,
            bankUrl,
            loginFlag,
            userName,
            expireTime,
            a.ID_Num,
            a.numID,
            
        
        """


        HOUR = datetime.datetime.now().hour
        if HOUR == POS_TASK_HOUR:
            search = "="
        else:
            search = "<>"

        # 读取并表 (排序交给后面处理)
        sql = ''' SELECT
                a.*,
            typeDate, fristStart, fristEnd, secondStart, secondEnd
            FROM
                BankData as a
            left JOIN TarikhBil as b ON a.ID_num = b.ID_Num
            where a.status = 1 and a.dataQueueName %s "银联POS"
            ;

        '''%(search)


        df = self.get_df(sql)

        # 本想放入SQL中，为了后面数据处理，决定分开
        sql = "SELECT * from SubAccount;"
        sub_df = self.get_df(sql).rename(columns={"ID":"accountID"})

        sub_df.drop(columns=['founder', 'updateTime', 'createTime'],inplace=True)
        merger_df = pd.merge(df, sub_df,how='left',left_on='ID',right_on="bankDataID")


        # 加工成任务参数
        account_cols = sub_df.columns   # 这里体现出分开好处
        m_cols = merger_df.columns
        origin_cols = list(set(m_cols) - set(account_cols))



        def func(g):
            account_data = g[account_cols].to_json(orient="records",force_ascii =False)
            origin_df = g[origin_cols]
            origin_ser = origin_df.iloc[0]
            origin_ser['account'] = json.loads(account_data)
            return origin_ser
        result = merger_df.groupby("ID").apply(func)

    
        return result


    def infomation(self,data):
        ds = pd.to_datetime(data['expireTime'])
        diff_day = ds - pd.to_datetime(datetime.date.today())
        diff_day = diff_day.apply(lambda z:z.days)
       
        # 异常数据检测
        data['flowId'] = data['flowId'].fillna("")
        data['dataQueueName'] = data['dataQueueName'].fillna("")
        data['abnormal_state'] = 0
        data['abnormal_state'][(data['flowId']=="") | (data['dataQueueName']=="")] = 1


        # 过期ID检测
        data['expired_state'] = np.nan
        data['expired_state'][diff_day>15] = 0
        data['expired_state'][(diff_day>=0) & (diff_day <=15)] = 1
        data['expired_state'][diff_day<0] = 2
        data['expired_state'][diff_day.isnull()] = 0
        data['expired_state'] = data['expired_state'].astype(int)

        return data


    def __call__(self):
        result = self.alloc_task()
     
        data = self.infomation(result)

        d = {}

        # 正常
        d['normal_data'] = data[
            (data['expired_state'] < 2) & 
            (data['abnormal_state'] == 0)
        ].sort_values(by=['numID'])

        # 异常数据 fllowID 或 dataQueueName 为空
        d['abnormal_data'] = data[data['abnormal_state'] == 1]
        
        # 快到期
        d['expiring_soon_data'] = data[data['expired_state'] == 1]


        # 过期

        d['expired_data'] = data[data['expired_state'] == 2]


        return d

if __name__ == "__main__":
    
    static_str = "afd8426953b54e23b925a63dff4bf7ed"
    app_key = "b3e44d7b862143cca5a0f6ff136a59c5"
    app_secret = "f543cfbce1a246d6ba436cee7f125270"
    req_url = "http://192.168.75.130"
    api = CommanderAPI(req_url,static_str,app_key,app_secret)

    l = []
    l.append("UP")
    l.append("DOWN")
    # l.append("SAVE_XL")
    # 
    if "UP" in l:
        result = InitTaskData()()
        normal_data = result['normal_data']

        for i,row in normal_data[[
                    'abnormal_state','expired_state',
                    'bankUrl','workerName', 
                    'loginFlag','dataQueueName', 'flowId', 'account',
                    "customerId",
                    "userName",
                    "operator",
                    "loginKeyboxId",
                    "loginKeyboxIndex",
                    "certKeyboxId",
                    "certKeyboxIndex",
                    "usbhubIp",
                    "usbhubPort",
                    "fristStart",
                    "fristEnd",
                    "secondStart",
                    "secondEnd",
                    "bankName"

                ]].iterrows():
            # row['dataQueueName']
            js = row.to_frame().T.to_json(orient="records",force_ascii =False)
            print(js)
            print(api.push(row['dataQueueName'], 'test', js))
     
    

    if "DOWN" in l:

        for bank in ["北京银行", "浙商银行", "交通银行", "光大银行"]:
            while True:
                print("-------------%s" %bank)
                if bank != "北京银行":break

                result = api.pop(bank,"test")
                

                if result['code'] != 0 :
                    print(result)
                    break
                    
                

                data = result['data']
                
                if data is None: break


                content = json.loads(data['content'])[0]
     
                # print(type(content))
                print(content)
                if content['workerName'] == "Worker01":
                    print(content['workerName'])
                    r = api.add_task(content['flowId'] ,content['workerName'], 'test',args={"data":content} )
                    print(r)


    # 
    if "SAVE_XL" in l:
        book_name = "information %s.xlsx" %datetime.datetime.today().strftime("%Y-%m-%d %H_%M_%S")
        book_path = os.path.join(DESKTOP_DIR, book_name )

        l  = ["normal_data","abnormal_data","expiring_soon_data","expired_data"]
        writer = pd.ExcelWriter(book_path)
        for k in l:
            result[k].to_excel(writer, sheet_name=k, index=False)

        writer.save()
