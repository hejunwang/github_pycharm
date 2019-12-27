#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: matp_1.py
@time: 2019/12/11 9:24
@desc:
'''

'''
matplotlib 主要是数据的可视化图标 ,x轴和y轴的数据一定是一对一的  ,只需要选择相应的x轴的数据和y轴的数据 
使用方法即可 
'''
# demo 1
# 每隔两个小时的气温,展示在图形上
from matplotlib import pyplot as plt
import numpy as np

y = [12,3,25,5,2,12,12,4,6,4,6,7]           # 随机的气温值
x = np.arange(2,26,2)
print(x)

plt.figure(figsize=(11,5),dpi=80)           #设置图片的大小

#绘图
plt.plot(x,y)                               #默认matplotlib设置的x轴和y轴

#手动设置x轴,来调整x轴的密集度 , xticks 设置x轴的密集度  yticks 设置y轴的密集度
# plt.xticks(x)
plt.xticks(range(1,25))       #设置x轴的设置

#保存
# plt.savefig('./new_mat.png')
plt.savefig('./new_mat.svg')    #也可以使用矢量图的方式保存 .svg 的方式,放大不会失真
#展示图片
plt.show()



