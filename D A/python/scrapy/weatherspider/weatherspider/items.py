# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherspiderItem(scrapy.Item):
    citydate=scrapy.Field()
    week=scrapy.Field()
    img=scrapy.Field()
    temperature=scrapy.Field()
    weather=scrapy.Field()
    wind=scrapy.Field()
    
   
