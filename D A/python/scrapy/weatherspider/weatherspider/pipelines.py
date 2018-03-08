# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html



import time  
import os.path  
from urllib2 import Request
from urllib import urlopen
  
class WeatherPipeline(object):  
    def process_item(self,item,spider):  
        today=time.strftime('%Y-%m-%d',time.localtime())  
        fileName=today+'.txt'     
        with open(fileName,'a') as fp:  
            fp.write((item['citydate'].encode('utf-8')+'\t'))  
            fp.write(item['week'].encode('utf-8')+'\t')
            fp.write(item['img'].encode('utf-8')+'\t')
            

            
           

            imgName=os.path.basename(item['img'])  
            fp.write(imgName+'\t')  
            if os.path.exists(imgName):  
                pass  
            else:  
                with open(imgName,'wb') as fp:  
                    response=urlopen(item['img'])  
                    fp.write(response.read())
                  
            fp.write(item['temperature'].encode('utf-8')+'\t')  
            fp.write(item['weather'].encode('utf-8')+'\t')  
            fp.write(item['wind'].encode('utf-8')+'\t\n')  
            time.sleep(1)  
        return item  
