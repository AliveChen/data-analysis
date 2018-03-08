# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time  
  
class GetProxyPipeline(object):  
    def process_item(self,item,spider):  
        today= time.strftime('%Y-%m-%d',time.localtime())  
        fileName='proxy'+today+'.txt'  
        with open(fileName,'a') as fp:  
            fp.write('记录'+item['id'].strip()+':'+'\t')  
            fp.write(item['ip'].strip()+'\t')  
            fp.write(item['port'].strip()+'\t')  
            fp.write(item['protocol'].strip()+'\t')  
            fp.write(item['type'].encode('utf-8').strip()+'\t')  
            fp.write(item['location'].encode('utf-8').strip()+'\t')  
            fp.write(item['source'].strip()+'\t\n')  
              
        return item  
