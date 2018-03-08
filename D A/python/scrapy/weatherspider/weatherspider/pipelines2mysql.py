import MySQLdb  
import os.path  
  
class WeatherPipeline(object):  
    def process_item(self,item,spider):  
        city_date=item['citydate']  
        #week=item['week']  
        img=os.path.basename(item['img'])  
        temperature=item['temperature']  
        weather=item['weather']  
        wind=item['wind']  
  
        conn=MySQLdb.connect(  
            host='localhost',  
            port=3306,  
            user='root',  
            passwd='123456',  
            db='test',  
            charset='utf8'  
            )  
        cur=conn.cursor()  
        cur.execute("insert into tianqispider(city_date,img,temperature,weather,wind) values (%s,%s,%s,%s,%s)",(city_date,img,temperature,weather,wind))  
        cur.close()  
        conn.commit()  
        conn.close()  
          
        return item  
