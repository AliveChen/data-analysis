import pandas as pd


# 读取数据
train = pd.read_csv("data/train1.csv")
test = pd.read_csv("data/test1.csv")
submit = pd.read_csv("data/sample_submit.csv")

# 删除id
train.drop('id', axis=1, inplace=True)
test.drop('id', axis=1, inplace=True)

# 取出训练集的y
y_train = train.pop('y')

from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(train, y_train)
# display the relative importance of each attribute
print model.feature_importances_
