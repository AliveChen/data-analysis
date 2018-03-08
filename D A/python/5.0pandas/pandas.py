Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> pop={'nevada':{2001:2.2,2002:2.3},'ohio':{2000:22,2002}}
SyntaxError: invalid syntax
>>>  pop={'nevada':{2001:2.2,2002:2.3},'ohio':{2000:22,2002:25}}
 
  File "<pyshell#1>", line 2
    pop={'nevada':{2001:2.2,2002:2.3},'ohio':{2000:22,2002:25}}
    ^
IndentationError: unexpected indent
>>> pop={'nevada':{2001:2.2,2002:2.3},'ohio':{2000:22,2002:25}}
>>> frame3=DataFrame(pop)

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    frame3=DataFrame(pop)
NameError: name 'DataFrame' is not defined
>>> import pandas
>>> frame3=pandas.DataFrame(pop)
>>> frame3
      nevada  ohio
2000     NaN  22.0
2001     2.2   NaN
2002     2.3  25.0
>>> frame3.T
        2000  2001  2002
nevada   NaN   2.2   2.3
ohio    22.0   NaN  25.0
>>> frame.values

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    frame.values
NameError: name 'frame' is not defined
>>> frame3.values
array([[  nan,  22. ],
       [  2.2,   nan],
       [  2.3,  25. ]])
>>> frame3.index.name='year';frame3.columns.name='state'
>>> frame3
state  nevada  ohio
year               
2000      NaN  22.0
2001      2.2   NaN
2002      2.3  25.0
>>> frame3.index
Int64Index([2000, 2001, 2002], dtype='int64', name=u'year')
>>> frame3.columns
Index([u'nevada', u'ohio'], dtype='object', name=u'state')
>>> 'nevada' in frame3.columns
True
>>> # ÏòÏÂÌî³ä
>>> obj4=pandas.Series(['blue','purple','yellow'],index=[0,2,4])
>>> obj4.reindex(range(6),method='ffill')
0      blue
1      blue
2    purple
3    purple
4    yellow
5    yellow
dtype: object
>>> 
