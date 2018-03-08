#coding:utf-8


import matplotlib.pyplot as plt
from wordcloud import WordCloud,ImageColorGenerator,STOPWORDS
import jieba
import numpy as np
from PIL import Image
from os import path
from scipy.misc import imread


stopwords = {}
isCN = 1 #默认启用中文分词
#读入背景图片
#back_coloring_path = np.array(Image.open("longzutest.jpg"))

back_coloring_path = "longzutest.jpg"
back_coloring = imread(back_coloring_path)
#读取要生成词云的文件
text_from_file_with_apath = open('hlm_x.txt').read()

#通过jieba分词进行分词并通过空格分隔

text_path='hlm_x.txt'
stopwords_path='stoplist.txt'

text = open('hlm_x.txt').read()
def add_word(list):
    for items in list:
        jieba.add_word(items)
my_words_list = [u'开心麻花']

def jiebaclearText(text):
    mywordlist = []
    seg_list = jieba.cut(text, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords_path)
    try:
        f_stop_text = f_stop.read( )
        f_stop_text=unicode(f_stop_text,'utf-8')
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    return ''.join(mywordlist)

if isCN:
    text = jiebaclearText(text)
www=open('jishu2.txt','w')
www.write(text.encode('gbk'))


    
#my_wordcloud = WordCloud().generate(wl_space_split) 默认构造函数
my_wordcloud = WordCloud(
            background_color='white',    # 设置背景颜色
            mask =back_coloring,        # 设置背景图片
            max_words = 2000,            # 设置最大现实的字数
            #stopwords = STOPWORDS,        # 设置停用词
            font_path = 'C:/Users/Windows/fonts/simkai.ttf',# 设置字体格式，如不设置显示不了中文
            max_font_size = 100,            # 设置字体最大值
            random_state = 42,            # 设置有多少种随机生成状态，即有多少种配色方案            
            width=1000, height=860, margin=2,#
                ).generate(text)

# 根据图片生成词云颜色
image_colors = ImageColorGenerator(back_coloring)
#my_wordcloud.recolor(color_func=image_colors)
plt.imshow(my_wordcloud.recolor(color_func=image_colors),cmap=plt.cm.gray)
plt.axis("off")
plt.show()


