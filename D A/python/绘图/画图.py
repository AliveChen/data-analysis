#coding=utf-8
import matplotlib.pyplot as plt
#画饼图
labels=[u'我那个','kk','kk','zhaowu']#标签
sizes=[15,30,45,10]#标签占比
explode=(0,0.1,0,0)#将某个部分分离出来

plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',
        shadow=False,startangle=90)
#保留一位小数，阴影，起始角度为90度
plt.axis('equal')#xy轴刻度一致，才是圆形
plt.title('bingtu')
plt.show()

#画直方图
import numpy as np

np.random.seed(0)   #每次生成的随即数都相同
mu , sigma = 100,20    #均值和标准差
a = np.random.normal(mu,sigma,size=100)    #给出均值为mean，标准差为stdev的高斯随机数（场），当size赋值时，例如：size=100，表示返回100个高斯随机数。

plt.hist(a,10,histtype='stepfilled',facecolor='b',alpha=0.75)   #10是直方图的个数
plt.title('Histogram')  #标题
plt.show()

import numpy as np
#画坐标图

N = 20
theta = np.linspace(0.0, 2 * np.pi, N , endpoint=False)
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

ax = plt.subplot(111,projection='polar')
bars = ax.bar(theta,radii,width=width,bottom=0.0)

for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)
plt.show()


#
import numpy as np
import matplotlib.pyplot as plt

fig , ax = plt.subplots()
ax.plot(10*np.random.rand(100),10*np.random.rand(100),'o')
ax.set_title('Simple Scatter')
plt.show()
