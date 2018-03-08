import pandas as pd
import numpy as np
from sklearn import  preprocessing
import xgboost as xgb
import lightgbm as lgb
from sklearn.model_selection import train_test_split
import os
os.chdir("/root/user/tianchi")
def haversine(lon1, lat1, lon2, lat2):
    from math import radians, cos, sin, asin, sqrt
    lon1= map(radians, np.array(lon1))  
    lat1= map(radians, np.array(lat1))
    lon2= map(radians, np.array(lon2))
    lat2= map(radians, np.array(lat2))
    lon1 = np.array(list(lon1)).reshape(-1,1)
    lon2 = np.array(list(lon2)).reshape(-1,1)
    lat1 = np.array(list(lat1)).reshape(-1,1)
    lat2 = np.array(list(lat2)).reshape(-1,1)
    dlon = lon2 - lon1
    dlat = lat2 - lat1 
    a = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2  
    c = 2 * np.arcsin(np.sqrt(a))   
    r = 6371
    return c * r * 1000  
column1=[]
for i in range(10):
    column1.append("wificc{}".format(i))
path='./'
df=pd.read_csv(path+u'ccf_first_round_user_shop_behavior.csv',engine='python')
shop=pd.read_csv(path+u'ccf_first_round_shop_info.csv',engine='python')
test=pd.read_csv(path+u'evaluation_public.csv',engine='python')
df=pd.merge(df,shop[['shop_id','mall_id']],how='left',on='shop_id')
train=pd.concat([df,test])
train['time_stamp']=pd.to_datetime(train['time_stamp'])
train['isweekend']=train.time_stamp.map(lambda x:1 if x.weekday()>4 else 0)
dfx1=df.set_index("shop_id").wifi_infos.str.split(";",expand=True)
dfx1=dfx1.fillna("l").applymap(lambda x:x[:x.find("|")] if "b" in x else np.nan)
dfx2=dfx1[0]
for i in dfx1.columns[1:]:
    dfx3=dfx1[i]
    dfx2=pd.concat([dfx2,dfx3])
