
+ 启动黑屏解决方案
    + 进入 引导界面 按e键
    + 加入 nouveau.modeset=0
    
    + 长久解决方案
        + 进入 kaili后
        + cd /etc/modprobe.d
            + 写入 blacklist nouveau
        + vi /etc/default/grub
            + rdblacklist=nouveau nouveau.modeset=0
        + sudo update-initramfs -u