#coding=utf-8
import MySQLdb

conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='123456',
        db ='teset',
        )
cur = conn.cursor()

sqli="insert into student values(%s,%s,%s,%s)"
cur.executemany(sqli,[('3','Tom','1 year 1 class','6'),('3','Jack','2 year 1 class','7'),('3','Yaheng','2 year 2 class','7')])

cur.close()
conn.commit()
conn.close()
