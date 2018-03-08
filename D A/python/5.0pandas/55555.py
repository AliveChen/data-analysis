Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:53:40) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import pandas as pa
impo
>>> import pandas as pd
>>> import numpy as np
>>> frame=DateFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=['d','a','b','c'])

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    frame=DateFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=['d','a','b','c'])
NameError: name 'DateFrame' is not defined
>>> frame=pd.DateFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=['d','a','b','c'])

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    frame=pd.DateFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=['d','a','b','c'])
AttributeError: 'module' object has no attribute 'DateFrame'
>>>  frame=pd.DataFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=['d','a','b','c'])
 
  File "<pyshell#8>", line 2
    frame=pd.DataFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=['d','a','b','c'])
    ^
IndentationError: unexpected indent
>>> frame=pd.DataFrame(np.arange(8).reshape(2,4),index=['three','one'],columns=['d','a','b','c'])
>>> frame.sort_index()
       d  a  b  c
one    4  5  6  7
three  0  1  2  3
>>> frame.sort_index()
       d  a  b  c
one    4  5  6  7
three  0  1  2  3
>>> frame.sort_index(axis=1)
       a  b  c  d
three  1  2  3  0
one    5  6  7  4
>>> obj=pd.Series([4,7,-3,2])
>>> obj.order()

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    obj.order()
  File "C:\Python27\lib\site-packages\pandas\core\generic.py", line 3081, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'order'
>>> frame=pd.DataFrame({'b':[4,7,-3,2],'a'=[0,1,0,1]})
SyntaxError: invalid syntax
>>> frame=pd.DataFrame({'b':[4,7,-3,2],'a'=[0,1,0,1]})
SyntaxError: invalid syntax
>>> frame=pd.DataFrame({'b':[4,7,-3,2],'a':[0,1,0,1]})
>>> frame
   a  b
0  0  4
1  1  7
2  0 -3
3  1  2
>>> frame.sort_index(by='b')

Warning (from warnings module):
  File "__main__", line 2
FutureWarning: by argument to sort_index is deprecated, pls use .sort_values(by=...)
   a  b
2  0 -3
3  1  2
0  0  4
1  1  7
>>> frame.sort_index(by=['a','b'])
   a  b
2  0 -3
0  0  4
3  1  2
1  1  7
>>> obj=pd.Series([7,-5,7,4,2,0,4])
>>> obj
0    7
1   -5
2    7
3    4
4    2
5    0
6    4
dtype: int64
>>> obj.rank()
0    6.5
1    1.0
2    6.5
3    4.5
4    3.0
5    2.0
6    4.5
dtype: float64
>>> obj
0    7
1   -5
2    7
3    4
4    2
5    0
6    4
dtype: int64
>>> obj.rank(method='first')
0    6.0
1    1.0
2    7.0
3    4.0
4    3.0
5    2.0
6    5.0
dtype: float64
>>> obj=pd.Series(range(5),index=['a','a','b','b','c'])
>>> obj
a    0
a    1
b    2
b    3
c    4
dtype: int64
>>> obj.index.is_unique
False
>>> obj['a']
a    0
a    1
dtype: int64
>>> dtype: int64
SyntaxError: invalid syntax
>>> df=ps.DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])

Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    df=ps.DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])
NameError: name 'ps' is not defined
>>> df=pd.DataFrame([[1.4,np.nan],[7.1,-4.5],[np.nan,np.nan],[0.75,-1.3]],index=['a','b','c','d'],columns=['one','two'])
>>> df
    one  two
a  1.40  NaN
b  7.10 -4.5
c   NaN  NaN
d  0.75 -1.3
>>> df.sum()
one    9.25
two   -5.80
dtype: float64
>>> df.sum(axis)

Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    df.sum(axis)
NameError: name 'axis' is not defined
>>> df.sum(axis=1)
a    1.40
b    2.60
c     NaN
d   -0.55
dtype: float64
>>> df.idxmax()
one    b
two    d
dtype: object
>>> df.idxmax(axis=1)
a    one
b    one
c    NaN
d    one
dtype: object
>>> df.describe()
            one       two
count  3.000000  2.000000
mean   3.083333 -2.900000
std    3.493685  2.262742
min    0.750000 -4.500000
25%    1.075000 -3.700000
50%    1.400000 -2.900000
75%    4.250000 -2.100000
max    7.100000 -1.300000
>>> 
>>> import pandas.io.data as web

Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    import pandas.io.data as web
  File "C:\Python27\lib\site-packages\pandas\io\data.py", line 2, in <module>
    "The pandas.io.data module is moved to a separate package "
