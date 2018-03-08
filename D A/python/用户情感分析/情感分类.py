
from snownlp import SnowNLP
import pandas as pd
inputfile='chapter15/out/meidi_jd_process_1.txt'
outputfile='chapter15/out/fenlei.txt'
text=pd.read_csv(inputfile,header=None,encoding='utf-8')

print (text[:5])

text[1]=[SnowNLP(i).sentiments for i in text[0]]

    



print (text[:5])

text.to_excel('dasfcdafc.xls')
