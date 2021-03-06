#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: numpy_2.py
@time: 2019/12/3 21:04
@desc:
'''

'''
在numpy中可以理解为方向 ,使用 0 ,1,2 数字表示 ,对于一个一维数组,只有一个0轴 ,对于2纬数组(shape(2,2)),有 0轴和1轴
对于3纬数组(shape(2,2,3)),有 0 ,1,2轴 
有了轴的概念后 ,我们计算就更加的方便了,比如执行一个2纬数组的平均值 ,必须指定计算是哪个方向上的数字的平均值 

'''
import numpy as np

a1 = np.arange(10).reshape(2,5)
print(a1)
'''  结果      (2,5)  2 表示0轴 ,5 就表示1轴 ,我自己认为是 0轴是就是说的x轴 ,1轴就表示的y轴 
[[0 1 2 3 4]
 [5 6 7 8 9]]
'''
a2 = np.arange(9).reshape(1,3,3)      #1是0轴 ,立方体的斜对角 ,3是0轴 ,3是1轴
print(a2)
'''
[[[0 1 2]
  [3 4 5]
  [6 7 8]]]
'''
'''
#numpy 中的转置,转置是一种变换,对于numpy中的数组来说 ,就是对角线方向交换数据 ,目的是为了更方便的处理数据
'''


a3 =np.arange(12).reshape(3,4)
print(a3)
'''
[[ 0  1  2  3]
 [ 4  5  6  7]
 [ 8  9 10 11]]
'''
# 二维数组的转换方式一
print(a3.transpose())       #行的数据 转换成列的数据
'''
[[ 0  4  8]
 [ 1  5  9]
 [ 2  6 10]
 [ 3  7 11]]
'''
#二维数组的转换方式二
print(a3.T)
print('------------')
print(a3.swapaxes(1,0))   #这里的1 和0 代表的是  1轴和0轴的转换 ,可以看出 转置和交换轴是一个效果


print('----------numpy读取数据,但是没有pandas强大,了解下---------------')
# np.loadtxt("filename",dtype=np.float,delimiter=None,skiprows=0,usecols=None,unpack=False)
       # 常用  文件路径                                                            unpack把行变成列

n1 = np.loadtxt('n2.csv',delimiter=',',dtype=int)
print(n1.shape)     #5行3列
print(n1)
'''
[[ 23 123  23]
 [ 77   1  34]
 [ 67 345 345]
 [ 12  67  67]
 [ 34  78  23]]
'''
#取行的数据
print(n1[2])
print(n1[2,:])   #每一列都要的的话 就使用  :  表示都要
#取连续的多行数据
print(n1[2:])
print('-----'*10)
#取不连续的多行数据 ,数据类型是ndarray ,直接输入要取的行数
print(n1[[0,2,4]])

print('------------------------------------------')
'''
#通用 逗号之前是行 ,逗号之后是列   这是一个通用的方法 ,不管是取行还是取列,如果每一列都要可以使用  : 表示
'''
print('------------------------------------------')

#取行
print(n1[2,:])
#通用 逗号之前是行 ,逗号之后是列   这是一个通用的方法 ,不管是取行还是取列,如果每一列都要可以使用  : 表示
#上面可以看成是第三行
#不连续的 行
print(n1[[1,3],:])


#取列
print(n1[:,1])    #对逗号之前的不动 ,使用: 代替 ,使用数字取列数
#取不连续的多列 , 逗号之前的是行,使用 :代替 ,括号内使用要取的列数 ,或者是后面的都取
print(n1[:,[0,2]])  #指定的多列

print(n1[:,1:])   #连续的多列


#行和列的具体值   取第三行第二列的值
a4 = n1[2,1]
print(a4)
print(type(a4))

#取第二行到第五行 ,第二列到第三列的数据  ,这里取的数据是行和列交叉的位置
print(n1[1:5,1:3])

#取多个不相邻的点
print('-------------------------')
print(n1[[0,1,2],[0,1,2]])

