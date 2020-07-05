# redsi 安装
wget http://download.redis.io/releases/redis-5.0.7.tar.gz

    tar -zxvf redis-5.0.7.tar.gz
    make 
    cd src && make install --PREFIX=/usr/local/redis
    
        1）vi /etc/sysctl.conf
 
        2）内容添加vm.overcommit_memory = 1

        3）使生效sysctl -p 


    cd /usr/local/redis/etc
    vi /usr/local/redis/etc/6379.conf

        bind 0.0.0.0
        dir "/usr/local/redis/rdb/"
        logfile "/usr/local/redis/log/redis_log.log"
        pidfile /var/run/redis_6378.pid
        protected-mode no
        save 900 10
     

    ps -aux | grep redis
    
    修改自启动脚本
    vi [解压目录]/utils/redis_init_scripts
    cp  /utisl/redis_init_scripts /etc/init.d/redis
    chkconfig redisd on

# 端口映射
下载 rinetd
vi /etc/rinetd.conf
0.0.0.0 6379 127.0.0.1 6378 # 服务器在本地

rinetd 启动
netstat -lntup|grep6379

开机启动
    echo rinetd >>/etc/rc.local
    
    chmod 755 /etc/init.d/redisd #设置文件redisd的权限，让Linux可以执行
    chkconfig redisd on    #开启服务自启动
    chkconfig --list      #查看所有注册的脚本文件
    service redisd start   #启动
    service redisd stop    #关闭redisd