ImportError: The pandas.io.data module is moved to a separate package (pandas-datareader). After installing the pandas-datareader package (https://github.com/pydata/pandas-datareader), you can change the import ``from pandas.io import data, wb`` to ``from pandas_datareader import data, wb``.
>>> obj=pd.Series(['c','a','d','a','a','b','c','c'])
>>> unique=obj.unique()
>>> unique
array(['c', 'a', 'd', 'b'], dtype=object)
>>> obj.value_counts()
c    3
a    3
d    1
b    1
dtype: int64
>>> pd.value_counts(obj.values,sort=False_)

Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    pd.value_counts(obj.values,sort=False_)
NameError: name 'False_' is not defined
>>> pd.value_counts(obj.values,sort=False)
a    3
c    3
b    1
d    1
dtype: int64
>>> from numpy import nan as NA
>>> data=pd.Series([1,NA,3.5,NA,7])
>>> data
0    1.0
1    NaN
2    3.5
3    NaN
4    7.0
dtype: float64
>>> data.dropna()
0    1.0
2    3.5
4    7.0
dtype: float64
>>> data
0    1.0
1    NaN
2    3.5
3    NaN
4    7.0
dtype: float64
>>> data[data.notnull()]
0    1.0
2    3.5
4    7.0
dtype: float64
>>> df=pd.DataFrame(np.random.randn(7,3))
>>> df
          0         1         2
0 -1.595077 -1.057471  1.489327
1  0.159008  0.892989 -0.740484
2  0.509428  0.035218  0.417744
3  0.884586 -0.019892 -0.085873
4  0.144830  0.907465  1.274998
5  0.033852  0.185952  1.476906
6 -0.179276 -1.052364 -1.185115
>>> df.ix[:4,1]=NA;df.ix[:2,2]=NA
>>> df
          0         1         2
0 -1.595077       NaN       NaN
1  0.159008       NaN       NaN
2  0.509428       NaN       NaN
3  0.884586       NaN -0.085873
4  0.144830       NaN  1.274998
5  0.033852  0.185952  1.476906
6 -0.179276 -1.052364 -1.185115
>>> df.dropna(thresh=3)
          0         1         2
5  0.033852  0.185952  1.476906
6 -0.179276 -1.052364 -1.185115
>>> df.fillna(0)
          0         1         2
0 -1.595077  0.000000  0.000000
1  0.159008  0.000000  0.000000
2  0.509428  0.000000  0.000000
3  0.884586  0.000000 -0.085873
4  0.144830  0.000000  1.274998
5  0.033852  0.185952  1.476906
6 -0.179276 -1.052364 -1.185115
>>> df.
SyntaxError: invalid syntax
>>> df.fillna({1:0.5,3:-1})
          0         1         2
0 -1.595077  0.500000       NaN
1  0.159008  0.500000       NaN
2  0.509428  0.500000       NaN
3  0.884586  0.500000 -0.085873
4  0.144830  0.500000  1.274998
5  0.033852  0.185952  1.476906
6 -0.179276 -1.052364 -1.185115
>>> 
>>> data=pd.Series(np.random.randn(10),index=[['a','a','a','b','b','b','c','c','d','d'],[1,2,3,1,2,3,1,2,3,3]])
>>> data
a  1   -0.987488
   2   -1.327619
   3    1.602221
b  1   -0.748035
   2    0.336774
   3   -0.706287
c  1    0.761155
   2    0.945324
d  3    0.846502
   3   -0.051424
dtype: float64
>>> data.index
MultiIndex(levels=[[u'a', u'b', u'c', u'd'], [1, 2, 3]],
           labels=[[0, 0, 0, 1, 1, 1, 2, 2, 3, 3], [0, 1, 2, 0, 1, 2, 0, 1, 2, 2]])
>>> data['b']
1   -0.748035
2    0.336774
3   -0.706287
dtype: float64
>>> data['b','d']

Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    data['b','d']
  File "C:\Python27\lib\site-packages\pandas\core\series.py", line 642, in __getitem__
    return self._get_with(key)
  File "C:\Python27\lib\site-packages\pandas\core\series.py", line 655, in _get_with
    return self._get_values_tuple(key)
  File "C:\Python27\lib\site-packages\pandas\core\series.py", line 703, in _get_values_tuple
    indexer, new_index = self.index.get_loc_level(key)
  File "C:\Python27\lib\site-packages\pandas\core\indexes\multi.py", line 2132, in get_loc_level
    return partial_selection(key)
  File "C:\Python27\lib\site-packages\pandas\core\indexes\multi.py", line 2099, in partial_selection
    indexer = self.get_loc(key)
  File "C:\Python27\lib\site-packages\pandas\core\indexes\multi.py", line 2009, in get_loc
    if lead_key else (0, len(self)))
  File "C:\Python27\lib\site-packages\pandas\core\indexes\multi.py", line 1914, in slice_locs
    return super(MultiIndex, self).slice_locs(start, end, step, kind=kind)
  File "C:\Python27\lib\site-packages\pandas\core\indexes\base.py", line 3538, in slice_locs
    start_slice = self.get_slice_bound(start, 'left', kind)
  File "C:\Python27\lib\site-packages\pandas\core\indexes\multi.py", line 1885, in get_slice_bound
    return self._partial_tup_index(label, side=side)
  File "C:\Python27\lib\site-packages\pandas\core\indexes\multi.py", line 1931, in _partial_tup_index
    raise TypeError('Level type mismatch: %s' % lab)
TypeError: Level type mismatch: d
>>> type ch06/
