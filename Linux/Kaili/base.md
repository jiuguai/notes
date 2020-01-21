+. 安装apt-file
apt-get install apt-file    # 用于解决文件依赖
apt-get update      # 同步源的索引
apt-get upgrade     # 安装最新版软件

+. 中文乱码
```bash
apt-get install locales
dpkg-reconfigure locales
    # 选中en_US.UTF-8和zh_CN.UTF-8，确定后，将en_US.UTF-8选为默认。
apt-get install xfonts-intl-chinese
apt-get install ttf-wqy-microhei
rebot

```


+. 安装输入法
```bash
apt-get install fcitx fcitx-pinyin fcitx-module-cloudpinyin fcitx-googlepinyin
apt-get install im-config

```

+. ssh
```bash
dpkg-reconfigure openssh-server

vi /etc/ssh/sshd_config
    ```config 
        PasswordAuthentication yes
        PermitRootLogin yes
    ```
/etc/init.d/ssh restart

```

+. network
    1. 命令行
    ```bash
        ifconfig eth0 192.168.150.131 netmask 255.255.255.0
        route add default gw192.168.150.2
        echo nameserver 8.8.8.8 > /etc/resolv.conf

    ```

    2. 配置域名
        vi /etc/resolv.conf
        ```bash
        domain
        nameserver 10.10.10.10
        nameserver 8.8.8.8

        ```
        /etc/init.d/networking restart

vi /etc/network/interfaces
```bash
auto eth0
iface eh0 inet static
address 192.168.151.131
netmask 255.255.255.0
gateway 192.168.150.2
broadcast 192.168.150.255

```
