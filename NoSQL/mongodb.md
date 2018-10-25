## 安装

>[高级查询](https://www.jb51.net/article/48216.htm)


#### 1.MongoDB
#### 2.MongoDB Compass : 与MongoDB分开安装

## 制作 windows 服务
#### 1. 创建mongod.cfg
```config
dbpath="data_path"
logpath="F:\ProgramFile\MongoDB\log\mongod.log"

```
#### 2.安装服务
```cmd
mongod --config "mongod.cfg" --install
```

#### 3.启动服务：net start mongodb
#### 4.关闭服务：net stop mongodb
#### 5.移除服务："../mongod.exe" --remove

## 常用概念
#### 1.文档(document):json格式
#### 2.集合(collection):文档的集合

## 操作命令
#### 1.db
#### 2.show dbs
#### 3.use db_name : 切换或者新建 添加数据后才能 show dbs 中显示出来
#### 4.db.dropDatabase()
#### 5.db.insert({})
#### 6.db.collenction.find() : 查找更多数据

## Python 操作 MongoDB
> pip install pymongo

```python
    import pymongo

    # 连接
    cli = pymongo.MongoClient("127.0.0.1",port=27017)
    
    # 创建数据库
    db = cli.zhihu

    # 创建集合
    collection = db.qa

    # 添加
    collection.insert([{"username":"zero",'type':1},
        {"username":"wind",'type':2}

        ])
    collection.insert({"user":"zero"})

    # 查找数据
    ## 返回多条
    cursor = collection.find({'username':"zero"})
    print(list(cursor))
    ## 返回一条
    data1 = collection.find_one({'user':"zero"})
    print(data1)

    # 更新
    collection.update_one({"user":"zero"},{"$set":{"age":18,"type":"test"}})
    collection.update_many({"username":"zero"},{"$set":{"age":18}})

    # 删除
    collection.delete_one({"usernam":"zero"})
    collection.delete_many({"usernam":"zero"})
    cli.close()
```