# -*- coding: utf-8 -*-

import scrapy


class GetProxyItem(scrapy.Item): 
    ip = scrapy.Field()
    port = scrapy.Field()
    position = scrapy.Field()
    location = scrapy.Field()
    type = scrapy.Field()
    speed = scrapy.Field()
    last_check_time = scrapy.Field()
