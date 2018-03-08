# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy  
  
class GetProxyItem(scrapy.Item):  
    ip=scrapy.Field()  
    port=scrapy.Field()  
    type=scrapy.Field()  
    location=scrapy.Field()  
    protocol=scrapy.Field()  
    source=scrapy.Field()  
    id=scrapy.Field()#用来保存记录条数  
