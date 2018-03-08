#encoding=utf-8
import numpy as np
import pandas as pd
data=pd.read_csv('train2.csv',index_col='id')

#print np.round(data.corr(method='pearson'),2)
from sklearn.linear_model import LassoLarsCV
#print len(data.columns)
#print data.iloc[:,52]
x=data.iloc[:,0:52].as_matrix()
y=data.iloc[:,52].as_matrix()

ll=LassoLarsCV()
ll.fit(x,y)

a=ll.coef_
b=[i!=0 for i in a]

data1=data.iloc[:,0:52]
data1=data1[data1.columns[b]]
x=data1.iloc[:,:].as_matrix()

from xgboost import XGBRegressor

reg = XGBRegressor()
reg.fit(x, y)
y_pred = reg.predict(x)
print ('有限特征%s'%data1.columns)
testdata=pd.read_csv('test2.csv',index_col='id')
testdata=testdata[testdata.columns[b]].as_matrix()

y_pred=pd.Series(reg.predict(x))
#y_pred.to_csv('6666.csv')





