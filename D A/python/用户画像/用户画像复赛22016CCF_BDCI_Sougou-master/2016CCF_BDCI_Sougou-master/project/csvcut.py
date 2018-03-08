#encoding=utf-8
import pandas as pd
import jieba
import jieba.posseg
import time

'''
cutpath='train_data_querylist.csv'

cutfile=open(cutpath,'r',encoding='utf8')
#print cutfile[0][0]


after_cut_train=open('aftercuttrain.csv','w')
time1=time.clock()

pos={}

for i in cutfile:
    #print (i)
    s=[]
    str1=''
    words=jieba.cut(i)
    for word in words:
        #pos[flag]=pos.get(flag,0)+1
        if len(word)>=2:
            str1+=word+' '
    s.append(str1)
    after_cut_train.write(str1+'\n')

after_cut_train.close
print (pos)

time2=time.clock()
print('total time:%f s'%(time2-time1))

'''    
cutpath='test_data_quesylist.csv'

cutfile=open(cutpath,'r',encoding='utf8')
#print cutfile[0][0]


after_cut_train=open('aftercuttest.csv','w')
time1=time.clock()

pos={}

for i in cutfile:
    #print (i)
    s=[]
    str1=''
    words=jieba.cut(i)
    for word in words:
        #pos[flag]=pos.get(flag,0)+1
        if len(word)>=2:
            str1+=word+' '
    s.append(str1)
    after_cut_train.write(str1+'\n')

after_cut_train.close
print (pos)

time2=time.clock()
print('total time:%f s'%(time2-time1))        
