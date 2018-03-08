import pandas as pd


# ��ȡ����
train = pd.read_csv("data/train1.csv")
test = pd.read_csv("data/test1.csv")
submit = pd.read_csv("data/sample_submit.csv")

# ɾ��id
train.drop('id', axis=1, inplace=True)
test.drop('id', axis=1, inplace=True)

# ȡ��ѵ������y
y_train = train.pop('y')

from sklearn import metrics
from sklearn.ensemble import ExtraTreesClassifier
model = ExtraTreesClassifier()
model.fit(train, y_train)
# display the relative importance of each attribute
print model.feature_importances_
