#coding=utf-8

import pandas as pd
train_path='user_tag_query.10W.TRAIN.csv'
test_path='user_tag_query.10W.TEST.csv'
train_data=pd.read_csv(train_path)
test_data=pd.read_csv(test_path)
train_data.age.to_csv('train_data_age.csv',index=False)
train_data.Gender.to_csv('train_data_gender.csv',index=False)
train_data.Education.to_csv('train_data_education.csv',index=False)
train_data.QueryList.to_csv('train_data_querylist.csv',index=False)

test_data=pd.read_csv(test_path)
test_data.QueryList.to_csv('test_data_quesylist.csv',index=False)
print train_data.Gender.value_counts()
