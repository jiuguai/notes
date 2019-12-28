

git
    
    1. git add ...
    2. git checkout
    3. git reset
    4. git log

python 
    测试 __setattr__
    Super
    __enter__

## Pandas常用工具

##### 更改索引或者列名

```python
data.rename(
    mapper=None,
    index=None,
    columns=None,
    axis=None,
    copy=True,
    inplace=False,
    level=None,
)


data.rename(columns={"X":"C"})

```



##### 表格标准化
```python
data.reindex(
    labels=None,
    index=None,
    columns=None,
    axis=None,
    method=None,
    copy=True,
    level=None,
    fill_value=nan,
    limit=None,
    tolerance=None,
)
s
```


##### 值替换
```python

# regex=False
# method {'pad', 'ffill', 'bfill', `None`}

data.replace("(长沙)",r"湖南\1",regex=True,method="bfill")

```



##### 查看重复值

```python
# 用于筛选出重复值
data = data[data.duplicated(subset=["A","B"],keep=False)]

# 用于获取 组合字段是否 唯一
data.duplicated(subset=["A","B"]).any() # 为True 则有重复值

```

##### 清除重复值

```python
# keep = {'first', 'last', False}
data.drop_duplicate(subset=['A','B'])

```


##### 了解各字段信息
```python
# 查看各

#  percentiles = [0.25, 0.50, 0.75]
#  include = "all"
#  exclude = [np.object, "category", np.number]

df.describe(percentiles=[0.3, 0.6, 0.9])
```

##### 删除索引或者列


```python
# 默认 删除 index

df_t.drop(
    labels=None,
    axis=0,         # 默认为行
    index=None,     # 索引名
    columns=None,   # 列名
    level=None,     # 索引级别
    inplace=False,
    errors='raise', # {'ignore', 'raise'} default raise
)



```






>>>>>>> adad289399981bcab30f380310490e0d045a2ed4
