

### 打开 jupyter notebook
```cmd
@echo off
CD /d E:\dataparse\Python_DATA_PARSE
ipython notebook
```

### 执行 某段代码
```
python3 E:/easy_script/解决声音消失.py
```

### netsh

```shell
netsh dump > net.info
netsh int ip set address name="本地连接" source=static addr=192.168.0.101 mask=255.255.255.0
netsh int ip set address name="本地连接" source=dhcp
netsh int ip set address name="本地连接" gateway=192.168.0.1 gwmetric=1
netsh interface ip set dns name="本地连接" source=static addr=114.114.114.114
netsh interface ip add dns name="本地连接" source=static addr=8.8.8.8 index=2


# 解决修复网络故障
netsh winsock reset # 解决网络冲突、病毒原因造成的错误问题

netsh int ip reset c:\resetlog.txt # 重新安装TCP/IP协议

# 操作防火墙
netsh firewall set opmode mode=disable # enable

# 获取密码
netsh wlan show profiles # 显示所有保存的网络
netsh wlan show profile name="ssid" key=clear
```

### ipconfig
```shell
ipconfig /all
ipconfig /release
ipconfig /renew
ipconfig /flushdns
```

