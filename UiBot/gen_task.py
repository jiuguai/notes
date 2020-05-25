import json


import pymysql

import pandas as pd

con_dic = {
    "user":"uibot",
    "password":"OHdSK3Ab0iuvgDrn",
    "host":"192.168.75.130",
    "port":3306,
    "charset":'utf8mb4',
    "database":"uibot_entwebconsole"
    
    
}


#  BankData, LogInformation, SubAccount, TarikhBil



con = pymysql.connect(**con_dic)

cursor = con.cursor()



def get_df(sql):
    cursor.execute(sql)

    
    cols  = [col[0] for col in cursor.description]
    return pd.DataFrame(list(cursor.fetchall()),columns=cols)


def alloc_task()

    # 读取并表

    ​sql = """
    SELECT
        ID,
        `STATUS`,
        bankName,
        flowID,
        workerName,
        dataQueueName,
        bankUrl,
        loginFlag,
        userName,
        a.ID_Num,
    typeDate, fristStart, fristEnd, secondStart, secondEnd
    FROM
        BankData as a
    left JOIN TarikhBil as b ON a.ID_num = b.ID_Num;

    """


    df = get_df(sql)
    sql = "SELECT * from SubAccount;"
    sub_df = get_df(sql).rename(columns={"ID":"accountID"})
    merger_df = pd.merge(df, sub_df,how='left',left_on='ID',right_on="bankDataID")



    # 加工成任务参数
    account_cols = sub_df.columns
    m_cols = merger_df.columns
    origin_cols = list(set(m_cols) - set(account_cols))



    def func(g):
        account_data = g[account_cols].to_json(orient="records",force_ascii =False)
        origin_df = g[origin_cols]
        origin_ser = origin_df.iloc[0]
        origin_ser['account'] = json.loads(account_data)
        return origin_ser
    result = r.groupby("ID").apply(func)

    con.close()
    return result