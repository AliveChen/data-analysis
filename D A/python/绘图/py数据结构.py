#coding=utf-8
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#numpy 的基础操作
a=np.array([2,0,1,5])
print a
print a[:3]
print a.min()
a.sort()
b=np.array([[1,2,3],[4,5,6]])
print b*b

# matplotlib
x=np.linspace(0,10,100) #作图的变量自变量
y=np.sin(x)+1
z=np.cos(x**2)+1
plt.figure(figsize=(8,4))
plt.plot(x,y,label='$\sin x+1$',color='red',linewidth=2)#作图，设置标签线条颜色线条大小
plt.plot(x,z,'b--',label='$\cos x^2+1$')#作图，设置标签，线条类型
plt.xlabel('Time(s)') #xzhou name
plt.ylabel('Volt')#yzhou name
plt.title('A simple example') #标题
plt.ylim(0,2.2)# 显示的y轴范围
plt.legend() # 显示图例
plt.show()  # 显示作图结果


#pandas

catering_sale='demo/data/catering_sale.xls' #此处不能用open，格式会变，下方excel不对应
data=pd.read_excel(catering_sale,index_col=u'日期')#（index_col是抬一行的列名称，如果没有列名称，加name）
print data.describe()
print len(data)
#绘箱图
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure()
p=data.boxplot(return_type='dict')
x=p['fliers'][0].get_xdata()
y=p['fliers'][0].get_ydata()
y.sort()

for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05-0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
plt.show()

statistics=data.describe()
statistics.loc['range']=statistics.loc['max']-statistics.loc['min']
statistics.loc['var']=statistics.loc['std']/statistics.loc['mean']
statistics.loc['dis']=statistics.loc['75%']-statistics.loc['25%']
print statistics
#帕累托图

dish_profit='demo/data/catering_dish_profit.xls'
data=pd.read_excel(dish_profit,index_col=u'菜品名')
print data
data=data[u'盈利'].copy()
print type(data)

data=pd.Series(sorted(data,reverse=True))
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False
plt.figure()
data.plot(kind='bar')
plt.ylabel(u'yingliyuan')
p=1.0*data.cumsum()/data.sum()
p.plot(color='r',secondary_y=True,style='-o',linewidth=2)
plt.annotate(format(p[6],'.4%'),xy=(6,p[6]),xytext=(6*0.9,p[6]*0.9),arrowprops=dict(arrowstyle='->',connectionstyle='arc3,rad=.2'))
plt.ylabel(u'盈利（比例）')
plt.show()
#相关系数矩阵
catering_sale = 'demo/data/catering_sale_all.xls' #餐饮数据，含有其他属性
data = pd.read_excel(catering_sale, index_col = u'日期') #读取数据，指定“日期”列为索引列

data.corr() #相关系数矩阵，即给出了任意两款菜式之间的相关系数
print data.corr()[u'百合酱蒸凤爪'] #只显示“百合酱蒸凤爪”与其他菜式的相关系数
data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺']) #计算“百合酱蒸凤爪”与“翡翠蒸香茜饺”的相关系数

#绘制一条蓝色正弦曲线
x=np.linspace(0,2*np.pi,50)
y=np.sin(x)
plt.plot(x,y,'bp--')
plt.show()
'''

#绘制一个饼形图
labels=['frogs','hogs','Dogs','logs']
sizes=[15,30,45,10]
colors=['yellowgreen','gold','lightskyblue','lightcoral']
explode=(0,0.1,0,0)
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.show()
