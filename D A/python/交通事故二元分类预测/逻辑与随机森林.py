#coding=utf-8
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
filname='data/train.csv'
data=pd.read_csv(filname)
x=data.iloc[:,1:37].as_matrix()#转化为矩阵
test = pd.read_csv("data/test.csv")
y=data.iloc[:,37].as_matrix()#矩阵
submit = pd.read_csv("data/sample_submit.csv")
clf = RandomForestClassifier()
clf.fit(x,y)
test=test.iloc[:,1:].as_matrix()
y_pred = clf.predict_proba(test)[:, 1]



submit['Evaluation'] = y_pred
submit.to_csv('data/my_RF_prediction3.csv', index=False)
