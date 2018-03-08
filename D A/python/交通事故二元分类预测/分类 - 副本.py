# -*- coding: utf-8 -*-
import pandas as pd

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

'''
from sklearn.ensemble import RandomForestClassifier

# 读取数据
train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")
submit = pd.read_csv("data/sample_submit.csv")

# 删除id
train.drop('CaseId', axis=1, inplace=True)
test.drop('CaseId', axis=1, inplace=True)

# 取出训练集的y
y_train = train.pop('Evaluation')

# 建立随机森林模型
clf = RandomForestClassifier(n_estimators=100, random_state=0)
clf.fit(train, y_train)
y_pred = clf.predict_proba(test)[:, 1]

# 输出预测结果至my_RF_prediction.csv
submit['Evaluation'] = y_pred
submit.to_csv('data/my_RF_prediction.csv', index=False)
'''


'''
#逻辑回归
filname='data/train.csv'
data=pd.read_csv(filname)
x=data.iloc[:,1:37].as_matrix()#转化为矩阵

submit = pd.read_csv("data/sample_submit.csv")
test = pd.read_csv("data/test.csv")
y=data.iloc[:,37].as_matrix()#矩阵
from sklearn.linear_model import LogisticRegression as LR
from sklearn.linear_model import RandomizedLogisticRegression as RLR 
rlr=RLR()#建立随机逻辑回归，模型，筛选变量
rlr.fit(x,y)#训练模型
rlr.get_support()#特征筛选结果，也可以用.sore
print rlr.get_support()#是一个布尔值list
print data.columns[1:37][rlr.get_support()]
#前面为列索引名称追加布尔值，只显示有显著性
#备注：原data列长度为9，但布尔值长度为8，所以【0:8】删结果列
print u'通过随机逻辑回归模型筛选特征结束'
print u'有限特征为：%s' % ','.join(data.columns[1:37][rlr.get_support()])
x=data[data.columns[1:37][rlr.get_support()]].as_matrix()#筛选后数据
lr=LR()
lr.fit(x,y)
print u'逻辑回归模型训练结束'
print u'模型的平均正确率为：%s'%lr.score(x,y)
test=test[test.columns[1:][rlr.get_support()]].as_matrix()

y_pred = lr.predict_proba(test)[:,1]
submit['Evaluation'] = y_pred
submit.to_csv('data/my_LASSO_prediction2.csv', index=False)
'''



'''
#cart决策树
filname='data/train.csv'
test = pd.read_csv("data/test.csv")
data=pd.read_csv(filname)
x=data.iloc[:,1:37].as_matrix()#转化为矩阵

submit = pd.read_csv("data/sample_submit.csv")
test = pd.read_csv("data/test.csv")
y=data.iloc[:,37].as_matrix()#矩阵

from sklearn.tree import DecisionTreeClassifier
tree = DecisionTreeClassifier() #建立决策树模型
tree.fit(x,y)
test=test.iloc[:, 1:].as_matrix()
y_pred = tree.predict_proba(test)[:,1]
#y_pred = tree.predict(test.iloc[:, 1:])
#也就是说proba需要两个索引框
submit['Evaluation'] = y_pred
submit.to_csv('data/cart_prdict2.csv', index=False)
'''




