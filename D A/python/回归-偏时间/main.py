#encoding=utf-8


import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

# 读取数据
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
submit = pd.read_csv("sample_submit.csv")

# 构造非线性特征
cols_lr = ['id', 'sqrt_id']
train['sqrt_id'] = np.sqrt(train['id'])
test['sqrt_id'] = np.sqrt(test['id'])
    
# 构造星期、月、年特征
train['date'] = pd.to_datetime(train['date'])
train['d_w'] = train['date'].dt.dayofweek
train['d_m'] = train['date'].dt.month
train['d_y'] = train['date'].dt.year
test['date'] = pd.to_datetime(test['date'])
test['d_w'] = test['date'].dt.dayofweek
test['d_m'] = test['date'].dt.month
test['d_y'] = test['date'].dt.year
cols_knn = ['d_w', 'd_m', 'd_y']

# 根据特征['id', 'sqrt_id']，构造线性模型预测questions
reg = LinearRegression()
reg.fit(train[cols_lr], train['questions'])
q_fit = reg.predict(train[cols_lr])
q_pred = reg.predict(test[cols_lr])

# 根据特征['id', 'sqrt_id']，构造线性模型预测answers
reg = LinearRegression()
reg.fit(train[cols_lr], train['answers'])
a_fit = reg.predict(train[cols_lr])
a_pred = reg.predict(test[cols_lr])

# 得到questions和answers的训练误差
q_diff = train['questions'] - q_fit
a_diff = train['answers'] - a_fit

# 把训练误差作为新的目标值，使用特征cols_knn，建立kNN模型
from sklearn.neighbors import KNeighborsRegressor
reg = KNeighborsRegressor()
reg.fit(train[cols_knn], q_diff)
q_pred_knn = reg.predict(test[cols_knn])
reg = KNeighborsRegressor()
reg.fit(train[cols_knn], a_diff)
a_pred_knn = reg.predict(test[cols_knn])

#输出预测结果至my_Lr_Knn_prediction.csv
submit['questions'] = q_pred + q_pred_knn
submit['answers'] = a_pred + a_pred_knn
submit.to_csv('my_Lr_Knn_prediction.csv', index=False)
