# zhihu_spider
使用scrapy框架的爬虫用来爬取知乎网上面的问题、答案、点赞数等相关信息,将爬取到的数据保存到Mysql中； 在知乎网站中搜索自定义内容，并且将回答里面的图片保存到本地




所需第三方库：
scrapy==1.5.1
mysqlclient==1.3.13
Pillow==5.2.0
selenium==3.14.0



使用方法：
在run.py里面配置需要进行的spider，有zhihu,image_spider两个可以选择。
在setting里面将需要使用的pipeline配置进去，其中mysqltwistedpipeline可以将知乎爬取的数据保存到mysql数据库中，
zhihu_image_spider_pipeline可以将自己搜索出来的知乎回答里面的图片进行保存。


需要修改的地方：
setting里面数据库的地址
知乎用户名和密码
图片的保存路径

