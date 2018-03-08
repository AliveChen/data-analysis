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





#model

import multiprocessing,Queue
#import xgboost as xgb
import numpy as np
from sklearn.linear_model import SGDClassifier, LogisticRegression,RidgeClassifier,PassiveAggressiveClassifier,Lasso,HuberRegressor
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.ensemble import VotingClassifier,RandomForestClassifier,gradient_boosting
from sklearn.ensemble.bagging import BaggingClassifier
from sklearn.ensemble.weight_boosting import AdaBoostClassifier
from sklearn.svm import LinearSVC, SVC
from sklearn.preprocessing import MinMaxScaler,StandardScaler,MaxAbsScaler

random_rate = 8240
clf1 = SGDClassifier(alpha=5e-05,average=False,class_weight='balanced',loss='log',n_iter=30,penalty='l2', n_jobs=-1, random_state=random_rate)
clf2 = MultinomialNB(alpha=0.1)
clf3 = LinearSVC(C=0.1, random_state=random_rate)
clf4 = LogisticRegression(C=1.0,n_jobs=-1, max_iter=100, class_weight='balanced', random_state=random_rate)
clf5 = BernoulliNB(alpha=0.1)
clf6 = VotingClassifier(estimators=[('sgd', clf1),('mb', clf2),('bb', clf3),('lf', clf4),('bnb', clf5)], voting='hard')
clf7 = SGDClassifier(alpha=5e-05,average=False,class_weight='balanced',loss='log',n_iter=30,penalty='l1', n_jobs=-1, random_state=random_rate)
clf8 = LinearSVC(C=0.9, random_state=random_rate)
clf9 = LogisticRegression(C=0.5, n_jobs=-1, max_iter=100, class_weight='balanced', random_state=random_rate)
clf10 = MultinomialNB(alpha=0.9)
clf11 = BernoulliNB(alpha=0.9)
clf12 = LogisticRegression(C=0.2, n_jobs=-1, max_iter=100, class_weight='balanced', random_state=random_rate,penalty='l1')
clf13 = LogisticRegression(C=0.8, n_jobs=-1, max_iter=100, class_weight='balanced', random_state=random_rate,penalty='l1')
clf14 = RidgeClassifier(alpha=8)
clf15 = PassiveAggressiveClassifier(C=0.01, loss='squared_hinge', n_iter=20, n_jobs=-1)
clf16 = RidgeClassifier(alpha=2)
clf17 = PassiveAggressiveClassifier(C=0.5, loss='squared_hinge', n_iter=30, n_jobs=-1)
clf18 = LinearSVC(C=0.5, random_state=random_rate)
clf19 = MultinomialNB(alpha=0.5)
clf20 = BernoulliNB(alpha=0.5)
clf21 = Lasso(alpha=0.1, max_iter=20, random_state=random_rate)
clf22 = Lasso(alpha=0.9, max_iter=30, random_state=random_rate)
clf23 = PassiveAggressiveClassifier(C=0.1, loss='hinge', n_iter=30, n_jobs=-1, random_state=random_rate)
clf24 = PassiveAggressiveClassifier(C=0.9, loss='hinge', n_iter=30, n_jobs=-1, random_state=random_rate)
clf25 = HuberRegressor(max_iter=30)

basemodel = [
    ['sgd', clf1],
    ['nb', clf2],
    ['lsvc1', clf3],
    ['LR1', clf4],
    ['bb',clf5],
    ['vote', clf6],
    ['sgdl1', clf7],
    ['lsvc2', clf8],
    ['LR2', clf9],
    ['nb2', clf10],
    ['bb2', clf11],
    ['LR3', clf12],
    ['LR4', clf13],
    ['rc1', clf14],
    ['pac1', clf15],
    ['rc2', clf16],
    ['pac2', clf17],
    ['lsvc3', clf18],
    ['nb3', clf19],
    ['bb3', clf20],
    ['lr5', clf21],
    ['lr6', clf22],
    ['rc3', clf23],
    ['pac3', clf24],
    ['hub', clf25],
    ]
        #####################################
clf_svc = SVC(C=1,random_state=random_rate,cache_size=1000)

base_models = basemodel
LR=clf4
svc = clf_svc


submit=pd.read_csv('sample_submit.csv')
for i,bm in enumerate(base_models):
    clf=bm[1]
    clf.fit(x_train,y_train)
    y_pred=clf.predict(testdata)
    submit[i+3]=np.array(y_pred)
submit.to_csv('quan.csv')
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








