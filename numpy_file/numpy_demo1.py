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

a = numpy.array([1,2,3,5])    #必须是相同的结构
a1 = numpy.array([1,2,3,5.0])    #必须是相同的类型,会自动的都会变成float
print(a)
print(a1)
print(a[0:3])

t1 = numpy.array(range(1,8))
print(t1)
print(type(t1))

t3 = numpy.arange(4,10,2)
print(t3)

#切片
vect = numpy.array([5,3,90,12,23])
print(vect[:3])                 #左闭右开

matrix =numpy.array([[1,4,6],
                     [2,4,5],
                     [34,23,45]])
matrix.sort()                     #排序
print(matrix[:,0:2])              #取所有数据的前两列,这是多维的切片


