# redsi 安装
wget http://download.redis.io/releases/redis-5.0.7.tar.gz

    tar -zxvf redis-5.0.7.tar.gz
    make 
    cd src && make install --PREFIX=/usr/local/redis

    cd /usr/local/redis/etc
    vi /usr/local/redis/etc/6379.conf

        bind 0.0.0.0
        dir "/usr/local/redis/rdb/"
        logfile "/usr/local/redis/log/redis_log.log"
        pidfile /var/run/redis_6378.pid
        protected-mode no
     

    ps -aux | grep redis
    
    修改自启动脚本
    vi [解压目录]/utils/redis_init_scripts
    cp  /utisl/redis_init_scripts /etc/init.d/redis


# 端口映射
下载 rinetd
vi /etc/rinetd.conf
0.0.0.0 6379 127.0.0.1 6378 # 服务器在本地

rinetd 启动
netstat -lntup|grep6379

开机启动
    echo rinetd >>/etc/rc.local
    
    chmod 755 /etc/init.d/redis #设置文件redis的权限，让Linux可以执行
    chkconfig redis on    #开启服务自启动
    chkconfig --list      #查看所有注册的脚本文件
    service redis start   #启动
    service redis stop    #关闭redis








