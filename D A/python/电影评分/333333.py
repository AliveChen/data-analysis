
import pandas as pd


unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('users.dat',sep='::',header=None,names=unames,engine='python')
rnames=['user_id','movie_id','rating','timestamp']
mnames = ['movie_id', 'title', 'genres']

ratings =pd.read_table('ratings.dat', sep='::', header=None, names=rnames,engine='python')
movies =pd.read_table('movies.dat', sep='::', header=None, names=mnames,engine='python')
#print users[:5]
#print ratings[:4]
#print movies[:6]
#�ϲ��ļ�
data=pd.merge(pd.merge(ratings,users),movies)
#print data
print data.ix[0]
#͸�ӱ�index�У�columns�У�aggfuncֵ
mean_ratings=data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')
#print mean_ratings[:5]
#��������࣬��size�Ű���С
rating_by_title=data.groupby('title').size()
print rating_by_title[:10]
#ֻ������250���������ϵĵ�Ӱ
active_titles=rating_by_title.index[rating_by_title >=250]
print active_titles
#�������к����������ݴ���250���ĵ�Ӱ���ݣ�Ȼ�����ǾͿ��Ծݴ˴�ǰ���mean_ratingѡȡ������
mean_ratings=mean_ratings.ix[active_titles]
print mean_ratings
#Ϊ���˽�Ů�Թ�����ϲ���ĵ�Ӱ
top_female_ratings=mean_ratings.sort_index(by='F',ascending=False)
#  print top_female_ratings[:10]
#������Ůrating��ֵ
mean_ratings['diff']=mean_ratings['M']-mean_ratings['F']
print mean_ratings[:5]
sorted_by_diff=mean_ratings.sort_index(by='diff')

