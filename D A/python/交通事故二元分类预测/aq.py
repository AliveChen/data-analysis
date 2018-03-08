
#coding=utf-8
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
results = []
sample_leaf_options = list(range(1, 500, 3))
n_estimators_options = list(range(1, 1000, 5))
#groud_truth = train_data['Survived'][601:]
filname='data/train.csv'
data=pd.read_csv(filname)
x=data.iloc[:,1:37].as_matrix()#转化为矩阵
test = pd.read_csv("data/test.csv")
y=data.iloc[:,37].as_matrix()#矩阵
submit = pd.read_csv("data/sample_submit.csv")
for leaf_size in sample_leaf_options:
    for n_estimators_size in n_estimators_options:
        alg = RandomForestClassifier(min_samples_leaf=leaf_size, n_estimators=n_estimators_size, random_state=50)
        alg.fit(x,y)
        predict = alg.predict(x)
        # 用一个三元组，分别记录当前的 min_samples_leaf，n_estimators， 和在测试数据集上的精度
        results.append((leaf_size, n_estimators_size, (y == predict).mean()))
        # 真实结果和预测结果进行比较，计算准确率
        print((y == predict).mean())

# 打印精度最大的那一个三元组
print(max(results, key=lambda x: x[2]))
