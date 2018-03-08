import scrapy
import sys
sys.path.append('C:\\Users\\Administrator\\getProxy')
from getProxy.items import GetProxyItem  
  
class Proxy360Spider(scrapy.Spider):  
    name="proxy360Spider"  
    allowed_domains=['proxy360.cn']  
    nations=['Brazil','China','America','Taiwan','Japan','Thailand','Vietnam','bahrein']  
    start_urls=[]  
    count=0  
    for nation in nations:  
        start_urls.append('http://www.proxy360.cn/Region/'+nation)
    print start_urls
  
    def parse(self,response):  
          
        subSelector=response.xpath('//div[@class="proxylistitem" and @name="list_proxy_ip"]')  
        items=[]  
          
        for sub in subSelector:  
            item=GetProxyItem()  
            item['ip']=sub.xpath('.//span[1]/text()').extract()[0]  
            item['port']=sub.xpath('.//span[2]/text()').extract()[0]  
            item['type']=sub.xpath('.//span[3]/text()').extract()[0]  
            item['location']=sub.xpath('.//span[4]/text()').extract()[0]  
            item['protocol']='HTTP'  
            item['source']='proxy360'  
            self.count+=1  
            item['id']=str(self.count)  
            items.append(item)  
  
        return items  
