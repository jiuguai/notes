
[TOC]

# 通用

## [安装包](https://pan.baidu.com/s/1ztKKs42Uq5sCI_5dTXdfvQ)
    
> 提取码:p982


## [开放端口](https://www.cnblogs.com/Treelight/p/11101517.html)
```python
    firewall-cmd --zone=public --add-port=3306/tcp --permanent
    firewall-cmd --zone=public --add-port=80/tcp --permanent
    firewall-cmd --zone=public --add-port=27017/tcp --permanent
    firewall-cmd --zone=public --add-port=6379/tcp --permanent
    firewall-cmd --reload

```

# 离线安装

## redis

###[download](https://redis.io/download)

### 安装步骤

1. 下载 redis-5.0.8.tar.gz

2. tar -zxvf redis-5.0.8.tar.gz

3. mkdir /usr/local/redis && cd /usr/local/redis && mkdir log rdb bin conf

4. cd redis-5.0.8 & make

5. cd src && make install 

6. vi /usr/local/redis/conf/6379.conf

```conf
bind 0.0.0.0
dir /usr/local/redis/rdb/
dbfilename redis_6379.rdb
logfile /usr/local/redis/log/redis_6379.log
pidfile /var/run/redis_6379.pid
protected-mode no
daemonize yes
save 900 1
save 300 10
save 60 10000

```

7. vi /etc/init.d/redisd
```bash
#!/bin/sh
#
# Simple Redis init.d script conceived to work on Linux systems
# as it does use of the /proc filesystem.

### BEGIN INIT INFO
# Provides:     redis_6379
# Default-Start:        2 3 4 5
# Default-Stop:         0 1 6
# Short-Description:    Redis data structure server
# Description:          Redis data structure server. See https://redis.io
### END INIT INFO

REDISPORT=6379
BASE_DIR=/usr/local/redis
EXEC=/usr/bin/redis-server
CLIEXEC=/usr/local/bin/redis-cli

PIDFILE=/var/run/redis_${REDISPORT}.pid
CONF=${BASE_DIR}/conf/${REDISPORT}.conf

case "$1" in
    start)
        if [ -f $PIDFILE ]
        then
                echo "$PIDFILE exists, process is already running or crashed"
        else
                echo "Starting Redis server..."
                $EXEC $CONF
        fi
        ;;
    stop)
        if [ ! -f $PIDFILE ]
        then
                echo "$PIDFILE does not exist, process is not running"
        else
                PID=$(cat $PIDFILE)
                echo "Stopping ..."
                $CLIEXEC -p $REDISPORT shutdown
                while [ -x /proc/${PID} ]
                do
                    echo "Waiting for Redis to shutdown ..."
                    sleep 1
                done
                echo "Redis stopped"
        fi
        ;;
    *)
        echo "Please use start or stop as first argument"
        ;;
esac

```

8. chkconfig --add redisd 

9. chkconfig redisd on

10. 内存分配策略

> 可选值：0、1、2

>0 表示内核将检查是否有足够的可用内存供应用进程使用；如果有足够的可用内存，内存申请允许；否则，内存申请失败，并把错误返回给应用进程。

>1 表示内核允许分配所有的物理内存，而不管当前的内存状态如何。

>2 表示内核允许分配超过所有物理内存和交换空间总和的内存

    1. vi /etc/sysctl.conf
 
    2. 内容添加vm.overcommit_memory = 1

    3. 使生效sysctl -p 



## docker

### download: [tgz](https://download.docker.com/linux/static/stable/x86_64/) [rpm](https://download.docker.com/linux/centos/7/x86_64/stable/Packages/)
> 建议选择 rpm

### 安装步骤

1. 下载 docker-19.03.9.tgz

2. tar zxvf docker-19.03.9.tgz

3. mv docker-19.03.9 /usr/local/docker

4. vi /etc/profile
```bash

# 添加
export PATH=$PATH:/usr/local/docker

```
5. 开启服务
    
    dockerd &

## mogodb

### [download](https://www.mongodb.com/try/download/community)

### 安装步骤

1. 下载 mongodb-linux-x86_64-rhel70-4.2.8.tgz

2. tar -zxvf  mongodb-linux-x86_64-rhel70-4.2.8.tgz

3. mv mongodb-linux-x86_64-rhel70-4.2.8 /usr/local/mongodb

4. cd /usr/local/mongodb && mkdir data log conf pid

5. vi /etc/profile
```bash
# 追加
export PATH=$PATH:/usr/local/mongodb

```
6. source profile

