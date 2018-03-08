# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import time
class DoubanmoviePipeline(object):
    def process_item(self, item, spider):
        today=time.strftime('%Y-%m-%d',time.localtime())
        fileName=today+'.txt'
        with open(fileName,'a') as fp:
            
            fp.write(item['rank'].strip()+'\t')  
            fp.write(item['title'].encode('utf-8').strip()+'\t')
            fp.write(item['link'].strip()+'\t')  
            fp.write(item['star'].encode('utf-8').strip()+'\t')
            fp.write(item['rate'].strip()+'\t')
            fp.write(item['quote'].encode('utf-8').strip()+'\t\n')
            time.sleep(1)
        return item
