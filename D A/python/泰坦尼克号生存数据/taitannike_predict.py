#coding=utf-8
import pandas as pd

data =pd.read_csv('data/titanic_train.csv')
print data.info()
#print data.describe()
print data.columns



import matplotlib.pyplot as plt

fig = plt.figure()
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
fig.set(alpha=0.2)  # 设定图表颜色alpha参数
plt.subplot2grid((2,3),(0,0))             # 在一张大图里分列几个小图
data['Survived'].value_counts().plot(kind='bar')# 柱状图 
plt.title(u"获救情况 (1为获救)") # 标题
plt.ylabel(u"人数")

plt.subplot2grid((2,3),(0,1))
data['Pclass'].value_counts().plot(kind="bar")
plt.ylabel(u"人数")
plt.title(u"乘客等级分布")

plt.subplot2grid((2,3),(0,2))
plt.scatter(data.Survived, data.Age)#散点
plt.ylabel(u"年龄")                         # 设定纵坐标名称
plt.grid(b=True, which='major', axis='y') 
plt.title(u"按年龄看获救分布 (1为获救)")

plt.subplot2grid((2,3),(1,0), colspan=2)
data.Age[data.Pclass == 1].plot(kind='kde')   
data.Age[data.Pclass == 2].plot(kind='kde')
data.Age[data.Pclass == 3].plot(kind='kde')
plt.xlabel(u"年龄")# plots an axis lable
plt.ylabel(u"密度") 
plt.title(u"各等级的乘客年龄分布")
plt.legend((u'头等舱', u'2等舱',u'3等舱'),loc='best') # sets our legend for our graph.

plt.subplot2grid((2,3),(1,2))
data.Embarked.value_counts().plot(kind='bar')
plt.title(u"各登船口岸上船人数")
plt.ylabel(u"人数")

plt.show()

#看看各乘客等级的获救情况

fig = plt.figure()

fig.set(alpha=0.2)# 设定图表颜色alpha参数

Survived_0 = data.Pclass[data.Survived == 0].value_counts()

Survived_1 = data.Pclass[data.Survived == 1].value_counts()

df=pd.DataFrame({u'获救':Survived_1, u'未获救':Survived_0})

df.plot(kind='bar', stacked=True)#stacked表示堆积或者并列

plt.title(u'各乘客等级的获救情况')

plt.xlabel(u'乘客等级')

plt.ylabel(u'人数')
plt.show()

#查看各性别的的获救情况
fig=plt.figure()
fig.set(alpha=0.2)
survived_0=data['Sex'][data['Survived']==0].value_counts()
survived_1=data['Sex'][data['Survived']==1].value_counts()
df=pd.DataFrame({u'获救':survived_0,u'未获救':survived_1})
df.plot(kind='bar',stacked=True)
plt.title(u'各乘客性别的获救情况')
plt.xlabel(u'乘客性别')
plt.ylabel(u'人数')
plt.show()

 #然后我们再来看看各种舱级别情况下各性别的获救情况
fig=plt.figure()
fig.set(alpha=0.65) # 设置图像透明度，无所谓
plt.title(u"根据舱等级和性别的获救情况")

ax1=fig.add_subplot(141)
data.Survived[data.Sex == 'female'][data.Pclass != 3].value_counts().plot(kind='bar', label="female highclass", color='#FA2479')
ax1.set_xticklabels([u"获救", u"未获救"], rotation=0)
ax1.legend([u"女性/高级舱"], loc='best')

ax2=fig.add_subplot(142, sharey=ax1)
data.Survived[data.Sex == 'female'][data.Pclass == 3].value_counts().plot(kind='bar', label='female, low class', color='pink')
ax2.set_xticklabels([u"未获救", u"获救"], rotation=0)
plt.legend([u"女性/低级舱"], loc='best')

ax3=fig.add_subplot(143, sharey=ax1)
data.Survived[data.Sex == 'male'][data.Pclass != 3].value_counts().plot(kind='bar', label='male, high class',color='lightblue')
ax3.set_xticklabels([u"未获救", u"获救"], rotation=0)
plt.legend([u"男性/高级舱"], loc='best')

ax4=fig.add_subplot(144, sharey=ax1)
data.Survived[data.Sex == 'male'][data.Pclass == 3].value_counts().plot(kind='bar', label='male low class', color='steelblue')
ax4.set_xticklabels([u"未获救", u"获救"], rotation=0)
plt.legend([u"男性/低级舱"], loc='best')

plt.show()

#登仓口的情况
fig = plt.figure()
fig.set(alpha=0.2)  # 设定图表颜色alpha参数

Survived_0 = data.Embarked[data.Survived == 0].value_counts()
Survived_1 = data.Embarked[data.Survived == 1].value_counts()
df=pd.DataFrame({u'获救':Survived_1, u'未获救':Survived_0})
df.plot(kind='bar', stacked=True)
plt.title(u"各登录港口乘客的获救情况")
plt.xlabel(u"登录港口") 
plt.ylabel(u"人数") 

plt.show()

g = data.groupby(['SibSp','Survived'])
df = pd.DataFrame(g.count()['PassengerId'])
print df
