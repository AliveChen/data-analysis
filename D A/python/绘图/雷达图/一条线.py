#coding=utf-8
#matplotlib雷达图

import numpy as np
import matplotlib.pyplot as plt
 
#=======自己设置开始============
#标签
labels = np.array([u'艺术A',u'调研I',u'实际R',u'常规C',u'企业E',u'社会S'])
#数据个数
dataLenth = 6
#数据
data = np.array([1,4,3,6,4,8])
#========自己设置结束============
 
angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合
 
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'bo-', linewidth=2)
ax.set_thetagrids(angles * 180/np.pi, labels,fontproperties='SimHei')
ax.set_title(u"matplotlib雷达图", va='bottom',fontproperties='SimHei')
ax.grid(True)
plt.show()
