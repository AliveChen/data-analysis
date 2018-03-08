#coding=utf-8
import pandas as pd
from sklearn.cluster import KMeans

'''
#聚类离散化
datafile='chapter8/demo/data/data.xls'
outputfile='chapter8/out/processed_data.xls'
typelabel ={u'肝气郁结证型系数':'A', u'热毒蕴结证型系数':'B', u'冲任失调证型系数':'C', u'气血两虚证型系数':'D', u'脾胃虚弱证型系数':'E', u'肝肾阴虚证型系数':'F'}
k=4

#读取数据并进行聚类分析
data=pd.read_excel(datafile)
keys=list(typelabel.keys())
result=pd.DataFrame()

if __name__ == '__main__':

    for i in range(len(keys)):
        #调用聚类
        print u'正在进行%s的的聚类'%keys[i]
        kmodel=KMeans(n_clusters=k,n_jobs=1)
        #print keys[i]
        #print [keys[i]]
        #print data[[keys[i]]][:5]
        kmodel.fit(data[[keys[i]]].as_matrix())

        r1=pd.Series(kmodel.labels_).value_counts()

        r2=pd.DataFrame(kmodel.cluster_centers_,
                        columns=[typelabel[keys[i]]])

        r1=pd.DataFrame(r1,columns=[typelabel[keys[i]]+'n'])

        #r=pd.concat([r2,r1],axis=1)
        r=pd.concat([r2,r1],axis=1).sort_values(by=[typelabel[keys[i]]])


        

        r.index=[1,2,3,4]
        print r

        r[typelabel[keys[i]]]=pd.rolling_mean(r[typelabel[keys[i]]],2)
        print r
        #用来计算相邻两列的均值，以此作为边界点
        r[typelabel[keys[i]]][1]=0.0
        print r
        #这两句代码将原来的聚类中心改为边界点
        result=result.append(r.T)
        print result

result=result.sort_index()
result.to_excel(outputfile)
'''


#利用关联规则
#导入编写的apriori


#自定义连接函数，用于实现L_{k-1}到C_k的连接
def connect_string(x, ms):
  x = list(map(lambda i:sorted(i.split(ms)), x))
  l = len(x[0])
  r = []
  for i in range(len(x)):
    for j in range(i,len(x)):
      if x[i][:l-1] == x[j][:l-1] and x[i][l-1] != x[j][l-1]:
        r.append(x[i][:l-1]+sorted([x[j][l-1],x[i][l-1]]))
  return r

#寻找关联规则的函数
def find_rule(d, support, confidence, ms = u'--'):
  result = pd.DataFrame(index=['support', 'confidence']) #定义输出结果
  
  support_series = 1.0*d.sum()/len(d) #支持度序列
  column = list(support_series[support_series > support].index) #初步根据支持度筛选
  k = 0
  
  while len(column) > 1:
    k = k+1
    print(u'\n正在进行第%s次搜索...' %k)
    column = connect_string(column, ms)
    print(u'数目：%s...' %len(column))
    sf = lambda i: d[i].prod(axis=1, numeric_only = True) #新一批支持度的计算函数
    
    #创建连接数据，这一步耗时、耗内存最严重。当数据集较大时，可以考虑并行运算优化。
    d_2 = pd.DataFrame(list(map(sf,column)), index = [ms.join(i) for i in column]).T
    
    support_series_2 = 1.0*d_2[[ms.join(i) for i in column]].sum()/len(d) #计算连接后的支持度
    column = list(support_series_2[support_series_2 > support].index) #新一轮支持度筛选
    support_series = support_series.append(support_series_2)
    column2 = []
    
    for i in column: #遍历可能的推理，如{A,B,C}究竟是A+B-->C还是B+C-->A还是C+A-->B？
      i = i.split(ms)
      for j in range(len(i)):
        column2.append(i[:j]+i[j+1:]+i[j:j+1])
    
    cofidence_series = pd.Series(index=[ms.join(i) for i in column2]) #定义置信度序列
 
    for i in column2: #计算置信度序列
      cofidence_series[ms.join(i)] = support_series[ms.join(sorted(i))]/support_series[ms.join(i[:len(i)-1])]
    
    for i in cofidence_series[cofidence_series > confidence].index: #置信度筛选
      result[i] = 0.0
      result[i]['confidence'] = cofidence_series[i]
      result[i]['support'] = support_series[ms.join(sorted(i.split(ms)))]
  
  result = result.T.sort_values(['confidence','support'], ascending = False) #结果整理，输出
  print u'\n结果为：'
  print result
  
  return result

#调用规则
import time

inputfile='chapter8/demo/data/apriori.txt'
data=pd.read_csv(inputfile,header=None,dtype=object)

start=time.clock()#即时开始

print u'\n转换矩阵开始0-1....'
ct=lambda x:pd.Series(1,index=x[pd.notnull(x)])
#转换0-1矩阵的过渡矩阵
b=map(ct,data.as_matrix())
data=pd.DataFrame(b).fillna(0)#填充0
end=time.clock()
print u'转换矩阵完毕，用时：%0.2f秒' %(end-start)
del b #删除中间变量


support=0.06
confidence=0.75
ms='---'

start=time.clock()
print u'开始搜索关联规则...'
find_rule(data,support,confidence,ms)
end=time.clock()
print u'搜索完成，用时%0.2f秒'%(end-start)




        
    
