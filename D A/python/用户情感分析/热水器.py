#coding=utf-8
import pandas as pd



inputfile='chapter15/out/meidi_jd_process_1.txt'
outputfile='chapter15/out/fenlei.txt'
text=pd.read_csv(inputfile,encoding='utf-8',header=None)


#text0=text.iloc[:,0]
#text1=[i.decode('utf-8') for i in text0]

#from snownlp import sentiment
#sentiment.train('C:\Python27\Lib\site-packages\snownlp\sentiment\neg.txt',
               # 'C:\Python27\Lib\site-packages\snownlp\sentiment\pos.txt')
#sentiment.sava('chapter15/out/sentiment.marshal')
#text[0]=unicode(text[0])

lambda p: SnowNLP(p).sentiments

bbb=[]
from snownlp import SnowNLP

qgfl=lambda p: SnowNLP(p).sentiments
data=text[0].apply(qgfl)
print data[:10]


'''
senti=[SnowNLP(i).sentiments for i in text[0]]
print senti[:10]
newsenti=[]
for i in senti:
    if (i>=0.6):
        newsenti.append(1)
    else:
        newsenti.append(-1)
text['predict']=newsenti
text.to_csv(outputfile,index=False,header=False,encoding='utf-8')

'''

