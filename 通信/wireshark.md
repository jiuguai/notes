> [官网](http://www.wireshark.org/)
> [书籍推见](http://www.wiresharkbook.com/)
> [维基](http://wiki.wireshark.org/)

+ 显示过滤器语法
    + 比较
        + \> < == != >= <=
    + 逻辑操作符
        + and or xor(有且仅有一个) not
    + IP
        + ip.addr ip.src ip.dst
    + 端口过滤
        + tcp.port tcp.srcport tcp.dstport tcp.flag.syn tcp.flag.ack
    + 协议过滤
        + arp ip icmp udp tcp bootp dns



+ BPF 语法
    + type
        + host, net, port
    + Dir
        + src, dst
    + Proto
        + ehter, ip, tcp, udp, http, ftp
    + 逻辑运算
        + &&
        + ||
        + ！

```bpf
src host 192.168.1.1 && dst port 80
host 192.168.1.1 || host 192.168.1.2
!broadcast
```

