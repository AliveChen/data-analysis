'''
#coding=utf-8
#朗格朗日插值处理
import pandas as pd
from scipy.interpolate import lagrange

inputfile='chapter6/test/data/missing_data.xls'
outputfile='chapter6/out/missing_data_processed'
data=pd.read_excel(inputfile,header=None)

#定义插值函数
def lagrange_interpolate(s,n,k=5):
    p=s[list(range(n-5,n))+list(range(n+1,n+1+k))]
    p=p[p.notnull()]
    return lagrange(p.index,list(p))(n)
#查找空值
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j]=lagrange_interpolate(data[i],j)
#备注：[data[i].isnull()][j]是错误的
#print data

#漏电用户的分类预测

#lm神经网络
from random import shuffle
inputfile2='chapter6/test/data/model.xls'
data=pd.read_excel(inputfile2,header=None)
data=data.as_matrix()

p=0.8
train=data[:int(len(data)*p),:]
test=data[int(len(data)*p):,:]

max_words = 1000 #vocab大小
from keras.models import Sequential
from keras.layers.core import Dense,Activation

netfile='chapter6/out/net.model'

net=Sequential()
net.add(Dense(3,10,init='uniform'))
net.add(Activation('relu'))
net.add(Dense(10,1,init='uniform'))
net.add(Activation('sigmoid'))
net.compile(loss='binary_crossentropy',optimizer='adam',class_mode='binary')

net.fit(train[:,:3],train[:,3],nb_epoch=1000,batch_size=1)
net.save_weights(netfile)

predict_result=net.predict_classes(train[:,:3]).reshape(len(train))
from cm_plot import *
cm_plot(train[:,3],predict_result).show()
'''


#-*- coding: utf-8 -*-
#构建并测试CART决策树模型

import pandas as pd #导入数据分析库
from random import shuffle #导入随机函数shuffle，用来打算数据


def cm_plot(y, yp):
  
  from sklearn.metrics import confusion_matrix #导入混淆矩阵函数

  cm = confusion_matrix(y, yp) #混淆矩阵
  
  import matplotlib.pyplot as plt #导入作图库
  plt.matshow(cm, cmap=plt.cm.Greens) #画混淆矩阵图，配色风格使用cm.Greens，更多风格请参考官网。
  plt.colorbar() #颜色标签
  
  for x in range(len(cm)): #数据标签
    for y in range(len(cm)):
      plt.annotate(cm[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
  
  plt.ylabel('True label') #坐标轴标签
  plt.xlabel('Predicted label') #坐标轴标签
  return plt



datafile = 'chapter6/test/data/model.xls' #数据名
data = pd.read_excel(datafile) #读取数据，数据的前三列是特征，第四列是标签
data = data.as_matrix() #将表格转换为矩阵
shuffle(data) #随机打乱数据

p = 0.8 #设置训练数据比例
train = data[:int(len(data)*p),:] #前80%为训练集
test = data[int(len(data)*p):,:] #后20%为测试集


#构建CART决策树模型
from sklearn.tree import DecisionTreeClassifier #导入决策树模型

treefile = 'chapter6/out/tree.pkl' #模型输出名字
tree = DecisionTreeClassifier() #建立决策树模型
tree.fit(train[:,:3], train[:,3]) #训练

#保存模型
from sklearn.externals import joblib
joblib.dump(tree, treefile)

#from cm_plot import * #导入自行编写的混淆矩阵可视化函数
cm_plot(train[:,3], tree.predict(train[:,:3])).show() #显示混淆矩阵可视化结果
#注意到Scikit-Learn使用predict方法直接给出预测结果。

from sklearn.metrics import roc_curve #导入ROC曲线函数
import matplotlib.pyplot as plt
fpr, tpr, thresholds = roc_curve(test[:,3], tree.predict_proba(test[:,:3])[:,1], pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label = 'ROC of CART', color = 'green') #作出ROC曲线
plt.xlabel('False Positive Rate') #坐标轴标签
plt.ylabel('True Positive Rate') #坐标轴标签
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc=4) #图例
plt.show()




