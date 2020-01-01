
+ 如果yum源中没有 mysql
    1. home 目录下
        mkdir temp
    2. 下载更新repo
        wget https://dev.mysql.com/get/mysql57-community-release-el7-9.noarch.rpm
        rpm -ivh mysql57-community-release-el7-9.noarch.rpm
+ 安装mysql
    1. 安装
        yum install mysql-server
    2. 启动
        systemctl start mysqld

    3. 第一次登陆mysql
    
        1. 获取安装时的临时密码
            + grep 'temporary password' /var/log/mysqld.log

                * 倘若没有获取临时密码
                    * 删除原来安装过的mysql残留的数据
                        rm -rf /var/lib/mysql

                    * 再启动mysql
                        systemctl start mysqld #启动MySQL       
        
        2. 登陆
            + mysql -uroot -p 临时密码
                + 若登录不了
                    +  vim /etc/my.cnf
                        在任意行 输入  skip-grant-tables

        3. 修改密码
            + set password=password("xxxxx")
                + 密码修改规则太复杂
                    + 查看密码相关配置 
                        + SHOW VARIABLES LIKE 'validate_password%';
                    # 设置密码规则 案例
                        * set global validate_password_policy=LOW;
                        * set validate_password_length = 6
+ MySql 设置(两种方法)
    + 访问设置
        * 修改
            update user set host = '%' where user = 'root';
        * 添加
            1. 切换库
                use mysql;
            2. 授予权限
                grant all privileges  on *.* to root@'%' identified by "password";
            3. 刷新
                flush privileges;
    + 编码设置
        * vi /etc/my.cnf
            [mysqld] character_set_server=utf8mb4
    
    + 服务启动
        1. 开启
            systemctl restart mysqld 
        2. 关闭
            systemctl stop mysqld 
        3. 重启
            systemctl restart mysqld 
        4. 查看状态
            systemctl status mysqld 
        5、设置开机启动
            systemctl enable mysqld 
        6、关闭开机启动
            systemctl disable mysqld 
        
+ 防火墙
    1. 查看
        firewall-cmd --list-all
        firewall-cmd --query-port=3306/tcp
    
    2. 开放端口    
        firewall-cmd --permanent --add-port=3306/tcp
        
    3. 重启防火墙
        service firewalld restart

    4. 再次查看防火墙
        firewall-cmd --query-port=3306/tcp
        firewall-cmd --list-all
    
    5. 关闭
        systemctl stop firewalld.service

    6. 开启
        systemctl stop firewalld.service

    7. 禁止开机启动
        systemctl disable firewalld.service
        
    8. 允许开机启动
        systemctl enable firewalld.service