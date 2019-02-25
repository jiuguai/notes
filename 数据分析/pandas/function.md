

```python
import pandas as pd
# 读取
df = pd.read_excel("双十一淘宝美妆数据.xlsx",sheetname=0)


df1 = df.groupby('age')['pp'].agg({'min':'min','max':'max'})

# 含有二级菜单
df2 = df.groupby('age').agg({'pp':{'min':'min','max':'max'}})

# df1['min'] == df2['pp']['min']



# 存入excel
writer = pd.ExcelWriter('姬.xlsx')
df2_4.to_excel(writer,'ji',index=False)
writer.save()

# 存入csv 中
df_ye.to_csv("叶迁徙_3.csv",index=False)
```