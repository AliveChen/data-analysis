import MySQLdb  
import os.path  
  
class GetProxyPipeline(object):  
    def process_item(self,item,spider):  
        number=item['id']  
        ip=item['ip']  
        port=item['port']  
        protocol=item['protocol']  
        Type=item['type']
        location=iten['location']
        source=item['source']
        
  
        conn=MySQLdb.connect(  
            host='localhost',  
            port=3306,  
            user='root',  
            passwd='123456',  
            db='test',  
            charset='utf8'  
            )  
        cur=conn.cursor()  
        cur.execute("insert into proxy360(number,ip,port,Type,protocol,location,source) values (%s,%s,%s,%s,%s,%s,%s)",(number,ip,port,Type,protocol,location,source))  
        cur.close()  
        conn.commit()  
        conn.close()  
          
        return item  
