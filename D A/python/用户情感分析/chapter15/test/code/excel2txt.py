#-*- coding: utf-8 -*-
import pandas as pd

inputfile = '../data/huizong.csv' #评论汇总文件
outputfile = '../data/meidi_jd.txt' #评论提取后保存路径
data = pd.read_csv(inputfile, encoding = 'utf-8')
data = data[[u'评论']][data[u'品牌'] == u'美的']
data.to_csv(outputfile, index = False, header = False, encoding = 'utf-8')