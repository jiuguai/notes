
>[官方文档](https://doc.scrapy.org/en/latest/intro/overview.html)

>[中文文档](https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html)

>[测试](>http://quotes.toscrape.com/)

>[scrapyd-deploy命令讲解](https://piaosanlang.gitbooks.io/spiders/05day/section5.3.html)

### scrapyd
+ scrapyd
    
+ scrapyd_client
    + Windows
        * 安装curl
        * scrapyd-deploy 文件 不能呗shell直接执行，需要新建scrapy-deploy.bat   
            ```bash

                @echo off
                E:\Python\WorkEnvs\scrapy3\Scripts\python E:\Python\WorkEnvs\scrapy3\Scripts\scrapyd-deploy %*
            ```


### commands
+ settings 
    + scrapy settings --get=DOWNLOADER_MIDDLEWARES_BASE
    + scrapy settings --get=SPIDER_MIDDLEWARES_BASE

### 异步锁
+ twisted
    + from twisted.internet.defer import DeferredLock

### 安装

+ **windows 环境**
    1. wheel:pip install wheel
    2. lxml:pip install lxml
    3. pyOpenssl :pip install wheel
    4. pip3 install pillow(非必须下载图片有用)
    5. [Twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted): 
点击链接下载 wheel文件本地安装
    5. [Pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/)
点击链接下载
    6. scapy：pip3 install scapy

+ **linux 环境**

    1. unbuntu:sudo apt-get install build-essential python3-dev libssl-dev libffi-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev
    2. scapy：pip3 install scapy
        1. ImportError: cannot import name main
        
            ```python

                from pip import __main__
                if __name__ == '__main__':
                    sys.exit(__main__._main())
            ```

+ **Mac OS**
    1. xcode-select --install
    2. pip3 install scrapy

---

### 搭建项目
#### 普通项目
1. **创建项目**
    + scrapy startproject [项目名称]
2. **创建一个爬虫**
    + scrapy genspider [crawle_name] "qiushibaike.com"
3. **运行爬虫**
    + scrapy crawl spider_name
4. **项目目录** 

#### CrawlSpider项目
1. **创建项目**
    + scrapy startproject [项目名称]
2. **创建一个爬虫**
    + scrapy genspider -t crawl [crawler_name] "qiushibaike.com"
3. **运行爬虫**
    + scrapy crawl spider_name

```python
#创建start.py 文件
from scrapy import cmdline
cmdline.execute("scrapy crawl qs".split(' '))
```


### 文件
1. settings.py
    + ROBOTSTXT_OBEY = FALSE  # 取消遵循robots协议
    + DEFAULT_REQUEST_HEADERS = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Language': 'en',
    } # 设置默认请求头
    + ITEM_PIPELINES = {
        'qsbk.pipelines.QsbkPipeline': 300, # 要使用pipeline需要打开设置  300 表示优先级越小优先级越高
    }
    + DOWNLOAD_DELAY = 2
2. pipelines.py
```python
    # 开始
    def open_spider(self,spider):
        print('爬虫开始')
        self.fp = open('duanzi.json','w',encoding="utf-8")

    # 获取过程
    def process_item(self, item, spider):
        item_json = json.dumps(item)
        self.fp.write(item_json+'\n')
        return item
    # 结束
    def close_spider(self,spider):
        print('爬虫结束')
        # 为了举个例子 不过建议放在 __del__ 中
        self.fp.close()
```
3. items.py
    + 定义数据模型 
        > 比字典更有约束性
    + 和字典等价
        


### 模块
+ **数据处理**
    + scrapy.exporters
        + JsonLinesItemExporter
        + JsonItemExporter
        + CsvItemExporter
+ **Crawl 模版** 
    + linkextractors
        + LinkExtractor
```md
FilteringLinkExtractor(allow=(), deny=(), allow_domains=(), deny_domains=(), restrict_xpaths=(),
                 tags=('a', 'area'), attrs=('href',), canonicalize=False,
                 unique=True, process_value=None, deny_extensions=None, restrict_css=(),
                 strip=True)

实例化后：restrict_css -> restrict_xpaths or response.selector
然后按照以下顺序寻找满足条件的urls:
restrict_xpaths  # restrict_css -> restrict_xpaths
targs
attrs
process_value
unique：docs 中子文档 外加canonicalize=false 条件
allow
deny
allow_domains
deny_domains
deny_extensions
unique:docs 合并后
```
    + spiders
        + Rule
        + CrawlSpider
+ **文件下载模块**
    + 安装 pillow 库
        + pip3 install pillow
    + settings(存储目录)
        + IMAGES_STORE = r'F:\images\cars\bmw5'
    + Files Pipeline
        1. 在Item 中定义 file_urls files属性
        2. 文件下载完成之后，会把文件下载的相关信息存放到item 的files中，如：下载路径、url、校验码
        3. 在settings.py 中配置 FILES_STORE,这个配置用来设置问价下载路径
        4. 启动pipeline: 在ITEM_PIPLINES 中设置 'scrapy.pipelines.files.FilesPipeline':100
    + Image Pipeline
        1. 在Item 中定义 image_urls images属性
        2. 文件下载完成之后，会把文件下载的相关信息存放到item 的files中，如：下载路径、url、校验码
        3. 在settings.py 中配置 FILES_STORE,这个配置用来设置问价下载路径
        4. 启动pipeline: 在ITEM_PIPLINES 中设置 'scrapy.pipelines.images.ImagesPipeline':100
    
```python
        # JsonLinesItemExporter 来一条存一条
        from scrapy.exporters import JsonLinesItemExporter
        class QsbkPipeline(object):
            def open_spider(self,spider):
                self.fp = open('qs.json','wb')
                self.exporter = JsonLinesItemExporter(self.fp,ensure_ascii=False,encoding="utf-8")
            def process_item(self,item,spider):
                self.exporter.export_item(item)
                return item
            def close_spider(self,spider):
                self.fp.close()
                print('爬虫结束')

        # JsonItemExporter 最后一次提交
        from scrapy.exporters import JsonItemExporter
        class QsbkPipeline(object):
            def open_spider(self,spider):
                self.fp = open('qs.json','wb')
                self.exporter = JsonItemExporter(self.fp,ensure_ascii=False)
                self.exporter.start_exporting()
                
            def process_item(self,item,spider):
                self.exporter.export_item(item)
                return item
            def close_spider(self,spider):
                self.exporter.finish_exporting()
                self.fp.close()
                print('爬虫结束')
```