7. vi /usr/local/mongodb/conf/27017-mongodb.conf
```yaml

storage:
   dbPath: /usr/local/mongodb/data
   journal:
      enabled: true

net:
   bindIp: 0.0.0.0
   port: 27017

processManagement:
   fork: true
   pidFilePath: /usr/local/mongodb/pid/mongodb-27017.pid

systemLog:
   destination: file
   path: "/usr/local/mongodb/log/mongodb-27017.log"
   logAppend: true

```

8. vi /etc/init.d/mongod
```bash
#!/bin/sh
#
# Simple Redis init.d script conceived to work on Linux systems
# as it does use of the /proc filesystem.

### BEGIN INIT INFO
# Provides:     mongodb_27017
# Default-Start:        2 3 4 5
# Default-Stop:         0 1 6
# Short-Description:    mongodb data structure server
# Description:          mongodb data structure server. See https://www.mongodb.com
### END INIT INFO

PORT = 27017
MONGO_HOME=/usr/local/mongodb
MONGO_BIN=${MONGO_HOME}/bin
MONGO_LOG=${MONGO_HOME}/log
MONGO_DATA=${MONGO_HOME}/data
MONGO_CONF=${MONGO_HOME}/conf

MONGO_BIN_MONGOD=${MONGO_BIN}/mongod
MONGO_CONF_MONGOD=${MONGO_CONF}/${PORT}-mongodb.conf
MONGO_LOG_MONGOD=${MONGO_LOG}/mongodb-${PORT}.log
MONGO_BIN_MONGO=${MONGO_BIN}/mongo

start()
{
    tmp=`ps -ef | grep ${MONGO_BIN_MONGOD} | wc -l`
    if [ $tmp -gt 1 ]; then
      echo "The server arealdy started...abort!"
      exit 1
    fi
    deleteLock
    cd ${MONGO_BIN}
    ${MONGO_BIN_MONGOD} --config ${MONGO_CONF_MONGOD}
    echo "Start MongoDB server in ${MONGO_BIN_MONGOD} OK!"
}

stop()
{
    cd ${MONGO_BIN}
    ${MONGO_BIN_MONGO} admin --eval "db.shutdownServer()"
    echo "Stopped MongoDB server"
}

usage()
{
        echo "Usage: $0 [start|stop|restart]"
}

deleteLock()
{
    echo "Deleting mongod.lock"
    cd ${MONGO_DATA}
    /bin/rm -f mongod.lock
    echo "Delete mongod.lock OK!"
}

if [ $# -lt 1 ];then
        usage
        exit
fi

if [ "$1" = "start" ];then
        start

elif [ "$1" = "stop" ];then
        stop

elif [ "$1" = "restart" ];then
        stop
        start

else
        usage
fi

```
9. chkconfig --add mongod

10. chkconfig mongod on

### 注意

1. 日志过大实施方案
```js
use admin  //切换到admin数据库
db.runCommand({logRotate:1})

```


## mysql

### [download](https://dev.mysql.com/downloads/mysql/5.7.html#downloads)

### 安装步骤

1. #### 删除mariadb
    
    1. rpm    
        
        rpm -qa | grep mariadb
        rpm -e -nodeps pakage
    
    2. yum
        
        yum list installed | grep mariadb

        yum remove mariadb*


2. #### 添加用户组
    
    1. 检查mysql用户组和用户是否存在
        
        cat /etc/group | grep mysql
        
        cat /etc/passwd | grep mysql
    
    2. 创建（1中检测）
        
        1. 添加组
        
            groupadd mysql
        
        2. 添加用户到mysql组中
            
            1. 未添加用户
                
                useradd -g mysql mysql
    
            2. 已经添加用户
                
                usermod -g mysql mysql

            3.从某组踢出某用户
                
                grep <groupname> /etc/gshadow
                gpasswd -d <username> <groupname>
                grep <groupname> /etc/gshadow

        3. 设置用户密码
            
            passwd mysql
    
    3. 添加配置环境
        
        vi /etc/profile

        export PATH=$PATH:/usr/local/mysql/bin

        source /etc/profile

    3. 初始化数据库
            
        mkdir /usr/local/mysql/data

        chown mysql:mysql data

        mysql_install_db  --user=mysql --basedir=/usr/local/mysql/ --datadir=/usr/local/mysql/data/
    
    4. 添加启动服务
    
        cp ./support-files/mysql.server /etc/init.d/mysqld


    5. 配置文件
        
        1. 编辑my.cnf
            
            vi /usr/local/mysql/my.cnf
        
        2. 设置访问权限
            
            chmod 777 my.cnf

    6. 查看初始化密码

        cat /root/.mysql_secret  

        set PASSWORD = PASSWORD('jiuguai');

        flush privileges;