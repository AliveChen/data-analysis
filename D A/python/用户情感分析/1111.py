#coding=utf-8


import pandas as pd

inputfile='chapter15/demo/data/huizong.csv'
outputfile='chapter15/out/meidi_jd.txt'
'''
data=pd.read_csv(inputfile,encoding='utf-8')
data=data[[u'评论']][data[u'品牌']==u'美的']
data.to_csv(outputfile,index=False,header=False)

inputfile=outputfile
outputfile='chapter15/out/meidi_jd_process_1.txt'
data=pd.read_csv(inputfile,encoding='utf-8',header=None)
print type(data)
len11=len(data)
data=pd.DataFrame(data[0].unique())
print type(data)
len12=len(data)

#data.to_csv(outputfile,index=False,header=False,encoding='utf-8')
a=len11-len12

print u'删除了条数评论%d' %a


#参数初始化
inputfile1 = u'chapter15/out/1111/meidi_jd_process_end_负面情感结果.txt'
inputfile2 = u'chapter15/out/1111//meidi_jd_process_end_正面情感结果.txt'
outputfile1 = 'chapter15/out/meidi_jd_neg.txt'
outputfile2 = 'chapter15/out/meidi_jd_pos.txt'

data1 = pd.read_csv(inputfile1, encoding = 'utf-8', header = None) #读入数据
data2 = pd.read_csv(inputfile2, encoding = 'utf-8', header = None)

data1 = pd.DataFrame(data1[0].str.replace('.*?\d+?\\t ', '')) #用正则表达式修改数据
data2 = pd.DataFrame(data2[0].str.replace('.*?\d+?\\t ', ''))

data1.to_csv(outputfile1, index = False, header = False, encoding = 'utf-8') #保存结果
data2.to_csv(outputfile2, index = False, header = False, encoding = 'utf-8')

#-*- coding: utf-8 -*-
import pandas as pd
import jieba #导入结巴分词，需要自行下载安装

#参数初始化
inputfile1 = 'chapter15/out/meidi_jd_neg.txt'
inputfile2 = 'chapter15/out/meidi_jd_pos.txt'
outputfile1 = 'chapter15/out/1111/meidi_jd_neg_cut.txt'
outputfile2 = 'chapter15/out/1111/meidi_jd_pos_cut.txt'

data1 = pd.read_csv(inputfile1, encoding = 'utf-8', header = None) #读入数据
data2 = pd.read_csv(inputfile2, encoding = 'utf-8', header = None)

mycut = lambda s: ' '.join(jieba.cut(s)) #自定义简单分词函数
data1 = data1[0].apply(mycut) #通过“广播”形式分词，加快速度。
data2 = data2[0].apply(mycut)

data1.to_csv(outputfile1, index = False, header = False, encoding = 'utf-8') #保存结果
data2.to_csv(outputfile2, index = False, header = False, encoding = 'utf-8')
'''
#-*- coding: utf-8 -*-
import pandas as pd

#参数初始化
negfile = 'chapter15/out/1111/meidi_jd_neg_cut.txt'
posfile = 'chapter15/out/1111/meidi_jd_pos_cut.txt'
stoplist = 'chapter15/out/1111/stoplist.txt'

neg = pd.read_csv(negfile, encoding = 'utf-8', header = None) #读入数据
pos = pd.read_csv(posfile, encoding = 'utf-8', header = None)
stop = pd.read_csv(stoplist, encoding = 'utf-8', header = None, sep = 'tipdm',engine='python')
#sep设置分割词，由于csv默认以半角逗号为分割词，而该词恰好在停用词表中，因此会导致读取出错
#所以解决办法是手动设置一个不存在的分割词，如tipdm。
stop = [' ', ''] + list(stop[0]) #Pandas自动过滤了空格符，这里手动添加

neg[1] = neg[0].apply(lambda s: s.split(' ')) #定义一个分割函数，然后用apply广播
neg[2] = neg[1].apply(lambda x: [i for i in x if i not in stop]) #逐词判断是否停用词，思路同上
pos[1] = pos[0].apply(lambda s: s.split(' '))
pos[2] = pos[1].apply(lambda x: [i for i in x if i not in stop])

from gensim import corpora, models

#负面主题分析
neg_dict = corpora.Dictionary(neg[2]) #建立词典
neg_corpus = [neg_dict.doc2bow(i) for i in neg[2]] #建立语料库
neg_lda = models.LdaModel(neg_corpus, num_topics = 3, id2word = neg_dict) #LDA模型训练
for i in range(3):
  print(neg_lda.print_topic(i)) #输出每个主题

#正面主题分析
pos_dict = corpora.Dictionary(pos[2])
pos_corpus = [pos_dict.doc2bow(i) for i in pos[2]]
pos_lda = models.LdaModel(pos_corpus, num_topics = 3, id2word = pos_dict)
for i in range(3):
  print(neg_lda.print_topic(i)) #输出每个主题


