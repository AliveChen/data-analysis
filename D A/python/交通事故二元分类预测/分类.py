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

#coding=utf-8
#朗格朗日插值处理
import pandas as pd
inputfile='data/train.csv'
data=pd.read_csv(inputfile)
L1=len(data)
explore=data.describe().T
explore['null']=L1-explore['count']
explore=explore[['null']]

data=data.as_matrix()

shuffle(data)

from sklearn.tree import DecisionTreeClassifier
treefile = 'data/tree.pkl'
tree = DecisionTreeClassifier() #建立决策树模型
tree.fit(data[:,1:37],data[:,37])

from sklearn.externals import joblib
joblib.dump(tree, treefile)
#from cm_plot import * #导入自行编写的混淆矩阵可视化函数
cm_plot(data[:,37], tree.predict(data[:,1:37])).show()
data2=pd.read_csv('data/test.csv')
data3=data2[['CaseId']]
data4=data2.as_matrix()
data3['predict']=tree.predict(data4[:,1:])
data3.to_csv('data/111.csv')

from sklearn.metrics import roc_curve #导入ROC曲线函数
import matplotlib.pyplot as plt
fpr, tpr, thresholds = roc_curve(data[:,37], tree.predict_proba(data[:,1:37])[:,1], pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label = 'ROC of CART', color = 'green') #作出ROC曲线
plt.xlabel('False Positive Rate') #坐标轴标签
plt.ylabel('True Positive Rate') #坐标轴标签
plt.ylim(0,1.05) #边界范围
plt.xlim(0,1.05) #边界范围
plt.legend(loc=4) #图例
plt.show()


