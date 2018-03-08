
# -*- coding: utf-8 -*-

# 引入模块
from xgboost import XGBRegressor
import pandas as pd

# 读取数据
train = pd.read_csv("train2.csv")
test = pd.read_csv("test1.csv")
submit = pd.read_csv("sample_submit.csv")

# 删除id
train.drop('id', axis=1, inplace=True)
test.drop('id', axis=1, inplace=True)

# 取出训练集的y
y_train = train.pop('y')

# 建立一个默认的xgboost回归模型
reg = XGBRegressor()
reg.fit(train, y_train)
y_pred = reg.predict(test)

# 输出预测结果至my_XGB_prediction.csv
submit['y'] = y_pred
submit.to_csv('my_XGB_prediction.csv', index=False)
