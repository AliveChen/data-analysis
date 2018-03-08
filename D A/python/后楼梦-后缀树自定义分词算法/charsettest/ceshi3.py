#encoding=utf-8
import re
import chardet

f=u'测试：你好j啊f收到第14回 见面'
f=''.join(f.split('j'))
f
print type(f)
print (f)


a=re.sub(u"第.{1,5}回", '', f)
#a=f.replace(u"第.{1,5}回",'')
'''

def str_replace_re(string, str_from, str_to=""):
    """
    Replace str_from with str_to in string.
    str_from can be an re-expression.
    """
    return re.sub(str_from, str_to, string)
f=str_replace_re(f,"第.{1,5}回")
'''

print (a)

#g=open('test2.txt','w')
#g.write(f)
