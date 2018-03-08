# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 19:05:24 2018

@author: chen
"""

import pandas as pd

data=pd.read_csv('test.csv',encoding='utf-8',index_col='id')
print data.info()
data.gk=data['gk'].fillna(data[['rw','rb','st','lw','cf','cam','cm','cdm','cb','lb']].sum(axis=1)/10)
data['work_rate_att'][data['work_rate_att']=='Low']=1
data['work_rate_att'][data['work_rate_att']=='Medium']=2
data['work_rate_att'][data['work_rate_att']=='High']=3
data['work_rate_def'][data['work_rate_def']=='Low']=1
data['work_rate_def'][data['work_rate_def']=='Medium']=2
data['work_rate_def'][data['work_rate_def']=='High']=3
data=data.drop(['birth_date','rw','rb','st','lw','cf','cam','cm','cdm','cb','lb'],axis=1)
data.to_csv('test2.csv')
