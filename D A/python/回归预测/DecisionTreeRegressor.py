# -*- coding: utf-8 -*-


# 引入模块

import pandas as pd
from sklearn.tree import DecisionTreeRegressor# 读取数据
train = pd.read_csv("data/train1.csv")
test = pd.read_csv("data/test1.csv")
submit = pd.read_csv("data/sample_submit.csv")

# 删除id
train.drop('id', axis=1, inplace=True)
test.drop('id', axis=1, inplace=True)

# 取出训练集的y
y_train = train.pop('y')




reg = DecisionTreeRegressor(max_depth=5)
reg.fit(train, y_train)





#y_pred = reg.predict(test)


# 输出预测结果至my_tdr_prediction.csv
#submit['y'] = y_pred
#submit.to_csv('data/my_tdr_prediction22.csv', index=False)

from sklearn import metrics
import numpy as np
rmse=np.sqrt(metrics.mean_squared_error(y_train, reg.predict(train)))
print 'linearRegression rmse为%f'%rmse
#xgboots 18.5718185229
#linearRegression rmse为38.920108
#linearRegression rmse为27.865298
