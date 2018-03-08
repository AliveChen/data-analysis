# -*- coding: utf-8 -*-


# 引入模块

import pandas as pd
from sklearn.linear_model import LinearRegression

# 读取数据
train = pd.read_csv("data/train1.csv")
test = pd.read_csv("data/test1.csv")
submit = pd.read_csv("data/sample_submit.csv")

# 删除id
train.drop('id', axis=1, inplace=True)
test.drop('id', axis=1, inplace=True)

# 取出训练集的y
y_train = train.pop('y')



# 建立线性回归模型
reg = LinearRegression()
reg.fit(train, y_train)


#y_pred = reg.predict(test)

# 若预测值是负数，则取0
#y_pred = map(lambda x: x if x >= 0 else 0, y_pred)
# 输出预测结果至my_XGB_prediction.csv
#submit['y'] = y_pred
#submit.to_csv('data/my_linearRegression_prediction22.csv', index=False)
print reg.coef_
from sklearn import metrics
import numpy as np
rmse=np.sqrt(metrics.mean_squared_error(y_train, reg.predict(train)))
print 'linearRegression rmse为%f'%rmse
#xgboots 18.5718185229
#linearRegression rmse为38.920108
