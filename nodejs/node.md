**数据转换**

    util.inspect()  //json转换为字符串
    querystring.parse(url.parse(req.url)) //将请求的查询字符串转为json对象
    


1.模块
    
    1)http
        方法:
            createServer(cs).listen(6666)
                cs:为处理函数
                    cs = function(req,res){     //req 请求信息  res 响应对象
                        res.writeHead('200',{'content-type':'text/html;charset=utf-8'})   //配置响应头
                        res.write('hellow world!')
                        res.end()               //响应结束
                    }
                6666:为端口号 

    2)fs        //文件模块
        同步:
            const fs = require('fs')
            file = 'test.txt'
            data = fs.readFileSync(file)    //同步读取
            console.log(data.toString())
        异步:
            const fs = require('fs')
            file = 'test.txt'
            console.log('read start!')
            fs.readFile(file,function(err,data){
                console.log(data.toString())
            })
            console.log('read end!')

     3)event 
            const events = require('events')
            evt  = new events.EventEmitter()
            function eventHandler(){
                console.log('aaa')
                console.log('www')
            }
            evt.on('eventName',eventHandler)
            evt.emit('eventName')

    4)url   //url解析
        url.parse()

    5)util //常用工具
        util.inspect()      //json转换为字符串
        util.isArray()
        util.isBoolean()
        util.isDate()
        util.isFunction()
        util.isObject()
        util.isRegExp()

    6)os
        os.tmpdir()
        os.hostname()
        os.type()
        os.platform()
        os.loadavg()
        os.totalmem()
        os.freemem()
        os.cpus()
        os.networkInterfaces()

    7)path
        path.dirname()
        path.basename()
        path.extname()
        path.parse()
        path.format()

    8)dns
        const dns = require('dns')
        domain = 'www.baidu.com'
        dns.lookup(domain,(err,ip,family)=>{
            dns.reverse(ip,(err,hostname)=>{
                if(err){
                    console.log(err.stack);
                }
                console.log(hostname);
            })
        })

    9)net
        const net = require('net')
        chat = net.createServer()
        chat.on('connection',(c)=>{
            c.write('hello world')
            c.on('data',(data)=>{
                console.log(data.toString());
            }) 
        })
        chat.listen(8900)
        console.log('tellnet server start');

    4)自建模块
        function show(){
            this.name = 'zero'
            this.age = 18
            this.say = function(){
                console.log('my name is '+this.name)
            }
        }
        module.exports=new show()

2.全局对象

    console.log('__filename:' + __filename);
    console.log('__dirname :' + __dirname);

    setInterval(fn,speed);
    setTimeout(fn,timeout)

    console.log('1111');
    console.info('2222');
    console.warn('3333');
    console.error('444');    
    
    //耗时
    console.time('x')
    for (i=0;i<1000000;i++){}
    console.timeEnd('x')

    str = process.version
    str = process.argv
    str = process.pid
    str = process.config
    str = process.title
    str = process.platform
    str = process.cwd()
    str = process.memoryUsage()
    str = process.uptime()
    str = process.env
    str = process.hrtime()
    process.stdout.write('abc\n')
    console.log(str);

    process.stdin.on('readable',function(){
        str = process.stdin.read()
        if(str!==null){
            process.stdout.write('data:'+str)
        }
    })

3.文件系统
    
    1)读文件内容
        异步
            data = fs.readFile(file,(err,data)=>{})
        同步
            data = fs.readFileSync(filepath)

    2)写文件内容
        fs.writeFile(file,str)

    3)删除文件
        fs.unlink(file)
        fs.rmdir(dir)

    4)创建文件
        fs.mkdir(dir)

4.get post 请求
    
    post请求
        req.on('data',(data)=>{})
        req.on('end',()=>{})



4.安装
    
    命令:
        npm:        //-g 参数为全局
            npm root                  //查看本地根目录
            npm root  -g              //查看全局根目录
            npm intall msyql
            npm uninstall mysql
            npm update mysql

