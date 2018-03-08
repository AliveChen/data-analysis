# -*- coding: utf-8 -*-
import scrapy
import sys
sys.path.append('C:\\Users\\Administrator\\doubanmovie\\doubanmovie')

from items import DoubanmovieItem
class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["movie.douban.com"]
    page=range(0,50,25)
    start_urls=[]
    for i in page:
        start_urls.append('https://movie.douban.com/top250?start=%s&filter='%i)
        print start_urls

    def parse(self, response):
        items=[]
        subselector=response.xpath('//ol[@class="grid_view"]/li')
        #print subselector
        for info in subselector:

            item = DoubanmovieItem()
            item['rank'] = info.xpath('.//div[@class="pic"]/em/text()').extract()[0]
            item['title'] = info.xpath('.//div[@class="pic"]/a/img/@alt').extract()[0]
            item['link'] = info.xpath('.//div[@class="pic"]/a/@href').extract()[0]
            item['star'] = info.xpath('.//div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            item['rate'] = info.xpath('.//div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()').extract()[0]
            item['quote'] = info.xpath('.//div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span/text()').extract()[0]
            items.append(item)

            #return items
        return items


