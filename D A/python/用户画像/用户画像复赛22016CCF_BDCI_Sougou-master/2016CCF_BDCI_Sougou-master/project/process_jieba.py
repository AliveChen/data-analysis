#coding=utf-8
import time
import pandas as pd
import jieba
import jieba.posseg
'''
seg_list = jieba.cut("陶喆下载", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 默认模式

words = jieba.posseg.cut("陶喆下载")
for word, flag in words:
     print('%s %s' % (word, flag))
'''
datapath='train_querylist.csv'
def inputfile(datapath):
    with open(datapath,'r') as f:
    
    
        f=f.readlines()
        count=0
        traindata=[]
        for line in f:
            line=line.strip()
        
            try:
            
                traindata.append(line)
                count+=1
            except:
            
                print('error:',line,count)
    return traindata    
time1=time.clock()
querylist=inputfile(datapath)
print (u'%s'%querylist[0:2])
writepath = 'writefile.csv'
csvfile = open(writepath, 'w')
POS={}
for i in querylist:
    s=[]
    str1=''
    words=jieba.posseg.cut(i)
    allowPOS=['n','v','j']
    for word,flag in words:
        POS[flag]=POS.get(flag,0)+1
        if (flag[0] in allowPOS) and len(word)>=2:
            str1+=word+' '
            s.append(str1.encode('utf-8'))
            csvfile.write(' '.join(s)+'\n')
csvfile.close()
for i in POS:
    print (i)
            
        
        
    
        
            
             

