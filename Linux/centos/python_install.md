[python 各个版本](https://www.python.org/ftp/python)

1. 下载
    1. 云主机下载慢
        1. 先安装 lrzsz
            yum -y install lrzsz

        2. 将下在 Python-3.7.0.tar.xz

    2. https://www.python.org/ftp/python/3.6.5/Python-3.6.5.tar.xz
2. 安装依赖
    + 解决退格键的问题
        yum install readline-devel.*
    + 解决make install 问题
        yum install zlib* openssl*

3. 编译
    cd cd Python-3.6.5
    ./configure --prefix=/usr/local/python3 --enable-optimizations
    make && make install

4. 创建软链接
    ln -s /usr/local/python3/bin/python3 /usr/local/bin/python3
    ln -s /usr/local/python3/bin/pip3 /usr/local/bin/pip3