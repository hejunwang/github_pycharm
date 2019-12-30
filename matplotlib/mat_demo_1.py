#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: mat_demo_1.py
@time: 2019/12/27 17:51
@desc:
'''

'''
绘制 10点到12点之间的每一份中的气温图     demo_1 
'''

from matplotlib import pyplot as plt
import  random
a = [random.randint(20,35) for i  in range(120)]
x = range(120)

p = plt.figure(figsize=(10,6),dpi=80)
plt.plot(x,a)      #导入x轴和y轴的数据  形成图形

'设置x轴的时间 ,分钟数 '
_x = list(x)[::3]    #设置x轴刻度的步长,这里总的数据要和a的数据大小是一样的
_xticks = ['10:{}'.format(i) for i in range(60)]     #这里的列表的是对应关系的
_xticks += ['11:{}'.format(i) for i in range(60)]     #这里的列表的是对应关系的

#取步长,数字和字符串形成一一对应的关系 ,数据的长度一样  ,rotation 旋转的度数
plt.xticks(_x,_xticks[::3],rotation =45)      #设置x轴的刻度 ,参数是两个的时间, 要和前面的x对应,文字密度大可以使用旋转

#添加描述信息
plt.xlabel('time')
plt.ylabel('temp °')
plt.title('10:00--12:00 every time temp')


plt.show()        #展示图形




