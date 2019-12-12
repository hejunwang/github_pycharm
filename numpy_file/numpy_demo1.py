#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: numpy_demo1.py
@time: 2019/12/2 13:10
@desc:
'''

import numpy
#1 添加的一般都是数组, 多个数组
a = numpy.array([1,2,3,5])    #必须是相同的结构
a1 = numpy.array([1,2,3,5.0])    #必须是相同的类型,会自动的都会变成float
print(a)
print(a1)
print(a[0:3])
#2
t1 = numpy.array(range(1,8))
print(t1)
print(type(t1))    #<class 'numpy.ndarray'>
# 3
t3 = numpy.arange(4,10)    #快速的生成数组
print(t3)
print(t3.dtype)       #  int32  数据类型

#4   手动指定的数据类型 使用dtype =  u4 ,u8  ,bool
t4 = numpy.array(range(1,5),dtype='u8')
print(t4)
print(t4.dtype)

#调整数据类型
t5 = t4.astype('int8')
print(t5)
print(t5.dtype)

#numpy中的小数
import random
t6 = numpy.array([random.random() for i in range(10)])
print(t6)
print(t6.dtype)
# [0.79802288 0.07585117 0.7597767  0.97743146 0.00404919 0.58022539
#  0.58916919 0.82121573 0.80812125 0.37727706]
# float64
#如果要保留2位小数  print(round(random.random(),2))
t7 =numpy.round(t6,2)
print(t7)

#切片
vect = numpy.array([5,3,90,12,23])
print(vect[:3])                 #左闭右开

matrix =numpy.array([[1,4,6],
                     [2,4,5],
                     [34,23,45]])
matrix.sort()                     #排序
print(matrix[:,0:2])              #取所有数据的前两列,这是多维的切片

'''
数组的计算
'''
print('-----数组的计算-----')
#shape  查看数组的形状
a1 = numpy.array([1,2,34,4,5,7])
print(a1.shape)     #(6,)     一维数组

a2 = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(a2)
print(a2.shape)     #(3, 3)
# shape 的到的结果 里面有几个数据就是几纬的 ,比如这个是 2纬的 ,如果shape得到的是3个的数值的,就是3纬的

#重新定义数据的形状  reshape
print(a1.reshape(2,3))    #定义 a1 变成一个2行 3列 的形状
print(a2.reshape(9))  #把a2 重新定义成了一个一维数组

a3 =numpy.arange(24).reshape(2,3,4)    #把这24个数据,重新定义成一个 三维数组  ,2 是块数,
print(a3)
print(a3.reshape(4,6))     # 把生成的数据 又一次进行了形状的改变,这是二维的数组,里面有两个参数
print(a3.reshape((24,1)))    #这也是一个 24行1列
print(a3.reshape((1,24)))    #这也是一个 一行24个   , 把数组转化成一个1纬度数据

#
print(a3.flatten())    #把a3 展开 ,二维的方法 转化成一维数组

#数组计算  + - * /
#<1>  数组和数值进行计算
print(a3+2)
print(a3-1)
print(a3*4)
print(a3/0)

'''   a3/0 的结果     nan 是0/0的结果 ,inf(无限无穷的意思) 是  数字/0的结果
[[[nan inf inf inf]
  [inf inf inf inf]
  [inf inf inf inf]]

 [[inf inf inf inf]
  [inf inf inf inf]
  [inf inf inf inf]]]

'''
#数组和数组的计算
a4 = numpy.arange(10,20).reshape(2,5)
print(a4)

a5 = numpy.arange(100,110).reshape(2,5)
print(a5)

print(a4+a5)    #相同数据类型 ,对应的直接相加进行运算,  - ,* / 其他也是一样的

a6 = numpy.arange(1,10).reshape(3,3)
print(a6)

print(a6+a5)   #不同的数据形状,是没有办法进行计算,对应的位置进行计算 ,如果在某一个纬度上相同的时间,才可以计算,所以会提示报错





