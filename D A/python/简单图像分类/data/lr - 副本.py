# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
from collections import Counter
from sklearn.ensemble import GradientBoostingClassifier
#import matlibplot.pylot

#读取数据
data=pd.read_csv('train.csv',index_col='id',encoding='utf-8')
test=pd.read_csv('test.csv',index_col='id',encoding='utf-8')
print data.shape
print test.shape

data=data.as_matrix()
testdata=test.as_matrix()




from random import shuffle

date=shuffle(data)
data_train=data

#data_train=data[:int(0.8*len(data)),:]
#data_test=data[int(0.8*len(data)):,:]
#print data_train[:,1600]

x_train=data_train[:,:1600]
y_train=data_train[:,1600].astype(int)


#x_test=data_test[:,:1600]
#y_test=data_test[:,1600].astype(int)




#model
from sklearn import svm

model=svm.LinearSVC()

model.fit(x_train,y_train)

#import pickle
#pickle.dump(model,open('svmlinearsvc.model','wb'))
#保存模型
#加载模型、




#import pickle
#model=pickle.load(open('svmlinearsvc.model','rb'))
'''
from sklearn import metrics
cm_train=metrics.confusion_matrix(y_train,model.predict(x_train))
#cm_train.show()
print cm_train
#训练样本的魂系矩阵
cm_test=metrics.confusion_matrix(y_test,model.predict(x_test))
print cm_test
#测试的混xi矩阵
'''


yred=model.predict(testdata)
print yred[0:1000]


submit=pd.read_csv('sample_submit.csv')

submit['yed']=np.array(yred)
submit.to_csv('linearsvcquan.csv')



