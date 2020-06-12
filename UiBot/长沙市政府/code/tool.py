import datetime

import pandas as pd


def allow_retry(datetime_l, count, max_interval_seconds):
    if len(datetime_l) <= count:
        
        return {'allow_retry':True, "compare_list":datetime_l}
    datetime_l = datetime_l[len(l)-count-1:]
    ser = pd.to_datetime(l)
    ser.name = 'A'
    dx = pd.DataFrame(ser)
    df = pd.concat([dx,dx.rename(columns={"A":"B"}).shift(1)],axis=1).dropna()
    temp = df["A"] - df['B']

    return {
        "allow_retry":any(temp.apply(lambda x:x.total_seconds()) > max_interval_seconds),
        "compare_list":datetime_l
    }

    '''另一种写法
        另一种实现
    
    '''

    # if len(datetime_l) <= count:
    #     return {'allow_retry':True, "compare_list":datetime_l}
    
    # datetime_l = datetime_l[len(l)-count-1:]
    # length = len(datetime_l)
    # dt_l = pd.to_datetime(datetime_l).tolist()
    # seconds_l = []
    # for i in range(length-1, 0, -1):
    #     dt = (dt_l[i] - dt_l[i-1]).total_seconds()
    #     seconds_l.append(dt)
    

    # return {
    #     "allow_retry":any(pd.Series( seconds_l) > max_interval_seconds),
    #     "compare_list":datetime_l
    # }





if __name__ == "__main__":
    l = ["2020-06-10 20:20:20", "2020-06-10 20:22:20", "2020-06-10 20:23:20", "2020-06-10 20:24:50"]

 
    print(allow_retry(l, 2, 120))
