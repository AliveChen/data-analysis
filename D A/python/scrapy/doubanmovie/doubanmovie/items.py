# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmovieItem(scrapy.Item):
    

    rank = scrapy.Field()#电影排名
    title = scrapy.Field()#标题--电影名
    link = scrapy.Field()#详情链接
    star = scrapy.Field()#电影评分
    rate = scrapy.Field()#评价人数
    quote = scrapy.Field() #名句
    # define the fields for your item here like:
    # name = scrapy.Field()
