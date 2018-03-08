#coding=utf-8

import pandas as pd
import csv
import numpy as np
'''
#import matplotlib.pyplot as plt
test=pd.read_csv('aftercuttest.csv',header=None,encoding='gbk')
train=pd.read_csv('aftercuttrain.csv',header=None,encoding='gbk')
#total=pd.concat([train,test],axis=0)
#print total
#total.to_csv('jieba_total_cut.csv',index=False,header=False,encoding='utf8')
train.to_csv('after_cuttrain.csv',index=False,header=False,encoding='utf8')
test.to_csv('after_cuttest.csv',index=False,header=False,encoding='utf8')
'''
#w2v=np.load('wv300_win100.test.npy')
#print len(w2v)
data=pd.read_csv('after_cuttest.csv',header=None,encoding='gbk')
print data.shape
data.to_csv('aftercuttest.csv',header=False,index=False,encoding='utf-8')


        





