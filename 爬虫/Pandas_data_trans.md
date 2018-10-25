# 通过pandas 实现 数据库 之间数据转换

## MongoDB
```python
import pandas as pd
import pymongo
cli = pymongo.MongoClient('localhost',27017)
col = cli.db.col
# 读取
df = pd.DataFram(list(col.find()))

# 存储 
from sqlalchemy import create_engine
# echo 为True 表示返回操作记录
engine = create_engine("mysql://root:root@127.0.0.1:3306/soufang?charset=utf8",echo=False)
# is_exist="replace|append|fail
df.to_sql("cs_zu_table",engine,is_exist="append")



cli.close()
```

## MySQL
```python
import pandas as pd
import pymysql
con = pymysql.connect(
        host="localhost",user="root",
        password="root",database="soufang",
        port=3306,
)

# 读取
query_SQL = "select * from new_house"
df = pd.read_sql(query_SQL,con=con)

# 存储
import json
new_cs_zu = cli.soufang.new_cs_zu
new_cs_zu.insert(json.loads(df1.to_json(orient="records")))

con.close()
```

