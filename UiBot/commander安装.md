
[TOC]


### 镜像下载
[CentOS-7.6 下载地址](http://mirrors.aliyun.com/centos/7/isos/x86_64)

### 更新源

1. 先执行
 
    yum install sl -y

2. 如果下载未成功
   
    yum install epel-release -y

    重复1步骤

2. 如果步骤2未成功
    1. 找个目录下载
        wget wget http://mirrors.aliyun.com/repo/Centos-7.repo
    
    2. 备份之前的源
        mv /etc/yum/repos.d/CentOS-Base.repo /etc/yum/repos.d/CentOS-Base.repo.bak
    
    3. 更新源
        cp Centos-7.repo /etc/yum/repos.d/CentOS-Base.repo
    
    4. 使源生效
       
        yum clean all

        yum makecache


### [开放端口](https://www.cnblogs.com/Treelight/p/11101517.html)
```python
    firewall-cmd --zone=public --add-port=3306/tcp --permanent
    firewall-cmd --zone=public --add-port=80/tcp --permanent
    firewall-cmd --zone=public --add-port=27017/tcp --permanent
    firewall-cmd --zone=public --add-port=6379/tcp --permanent
    firewall-cmd --reload

```

### 如果IP地址 不是固定

```python
    resolv.conf  # 域名生效需要修改
        nameserver 8.8.8.8
        nameserver 114.114.114.114

    systemctl restart NetworkManager

    cd /etc/sysconfig/network-scripts
    ifconfig | grep -P "flags|inet" 找到ens
    vi cfg-ens*
        BOOTPROTO="static"
        IPADDR=""  # 根据环境填
        NETMASK="" # 根据情况填
        ONBOOT="yes"

    systemctl restart network
```

### 安装MySQL

+ 源安装
    - 下载mysql 源
      
        wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm
    
    - 解析源
      
        rpm -Uvh mysql80-community-release-el7-3.noarch.rpm
        或者 yum localinstall mysql80-community-release-el7-3.noarch.rpm

    - 查看mysql默认版本选择
      
        yum repolist all | grep mysql

    - 版本选择
      
        yum-config-manager --disable mysql80-community
        yum-config-manager --enable mysql57-community
        
        - 如果 显示 无 yum-config-manager
        
            yum install -y yum-utils

    - 安装
      
        yum install mysql-community-server -y

    - 开启服务
      
        systemctl start mysqld.service

    - 服务自启
      
        systemctl enable mysqld.service

    - 查看密码
    
        grep 'temporary password' /var/log/mysqld.log

- 离线安装

    + 直接下载MySQL安装包
      
        wget https://dev.mysql.com/get/Downloads/MySQL-5.7/mysql-5.7.28-1.el7.x86_64.rpm-bundle.tar
    
    + 使用rpm命令安装
    
        tar -xvf ./mysql-5.7.28-1.el7.x86_64.rpm-bundle.tar
        rpm -ivh mysql-community-server-5.7.28-1.el7.x86_64.rpm


- 初始化密码
  
    + 查看初始密码
    
        grep 'temporary password' /var/log/mysqld.log

        * 倘若没有获取临时密码
            * 删除原来安装过的mysql残留的数据
                rm -rf /var/lib/mysql
* 再启动mysql
                systemctl start mysqld #启动MySQL
        
    + 修改密码
        ALTER USER 'root'@'localhost' IDENTIFIED BY '密码大小写数字符号都要有长度不小于8';
    
    + 修改密码安全级别
      
        SHOW VARIABLES LIKE 'validate_password%';
    
        set global validate_password_policy=LOW;
    
    + 初始化库
        source ~/mysql/m.sql
        
        /root/temp/normal/uibot_commander.sql

+ 配置文件

```bash
        datadir=/var/lib/mysql
        socket=/var/lib/mysql/mysql.sock
        # Disabling symbolic-links is recommended to prevent assorted security risks
        symbolic-links=0
        log-error=/var/log/mysqld.log
        pid-file=/var/run/mysqld/mysqld.pid
        default-time-zone = '+8:00'
        max_connections = 3000

        # [cpu]*2
        innodb_thread_concurrency = 2

        log-bin=mysql-bin
        server-id = 1000
        expire-logs-days=2
```

### Mongo DB

#### 安装   

+ yum安装    
        
  
        vi /etc/yum.repos.d/mongodb-org-4.2.repo

```python
    [mongodb-org-4.2]
    name=MongoDB Repository
    baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.2/x86_64/
    gpgcheck=1
    enabled=1
    gpgkey=https://www.mongodb.org/static/pgp/server-4.2.asc


```
        yum install -y mongodb-org

#### tgz 安装

##### wget https://fastdl.mongodb.org/linux/mongodb-linux-s390x-rhel72-4.2.6.tgz

##### tar -zxvf mongodb-linux-s390x-rhel72-4.2.6.tgz

##### mv ./mongodb-linux-s390x-rhel72-4.2.6 /usr/local/mongodb

##### cd /usr/local/mongodb && mkdir log conf data script

##### vi 27017-mongodb.conf

```python

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

##### vi script/mongod  (作为参考)

```bash
#!/bin/sh
#
# Simple mongodb init.d script conceived to work on Linux systems
# as it does use of the /proc filesystem.
#chkconfig: 2345 80 90
#description:auto_run
MONGODBPORT=27017
EXEC=/usr/local/mongodb/bin/mongod
PIDFILE=/usr/local/mongodb/pid/mongodb-${MONGODBPORT}.pid
CONF="/usr/local/mongodb/${MONGODBPORT}-mongodb.conf"
OPTIONS="--config $CONF" 
case "$1" in
    start)
                echo "Starting mongodb server..."
        $EXEC $OPTIONS
        ;;  
    stop)
        if [ ! -f $PIDFILE ]
        then
                echo "$PIDFILE does not exist, process is not running"
else
                PID=$(cat $PIDFILE)
                echo "Stopping ..."
                $CLIEXEC -p $MONGODBPORT shutdown
                while [ -x /proc/${PID} ]
                do
                    echo "Waiting for mongodb to shutdown ..."

```
##### mv /usr/local/mongodb/script/mongod /etc/init.d

##### chkconfig mongod on


#### 配置

+ 启动服务

    systemctl start mongod
    systemctl enable mongod
    


+ 配置数据库
  
    use admin
    db.createUser({user:"uibot", pwd:"123456", roles:["dbAdmin"]})


### Redis 安装

+ yum isntall -y redis

+ 可选配置

        1）vi /etc/sysctl.conf
         
        2）内容添加vm.overcommit_memory = 1
        
        3）使生效sysctl -p 

+ 参考日志

```python
dir work_dir
dbfilename path

rdbcompression yes
rdbchecksum yes  # 检验

auto-aof-rewrite-min-size size
auto-aof-rewrite-percentage percentage

save 900 10
appendonly yes
appendfsync always|everysec|no
appendfilename appendonly-port.aof

daemonize yes
bind 0.0.0.0
port 6379

databases 16

# 日志
loglevel debug|verbose|notice|warning
logfile port.log


maxclients 0 # 0表示无限制

timeout 300  # 闲置时间关闭连接

include /path/server-port.conf # 导入公共配置文件




```

### 安装docker

+ 安装依赖  

    yum install -y yum-utils device-mapper-persistent-data lvm2


+ 安装源

    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

+ 安装docker
  
    yum install -y docker-ce docker-ce-cli containerd.io

+ 开启服务
  
    systemctl start docker

    systemctl enable docker


+ 安装docker-compose
    curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
    
    chmod +x docker-compose




