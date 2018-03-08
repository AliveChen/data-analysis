#coding=utf-8
import scrapy
import sys
sys.path.append("C:\\Users\\Administrator\\collectips")

from collectips.items import GetProxyItem 

'''
class XiciSpider(scrapy.Spider):
    name = "xici"
    allowed_domains = ["xicidaili.com"]
    start_urls = (
        'http://www.xicidaili.com/',
    )

    def start_requests(self):
        res = []
        for i in range(1, 2):
            url = 'http://www.xicidaili.com/nn/%d'%i
            req = scrapy.Request(url)
            # 存储所有对应地址的请求
            res.append(req)
        return res

    def parse(self, response):
        table = response.xpath('//table[@id="ip_list"]')[0]
        trs = table.xpath('//tr')[1:]   #去掉标题行
        items = []
        for tr in trs:
            pre_item = DailiIpsItem()
            pre_item['ip'] = tr.xpath('td[2]/text()').extract()[0]
            pre_item['port'] = tr.xpath('td[3]/text()').extract()[0]
            pre_item['position'] = tr.xpath('string(td[4])').extract()[0].strip()
            pre_item['type'] = tr.xpath('td[6]/text()').extract()[0]
            pre_item['speed'] = tr.xpath('td[7]/div/@title').re('\d+\.\d*')[0]
            pre_item['last_check_time'] = tr.xpath('td[10]/text()').extract()[0]
            items.append(pre_item)
        return items
'''

class XiciDailiSpider(scrapy.Spider):  
    name='xici'  
    allowed_domains=['xicidaili.com']  
    wds=['nn','nt','wn','wt']  
    pages=20  
    start_urls=[]  
    count=0  
    for type in wds:  
        for i in range(1,pages+1):  
            start_urls.append('http://www.xicidaili.com/'+type+'/'+str(i))
            
      
    def parse(self,response):  
        subSelector=response.xpath('//tr[@class=""]|//tr[@class="odd"]')  
        items=[]  
        for sub in subSelector:  
            item=GetProxyItem()  
            item['ip']=sub.xpath('.//td[2]/text()').extract()[0]  
            item['port']=sub.xpath('.//td[3]/text()').extract()[0]  
            item['type']=sub.xpath('.//td[5]/text()').extract()[0]  
            if sub.xpath('.//td[4]/a/text()'):  
                item['location']=sub.xpath('//td[4]/a/text()').extract()[0]  
            else:  
                item['location']=sub.xpath('.//td[4]/text()').extract()[0]  
            #item['protocol']=sub.xpath('.//td[6]/text()').extract()[0]  
          
            item['speed'] = sub.xpath('td[7]/div/@title').re('\d+\.\d*')[0]
            item['last_check_time'] = sub.xpath('td[10]/text()').extract()[0]
            #self.count+=1  
            #item['id']=str(self.count)  
            items.append(item)  
        return items              