dfx2.dropna(inplace=True)
shop=pd.merge(shop,pd.DataFrame(dfx2.groupby(level=0).apply(lambda x:np.array(x.value_counts()[x.value_counts()>1].index))).rename(columns={0:"wifi1"}),left_on="shop_id",right_index=True)
shop=pd.merge(shop,pd.DataFrame(dfx2.groupby(level=0).apply(lambda x:np.array(x.value_counts()[x.value_counts()>10].index))).rename(columns={0:"wifi2"}),left_on="shop_id",right_index=True)
shop=pd.merge(shop,pd.DataFrame(dfx2.groupby(level=0).apply(lambda x:np.array(x.value_counts()[x.value_counts()>20].index))).rename(columns={0:"wifi3"}),left_on="shop_id",right_index=True)
shop=pd.merge(shop,pd.DataFrame(dfx2.groupby(level=0).apply(lambda x:np.array(x.value_counts().index))).rename(columns={0:"wific"}),left_on="shop_id",right_index=True)
lbl = preprocessing.LabelEncoder()
shop["category_id"]=lbl.fit_transform(shop.category_id.values)
result=pd.DataFrame()
df['time_stamp']=pd.to_datetime(df['time_stamp'])
df["hour"]=df.time_stamp.map(lambda x:x.hour)
dfz1=df.groupby(["shop_id","hour"]).shop_id.count().unstack().fillna(0)
dfz2=df.groupby(["mall_id","hour"]).shop_id.count().unstack().fillna(0)
shopx=pd.merge(shop.set_index("shop_id"),df.groupby(["mall_id","hour"]).shop_id.count().unstack(),left_on="mall_id",right_index=True)
dfzz=(dfz1/shopx.loc[:,range(24)].loc[dfz1.index]).fillna(0)
for i in shop.mall_id.unique():
    train1=train[train.mall_id==i]
    train1=train1.reset_index().drop("index",axis=1)
    shop1=shop[shop.mall_id==i]
    shop1.columns=shop1.columns.map(lambda x:x+"1")
    xx=train1.wifi_infos.str.split(";",expand=True).fillna("l").applymap(lambda x:x.split("|")[0] if "b" in x else np.nan)
    yy=train1.wifi_infos.str.split(";",expand=True).fillna("l").applymap(lambda x:x.split("|")[1] if "b" in x else np.nan)
    yy=yy.astype(float)
    dfy2=xx[0]
    for i in xx.columns[1:]:
        dfy3=xx[i]
        dfy2=pd.concat([dfy2,dfy3])
    indexx=dfy2.value_counts()[dfy2.value_counts()>20].index
    xx=xx.applymap(lambda x:x if x in indexx else np.nan)
    yy[xx.isnull()]=np.nan
    train1=pd.merge(train1,pd.DataFrame(xx.apply(lambda x:dict(zip(x.dropna().values.tolist(),yy.loc[x.name].dropna().values.tolist())),axis=1)).rename(columns={0:"wifid"}),left_index=True,right_index=True)
    dfy2=dfy2.map(lambda x:x if x in indexx else np.nan)
    dfy2.dropna(inplace=True)
    train1=pd.merge(train1,pd.DataFrame(dfy2.groupby(level=0).apply(lambda x:x.values)).rename(columns={0:"wifix"}),left_index=True,right_index=True)
    train2=pd.merge(train1,shop1,left_on="mall_id",right_on="mall_id1")
    train2["away"]=haversine(train2.longitude1,train2.latitude1,train2.longitude,train2.latitude)
    train2["wificount1"]=train2.wifi11.map(lambda x:len(x))
    train2["wificount2"]=train2.wifi21.map(lambda x:len(x))
    train2["wificount3"]=train2.wifi31.map(lambda x:len(x))
    train2["wificount4"]=train2.wific1.map(lambda x:len(x))
    train2[["count1","count2","count3"]]=train2.apply(lambda x:x[["wifi11","wifi21","wifi31"]].map(lambda y:len(np.intersect1d(y,x.wifix))/len(x.wifix)),axis=1)
    train2["hour"]=train2.time_stamp.map(lambda x:x.hour)
    train2["hourco"]=train2.apply(lambda x:dfzz.loc[x.shop_id1,x.hour],axis=1)
    def fun(x):
        dic=x.wifid
        ss=pd.Series(np.intersect1d(x.wific1,x.wifix))
        ss=ss.map(dic).sort_values(ascending=False).values.tolist()
        if len(ss)<10:
            ss.extend([""]*(10-len(ss)))
        return "{},{},{},{},{},{},{},{},{},{}".format(ss[0],ss[1],ss[2],ss[3],ss[4],ss[5],ss[6],ss[7],ss[8],ss[9])
    train2["wifico"]=train2.apply(fun,axis=1)
    trainx=train2.wifico.str.split(",",expand=True).applymap(lambda x:np.nan if len(x)==0 else x).astype(float)
    trainx.columns=column1
    trainx["wifimean"]=trainx.mean(1)
    trainx["wifisum"]=trainx.sum(1)
    trainx["wificount"]=trainx.count(1)
    train2=pd.merge(train2,trainx,left_index=True,right_index=True)
    feature=['wificount','category_id1','price1','away','wificount1','wificount2','wificount4','count1','count2','count3','hourco','wifimean','wifisum','isweekend']
    feature.extend(column1)
    train3=train2[train2.shop_id.notnull()]
    test=train2[train2.shop_id.isnull()]
    train3["label"]=(train3.shop_id==train3.shop_id1)*1
    train4=train3.copy()
    model=xgb.XGBClassifier(max_depth=6,learning_rate=0.1,n_estimators=100)
    params=model.get_xgb_params()
    xgbtrain=xgb.DMatrix(train4[feature],train4.label)
    cvresult=xgb.cv(params,xgbtrain,num_boost_round=1000,nfold=5,metrics="auc",early_stopping_rounds=50)
    print(cvresult)
    model.set_params(n_estimators=cvresult.shape[0])
    model.fit(train4[feature],train4.label)
    test["label"]=model.predict_proba(test[feature])[:,1]
    model=lgb.LGBMClassifier(boosting_type='gbdt', num_leaves=80, max_depth=-1, learning_rate=0.1, n_estimators=10, 
                         max_bin=255, subsample_for_bin=50000, objective="binary", min_split_gain=0.0, min_child_weight=5, 
                         min_child_samples=10, subsample=1.0, subsample_freq=1, colsample_bytree=1.0, reg_alpha=0.0, reg_lambda=0.0, 
                         random_state=0, n_jobs=-1, silent=True)
    params=model.get_params()
    params.pop("n_estimators")
    params.pop("silent")
    params.pop("n_jobs")
    params.pop("random_state")
    lgbtrain=lgb.Dataset(train4[feature].values,train4.label.values.tolist())
    res=lgb.cv(params,lgbtrain,metrics="auc",num_boost_round=1000,nfold=5,early_stopping_rounds=50)
    print(pd.DataFrame(res))
    model.set_params(n_estimators=pd.DataFrame(res).shape[0])
    model.fit(train4[feature],train4.label)
    test["label1"]=model.predict_proba(test[feature])[:,1]
    r=test[['row_id','shop_id1',"label","label1"]]
    r.columns=["row_id","shop_id","label","label1"]
    result=pd.concat([result,r])
    result['row_id']=result['row_id'].astype('int')
    result.to_csv(path+'suba0.csv',index=False)
