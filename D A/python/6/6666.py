#coding=utf-8
import pandas as pd
import numpy as np
import csv
import json
'''
df=pd.read_table('ch06/ex1.csv')
print df
df2=pd.read_csv('ch06/ex2.csv',header=None)
print df2
df3=pd.read_csv('ch06/ex2.csv',names=['a','b','c','d','message'])
print df3
names=['a','b','c','d','message']
df4=pd.read_csv('ch06/ex2.csv',names=names,index_col='message')
print df4
df5=pd.read_csv('ch06/csv_mindex.csv',index_col=['key1','key2'])
print df5
df6=list(open('ch06/ex3.txt'))
print df6
df7=pd.read_table('ch06/ex3.txt',sep='\s+')
print df7
df8=pd.read_csv('ch06/ex4.csv',skiprows=[0,2,3])
print df8
#166page
df9=pd.read_csv('ch06/ex6.csv',nrows=5)
print df9
df10=pd.read_csv('ch06/ex6.csv',chunksize=1000)
print df10

data=pd.read_csv('ch06/ex5.csv')
print data
data.to_csv('ch06/out728.csv')

f=open('ch06/ex7.csv')
reader=csv.reader(f)
for line in reader:
    print line
 
lines=list(csv.reader(open('ch06/ex7.csv')))
header,values=lines[0],lines[1:]
data_dict={h:v for h,v in zip(header,zip(*values))}
print data_dict 
data2=pd.ExcelFile('单边.xlsx')
print data2

import json
obj={'name':'wes','place_lived':['united states','spain','germany'],'pet':'null','siblings':[{'name':'scott','age':25,'pet':'zuko'},{'name':'katie','age':33,'pet':'cisco'}]}
result=json.load(obj)
print result

data2=pd.ExcelFile('单边.xlsx')
print data2
#table=data2.parse('sheet1')

import MySQLdb
conn=MySQLdb.connect(host='localhost',user='root',passwd='123456')
cur=conn.cursor()
#cur.execute('create database if not exists test')
conn.select_db('test')
#cur.execute('create table test1(id int,info varchar(20))')
ttt=[1,'hello world']
#cur.execute('insert into test1 values(%s,%s)',ttt)
#cur.execute('update test1 set info="hello word!!" where id=1')
a=cur.execute('select * from test1')
print a
aa=cur.fetchmany(a)
for every_test1_728 in aa:
    print every_test1_728
conn.commit()
cur.close()
conn.close()
'''
#数据规整化：清理，转换，合并，重塑
'''
df1=pd.DataFrame({'key':['b','b','a','c','a','a','b'],'data1':range(7)})
df2=pd.DataFrame({'key':['a','b','d'],'data2':range(3)})
print df1
print df2
df3=pd.merge(df1,df2)
print df3

left=pd.DataFrame({'key1':['foo','foo','bar'],
                   'key2':['one','two','one'],
                   'lval':[1,2,3,]})
right=pd.DataFrame({'key1':['foo','foo','bar','bar'],
                   'key2':['one','one','two','two'],
                   'rval':[4,5,6,7]})
df4=pd.merge(left,right,on=['key1','key2'],how='outer')
print df4
'''
#正则表达式
'''
import re
text='f00   bar\t baz \tqux'
#用\s+描述数量不定的空白符换行符制表符
df5=re.split('\s+',text)
print df5
'''
#第七章。usda食品数据库
import json
#db=json.load(open('ch07/foods-2011-10-03.json '))
#a=len(db)
#print a
#print db[0].keys()

df=pd.DataFrame({'key1':['a','a','b','b','a'],
                 'key2':['one','two','one','two','one'],
                 'data1':np.random.randn(5),
                 'data2':np.random.randn(5)})
print df
grouped=df['data1'].groupby(df['key1'])
print grouped.mean()









