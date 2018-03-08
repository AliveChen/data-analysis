'''
#coding=utf-8
#�ʸ����ղ�ֵ����
import pandas as pd
from scipy.interpolate import lagrange

inputfile='chapter6/test/data/missing_data.xls'
outputfile='chapter6/out/missing_data_processed'
data=pd.read_excel(inputfile,header=None)

#�����ֵ����
def lagrange_interpolate(s,n,k=5):
    p=s[list(range(n-5,n))+list(range(n+1,n+1+k))]
    p=p[p.notnull()]
    return lagrange(p.index,list(p))(n)
#���ҿ�ֵ
for i in data.columns:
    for j in range(len(data)):
        if (data[i].isnull())[j]:
            data[i][j]=lagrange_interpolate(data[i],j)
#��ע��[data[i].isnull()][j]�Ǵ����
#print data

#©���û��ķ���Ԥ��

#lm������
from random import shuffle
inputfile2='chapter6/test/data/model.xls'
data=pd.read_excel(inputfile2,header=None)
data=data.as_matrix()

p=0.8
train=data[:int(len(data)*p),:]
test=data[int(len(data)*p):,:]

max_words = 1000 #vocab��С
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
#����������CART������ģ��

import pandas as pd #�������ݷ�����
from random import shuffle #�����������shuffle��������������


def cm_plot(y, yp):
  
  from sklearn.metrics import confusion_matrix #�������������

  cm = confusion_matrix(y, yp) #��������
  
  import matplotlib.pyplot as plt #������ͼ��
  plt.matshow(cm, cmap=plt.cm.Greens) #����������ͼ����ɫ���ʹ��cm.Greens����������ο�������
  plt.colorbar() #��ɫ��ǩ
  
  for x in range(len(cm)): #���ݱ�ǩ
    for y in range(len(cm)):
      plt.annotate(cm[x,y], xy=(x, y), horizontalalignment='center', verticalalignment='center')
  
  plt.ylabel('True label') #�������ǩ
  plt.xlabel('Predicted label') #�������ǩ
  return plt



datafile = 'chapter6/test/data/model.xls' #������
data = pd.read_excel(datafile) #��ȡ���ݣ����ݵ�ǰ�������������������Ǳ�ǩ
data = data.as_matrix() #�����ת��Ϊ����
shuffle(data) #�����������

p = 0.8 #����ѵ�����ݱ���
train = data[:int(len(data)*p),:] #ǰ80%Ϊѵ����
test = data[int(len(data)*p):,:] #��20%Ϊ���Լ�


#����CART������ģ��
from sklearn.tree import DecisionTreeClassifier #���������ģ��

treefile = 'chapter6/out/tree.pkl' #ģ���������
tree = DecisionTreeClassifier() #����������ģ��
tree.fit(train[:,:3], train[:,3]) #ѵ��

#����ģ��
from sklearn.externals import joblib
joblib.dump(tree, treefile)

#from cm_plot import * #�������б�д�Ļ���������ӻ�����
cm_plot(train[:,3], tree.predict(train[:,:3])).show() #��ʾ����������ӻ����
#ע�⵽Scikit-Learnʹ��predict����ֱ�Ӹ���Ԥ������

from sklearn.metrics import roc_curve #����ROC���ߺ���
import matplotlib.pyplot as plt
fpr, tpr, thresholds = roc_curve(test[:,3], tree.predict_proba(test[:,:3])[:,1], pos_label=1)
plt.plot(fpr, tpr, linewidth=2, label = 'ROC of CART', color = 'green') #����ROC����
plt.xlabel('False Positive Rate') #�������ǩ
plt.ylabel('True Positive Rate') #�������ǩ
plt.ylim(0,1.05) #�߽緶Χ
plt.xlim(0,1.05) #�߽緶Χ
plt.legend(loc=4) #ͼ��
plt.show()




