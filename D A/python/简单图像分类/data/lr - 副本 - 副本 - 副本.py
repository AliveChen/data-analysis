#encoding=utf-8
import pandas as pd

jiaquan=pd.read_csv('quan.csv',index_col='id')
print(jiaquan)
jq=[]
for i in range(len(jiaquan)):
    res={0:0,1:0}
    a=list(jiaquan.iloc[i,:])

    for v in a:
        res[v]=res[v]+1
    if res[1]>res[0]:
        jq.append(1)
    else:
        jq.append(0)
jiaquan['jiaquan']=jq
jiaquan[['jiaquan']].to_csv('zhenshi.csv')


    


