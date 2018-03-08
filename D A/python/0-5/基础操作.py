#coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
'''
b='zhexiantu.xls'
a=pd.read_excel(b,header=None)
print a
x=a[0]
y=a[1]
print a.corr()


print a


plt.figure(figsize=(8,4))
plt.plot(x,y,label='$y xian$',color='red',linewidth=2)
plt.xlabel('time(s)')
plt.ylabel('sale')
plt.title('a simple example')
plt.ylim(0,30)
plt.legend()
plt.show()

#绘制饼图

sizes=[20,50,15,15]


labels=['example1','example2','exampel3','example']
colors=['red','orange','black','green']
explode=[0,0,0.1,0]
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',
        shadow=False,startangle=90)
plt.axis('equal')
plt.show()


from sklearn import datasets#导入内置的数据集
iris=datasets.load_iris()
print iris.data.shape#描述行列数
print iris.data[0:5]#观测，这个是numpy，没有head
from sklearn import svm

clf=svm.LinearSVC()#建立线性svm分类器
clf.fit(iris.data,iris.target)#用数据训练模型
clf.predict([5.0,3.6,1.3,0.25])#输入新的数据进行预测
print clf.coef_#查看训练好的模型参数


from scipy.interpolate import lagrange
b='zhexiantu.xls'
a=pd.read_excel(b,header=None)
print a
a[1][a[1]==12]=None
print a
#定义插值函数
def plyinsert(s,n,k=5):
    y=s[list(range(n-k,n))+list(range(n+1,n+1+k))]
    y=y[y.notnull()]
    return lagrange(y.index,list(y))(n)
for i in a.columns:
    for j in range(len(a)):
        if (a[i].isnull())[j]:
            a[i][j]=plyinsert(a[i],j)
print a

#主成分分析

b='zhexiantu.xls'
a=pd.read_excel(b)
from sklearn.decomposition import PCA
pca=PCA()
pca.fit(a)
print pca.components_#返回模型的各个特征向量
print u'方差贡献%s' %pca.explained_variance_ratio_#返回各个成分方差百分比
pca=PCA(1)
pca.fit(a)
low_d=pca.transform(a)#降维
#pd.DataFrame(low_d).to_excel()#保存
#pca.inverse_transform(low_d)#必要时复原数据
print low_d

#逻辑回归
filname='chapter5/demo/data/bankloan.xls'
data=pd.read_excel(filname)
x=data.iloc[:,:8].as_matrix()#转化为矩阵

y=data.iloc[:,8].as_matrix()#矩阵
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR 
rlr=RLR()#建立随机逻辑回归，模型，筛选变量
#这里采用的0.25rlr=RLR(selection_threshold=0.5)，
rlr.fit(x,y)#训练模型
rlr.get_support()#特征筛选结果，也可以用.sore
print rlr.get_support()#是一个布尔值list
print data.columns[0:8][rlr.get_support()]
#前面为列索引名称追加布尔值，只显示有显著性
#备注：原data列长度为9，但布尔值长度为8，所以【0:8】删结果列
print u'通过随机逻辑回归模型筛选特征结束'
print u'有限特征为：%s' % ','.join(data.columns[0:8][rlr.get_support()])
x=data[data.columns[0:8][rlr.get_support()]].as_matrix()#筛选后数据
lr=LR()
lr.fit(x,y)
print u'逻辑回归模型训练结束'
print u'模型的平均正确率为：%s'%lr.score(x,y)

#k—means聚类，餐饮客户分类
inputfile='chapter5/demo/data/consumption_data.xls'
outputfile='chapter5/out/data_type.xls'
k=3
iteration=500
data=pd.read_excel(inputfile,index_col='Id')
data_zs=1.0*(data-data.mean())/data.std()
from sklearn.cluster import KMeans
model=KMeans(n_clusters=k,n_jobs=1,max_iter=iteration)

model.fit(data_zs)

r1=pd.Series(model.labels_).value_counts()
print r1
r2=pd.DataFrame(model.cluster_centers_)
print r2
r=pd.concat([r2,r1],axis=1)
r.columns=list(data.columns)+[u'类别数目']
print r

r=pd.concat([data,pd.Series(model.labels_,index=data.index)],axis=1)
r.columns=list(data.columns)+[u'聚类类别']
r.to_excel(outputfile)

#绘制聚类后的概率密度图
def density_plot(data): #自定义作图函数
  import matplotlib.pyplot as plt
  plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
  plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号
  p = data.plot(kind='kde', linewidth = 2, subplots = True, sharex =False)
  [p[i].set_ylabel(u'密度') for i in range(k)]
  plt.legend()
  return plt
pic_output = 'chapter5/out/pd_' #概率密度图文件名前缀
for i in range(k):
  density_plot(data[r[u'聚类类别']==i]).savefig(u'%s%s.png' %(pic_output, i))
#print data[r[u'聚类类别']==2]能把类别为2的数据rfm三列数据都提出来

'''
#-*- coding: utf-8 -*-

import pandas as pd

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

#apriori关联规则

inputfile='chapter5/demo/data/menu_orders.xls'
outputfile='chapter5/out/apriori_rule.xls'
data=pd.read_excel(inputfile,header=None)

print u'\n转换原始数据至0-1矩阵。。。'
ct=lambda x: pd.Series(1,index=x[pd.notnull(x)])
b=map(ct,data.as_matrix())
data=pd.DataFrame(list(b)).fillna(0)
print data
print(u'\n转换完毕')
del b
support=0.2
confidence=0.5
ms='---'
find_rule(data,support,confidence,ms).to_excel(outputfile)

