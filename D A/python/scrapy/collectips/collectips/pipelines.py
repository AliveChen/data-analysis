# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
'''
import MySQLdb
class DailiIpsPipeline(object):
    # 该函数必须返回一个具有数据的dict或者item对象
    def process_item(self, item, spider):
        DBS = spider.settings.get('DBS')
        con = MySQLdb.connect(**DBS)
        # 下面这行代码表示设置MySQL使用的字符集为utf8
        con.set_character_set('utf8')
        cur = con.cursor()
        insert_sql = (
            "insert into proxy (ip, port, position, type, speed, last_check_time) "
            "values (%s,%s,%s,%s,%s,%s);"
        )
        values = (item['ip'], item['port'], item['position'], item['type'], item['speed'], item['last_check_time'])
        # 插入数据库
        try:
            cur.execute(insert_sql, values)
        except Exception, e:
            print "插入失败: ", e
            con.rollback()
        else:
            con.commit()
        cur.close()
        con.close()
        return item




        return item
'''
import time  
  
class GetProxyPipeline(object):  
    def process_item(self,item,spider):  
        today= time.strftime('%Y-%m-%d',time.localtime())  
        fileName='proxy'+today+'.txt'  
        with open(fileName,'a') as fp:  
            #fp.write('记录'+item['id'].strip()+':'+'\t')  
            fp.write(item['ip'].strip()+'\t')  
            fp.write(item['port'].strip()+'\t')  
            fp.write(item['speed'].strip()+'\t')  
            fp.write(item['type'].encode('utf-8').strip()+'\t')  
            fp.write(item['location'].strip()+'\t')  
            fp.write(item['lats_check_time'].strip()+'\t\n')  
              
        return item  
