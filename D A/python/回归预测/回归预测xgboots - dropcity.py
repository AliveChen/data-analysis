# -*- coding: utf-8 -*-
#python 3有xgboots

# 引入模块

import pandas as pd

from xgboost import XGBRegressor
# 读取数据
train = pd.read_csv("data/train1.csv")
test = pd.read_csv("data/test1.csv")
submit = pd.read_csv("data/sample_submit.csv")

# 删除id
train.drop('id', axis=1, inplace=True)
train.drop('city', axis=1, inplace=True)
test.drop('id', axis=1, inplace=True)

# 取出训练集的y
y_train = train.pop('y')



# 建立一个默认的xgboost回归模型
reg = XGBRegressor()
reg.fit(train, y_train)

#y_pred = reg.predict(test)


# 输出预测结果至my_XGB_prediction.csv
#submit['y'] = y_pred
#submit.to_csv('data/my_XGB_prediction22.csv', index=False)

from sklearn import metrics
import numpy as np
rmse=np.sqrt(metrics.mean_squared_error(y_train, reg.predict(train)))
print (rmse)
#18.5718185229
