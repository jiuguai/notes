[存取](https://blog.csdn.net/tz_zs/article/details/81137998)

```python
import pandas as pd
df = pd.DataFrame()
df.replace()
df['A'].str.replace
df['A'].str.extract('regex')  # 默认正则表达式不可修改
df['A'].str.contains          # 默认正则表达式可以修改
df['B'].describe()
df.sort_values(['A','B'])
df['A'].value_counts()
df['a'].astype(np.float64)
pd.pivot_table(data,values,columns,index,aggfunc)
pd.cross_table() # 频率统计
df.duplicated(['A'])
df.drop_duplicates(['A'])
pd.cut(s,[2,4,6],labels=['l', 'm', 'h'])
pd.cut(s,3)
```

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


# 存为xlsm格式
writer = pd.ExcelWriter('姬.xlsx',engine="xlsxwriter") # pip3 install xlsxwriter
df2_4.to_excel(writer,'ji',index=False)
workbook = writer.book
workbook.filename = "姬.xlsm"
wb.add_vba_project('./vbaProject.bin') # ./vbaproject.bin
writer.save()
# 存入csv 中
df_ye.to_csv("叶迁徙_3.csv",index=False)
```

1. 修补
    df1.combine_first(df2)

2. 更新
    df1.update(df2)

