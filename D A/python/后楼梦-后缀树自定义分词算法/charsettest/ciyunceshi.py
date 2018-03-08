#coding:utf-8

import jieba


stopwords = {}
isCN = 1 #默认启用中文分词




text_from_file_with_apath = open('content2.txt').read()

#通过jieba分词进行分词并通过空格分隔

text_path='content2.txt'
stopwords_path='stoplist.txt'

text = open('content2.txt').read()
print text
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
print 'fenge-------'
print text

aaa=open('test.txt','w')
aaa.write(text.encode('utf-8'))
