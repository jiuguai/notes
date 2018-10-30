
>[官方文档](https://doc.scrapy.org/en/latest/intro/overview.html)

>[中文文档](https://scrapy-chs.readthedocs.io/zh_CN/1.0/intro/tutorial.html)

>[测试](>http://quotes.toscrape.com/)



### 安装

+ **windows 环境**
    1. wheel:pip install wheel
    2. lxml:pip install lxml
    3. pyOpenssl :pip install wheel
    4. [Twisted](https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted): 
点击链接下载 wheel文件本地安装
    5. [Pywin32](https://sourceforge.net/projects/pywin32/files/pywin32/)
点击链接下载
    6. scapy：pip3 install scapy

+ **linux 环境**

    1. unbuntu:sudo apt-get install build-essential python3-dev libssl-dev libffi-dev libxml2 libxml2-dev libxslt1-dev zlib1g-dev
    2. scapy：pip3 install scapy

+ **Mac OS**
    1. xcode-select --install
    2. pip3 install scrapy

---

### 搭建项目
#### 普通项目
1. **创建项目**
    + scrapy startproject [项目名称]
2. **创建一个爬虫**
    + scrapy genspider [mydomain] "qiushibaike.com"
3. **运行爬虫**
    + scrapy crawl spider_name
4. **项目目录** 

#### CrawlSpider项目
1. **创建项目**
    + scrapy startproject [项目名称]
2. **创建一个爬虫**
    + scrapy genspider -t crawl [mydomain] "qiushibaike.com"
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
+ 数据处理
    + linkextractors
        + LinkExtractor
    + Rule
    + scrapy.exporters
        + JsonLinesItemExporter
        + JsonItemExporter
        + CsvItemExporter
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





