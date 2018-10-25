
>[Windos版本](https://github.com/MicrosoftArchive/redis/releases)

>[redisManager](https://github.com/uglide/RedisDesktopManager/releases)

>默认端口 6379

# 配置
## 配置
修改 ：redis.windows.conf
bind：192.168.0.51 所有客户端通过此IP访问
0.0.0.0 代表任意自己拥有的IP
## 开启服务
    redis-server.exe redis.windows.conf


# 安装
## Ubuntu
1. 安装
```shell
sudo apt-get install redis-server
```
2. 卸载
```shell
sudo apt-get purge --auto-remove redis-server
```
3. 启动
```shell
# 查看
ps aux|grep redis
sudo service redis-server start
```
4. 停止
```shell
sudo service redis-server stop
```

#操作
## 字符串操作
set key value [EX ns]
get key
ttl key

keys * 查看所有key

## 列表
```shell
lpush key value [value ...]
rpush key value [value ...]
lrange key start end
lpop key
rpop key

# count -1 反方向  0 所有
lrem key count value

# 返回列表 索引对应的值
lindex key 1

# 返回列表长度
llen key
```

## 集合
```shell
# 添加
sadd key member [member ...]

# 查看
smembers key

# 移除
srem key member

# 查看元素个数
scard key

# 运算
# 交集
sinter key [key ...]
# 并集
sinter key [key ...]
# 差集
sdiff key [key ...]

# 验证时候存在
sismember key member

```

## hash
```shell
hset key field value
hgetall key
hget key field
hkeys key
hvals key

# 删除
hdel key field [field ...]

# 判断存在
hexists key field

# 判断键值对个数
hlen key

```



