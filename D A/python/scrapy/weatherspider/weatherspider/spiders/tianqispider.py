#coding=utf-8
import scrapy
import sys
sys.path.append('C:\\Users\\Administrator\\weatherspider')
from weatherspider.items import WeatherspiderItem

class weatherSpider(scrapy.Spider):
    name='tianqispider'
    allowed_domains=['tianqi.com']
    citys=['wuhan','hangzhou']
    start_urls=[]

    for city in citys:
        start_urls.append('http://'+city+'.tianqi.com')
    print start_urls

    def parse(self,response):
        subSelector=response.xpath('//div[@class="tqshow1"]')
        items=[]
        for sub in subSelector:
            item=WeatherspiderItem()
            cityDates=''
            for cityDate in sub.xpath('.//h3//text()').extract():  
                cityDates+=cityDate
            
            item['citydate']=cityDates
            item['week']=sub.xpath('./p//text()').extract()[0]  
            item['img']=sub.xpath('./ul/li[1]/img/@src').extract()[0]  
            temps=''  
            for temp in sub.xpath('.//li[2]//text()').extract():  
                temps+=temp
            
            item['temperature']=temps
            item['weather']=sub.xpath('.//li[3]//text()').extract()[0]  
            item['wind']=sub.xpath('.//li[4]//text()').extract()[0]  
            items.append(item)  
        return items
    
    
