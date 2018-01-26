# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html


#宝猪！！！看这里！！！
#这个地方记得加一个moviename的选项


import scrapy
import time
ISOTIMEFORMAT='%Y-%m-%d %X'

class CollectItem(scrapy.Item):
    news_id=scrapy.Field()
    language=scrapy.Field()
    request_url=scrapy.Field()
    title=scrapy.Field()
    classification=scrapy.Field()
    body=scrapy.Field()
    cole_time=scrapy.Field()
    pub_time=scrapy.Field()
    img_src=scrapy.Field()
    moviename=scrapy.Field()#《《《《《《就是这个！