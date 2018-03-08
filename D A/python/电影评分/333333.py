
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
#合并文件
data=pd.merge(pd.merge(ratings,users),movies)
#print data
print data.ix[0]
#透视表index行，columns列，aggfunc值
mean_ratings=data.pivot_table('rating',index='title',columns='gender',aggfunc='mean')
#print mean_ratings[:5]
#按标题分类，用size排包大小
rating_by_title=data.groupby('title').size()
print rating_by_title[:10]
#只保留有250个评价以上的电影
active_titles=rating_by_title.index[rating_by_title >=250]
print active_titles
#该索引中含有评分数据大于250条的电影数据，然后我们就可以据此从前面的mean_rating选取所需行
mean_ratings=mean_ratings.ix[active_titles]
print mean_ratings
#为了了解女性观众最喜欢的电影
top_female_ratings=mean_ratings.sort_index(by='F',ascending=False)
#  print top_female_ratings[:10]
#计算男女rating差值
mean_ratings['diff']=mean_ratings['M']-mean_ratings['F']
print mean_ratings[:5]
sorted_by_diff=mean_ratings.sort_index(by='diff')

