

## 初始化环境
1. 更新本地源
    yum install epel-release --downloadonly --downloaddir=/opt/uibot_repo/epel-release



## 制作本地源

1. 制作yum-utiles
    yum install yum-utils --downloadonly --downloaddir=/opt/uibot_repo/yum-utils-repo

2. 制作mysql本地库

    wget https://dev.mysql.com/get/mysql80-community-release-el7-3.noarch.rpm


    yum localinstall -y mysql80-community-release-el7-3.noarch.rpm


    yum install mysql-community-server --downloadonly --downloaddir=/opt/uibot_repo/mysql57-repo

3. mongodb

    vi /etc/yum.repos.d/mongodb-org-4.2.repo

    ```python
        [mongodb-org-4.2]
        name=MongoDB Repository
        baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.2/x86_64/
        gpgcheck=1
        enabled=1
        gpgkey=https://www.mongodb.org/static/pgp/server-4.2.asc


    ```

    yum install  mongodb-org  --downloadonly --downloaddir=/opt/uibot_repo/mongodb4.2-repo



+ docker

    yum install -y docker-ce docker-ce-cli containerd.io --downloadonly --downloaddir=/opt/uibot_repo/docker-repo







    systemctl start docker
    systemctl enable docker
