#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: mat_demo_2.py
@time: 2019/12/30 13:17
@desc:
'''

'''
1 . 在一定的年龄段 ,交往的女友的个数   12-30岁之间 行程   折线图 
2 .多个人员的时间 ,同时在图上显示出来 
'''
from matplotlib import pyplot as plt

a = [1,0,2,3,4,2,2,1,2,3,4,3,3,2,1,2,1,3]

y1 =[2,0,1,3,3,2,1,2,1,3,2,3,1,1,1,1,1,2]
x =range(12,30)                                #年龄
p = plt.figure(figsize=(8,6),dpi=80)          #图形大小设置

plt.plot(x,a)
plt.plot(x,y1,label='friend')                          #添加了另外一个要画图的对象 , 一个图中两个图形

#设置x轴的刻度
_x_ticks =['{}'.format(i) for i in x]
plt.xticks(x,_x_ticks)         #一一对应

#设置标签
plt.xlabel('AGE years old')
plt.ylabel(' G F count')
plt.title('this is a matplotlib about gf')

#绘制网格 ,alpha设置是网格的透明度
plt.grid(alpha =0.4)
#保存
plt.savefig('./save.png')

#展示
plt.show()




