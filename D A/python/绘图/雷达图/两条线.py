
'''
matplotlib雷达图
'''
import numpy as np
import matplotlib.pyplot as plt
 
#=======自己设置开始============
#标签
labels = np.array(['A','I','R','C','E'])
#数据个数
dataLenth = 5
#数据
data = np.array([1,4,3,6,4])
data1= np.array([2,4,3,1,3])
#========自己设置结束============
 
angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False)
data = np.concatenate((data, [data[0]])) # 闭合
data1 = np.concatenate((data1, [data1[0]]))
angles = np.concatenate((angles, [angles[0]])) # 闭合
 
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, data, 'bo-', linewidth=2)

ax.plot(angles, data1,'--',linewidth=2)
ax.set_thetagrids(angles * 180/np.pi, labels)
ax.set_title("matplotlib", va='bottom')
ax.grid(True)
plt.show()
