#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: pandas_2.py
@time: 2019/12/12 20:15
@desc:
'''

import pandas as pd
import numpy as np

'''
DataFrame  二维数据 ,是Series 的容器 
'''

df = pd.DataFrame(np.arange(12).reshape(3,4))
print(df)
'''
   0  1   2   3         最顶部一行 指的是 列索引,表明是不同的列,纵向索引 ,叫columns  1轴 ,axis =1  
0  0  1   2   3                         
1  4  5   6   7
2  8  9  10  11         左侧的最前面的一列是行索引 ,表明不同的行,横向索引叫index ,0轴 ,axis = 0
'''

#series 可是使用dict创建 , DataFrame 也是可以传入dict的 ,其中没有的信息,使用的nan来进行填充
d1 = [{'name':"xiaohong","age":12,"tel":'10089'},
      {'name':"xiaogang","sex":"male","add":"GD","age":15},
      {'name':"xiaoming","sex":"male","add":"GD","age":13}
      ]
df = pd.DataFrame(d1)
print(df)
'''
       name   age    tel   sex  add
0  xiaohong  12.0  10089   NaN  NaN
1  xiaogang   NaN    NaN  male   GD
'''
print(df.index)
print(df.columns)
'''
RangeIndex(start=0, stop=2, step=1)
Index(['name', 'age', 'tel', 'sex', 'add'], dtype='object')
'''

print('*'*100)
'''
DataFrame的基础属性 
'''
print(df.shape)     #行 列 数
print(df.dtypes)     #列数据的类型
print(df.ndim)     #数据纬度
print(df.index)     # 行 索引
print(df.columns)     # 列索引
print(df.values)     # 二维的  ndarray

print(df.head(2))     # 显示头部几行 ,默认是5
print(df.tail(1))     # 显示末尾几行,默认是5

print(df.info())     # 相关信息的概要
print(df.describe())     # 快速综合的统计信息  统计数字列

print('*'*50+"重要"+"*"*50)
print(df.sort_values(by="age",ascending=False))    # 这个排序后面用的较多        降序排列
'''
pandas 中取行或者列的注意点 :
---方括号 写数组 表示对行 操作 
---方括号写字符串,表示的取列索引,对列进行操作  
'''
print(df[:1])
print(df['sex'])
print(df[:2]['age'])   #取得2行之前的数据 ,其中列中选择age列 作为输出

'''
pandas 优化过的选择方式  
df.loc[]  通过标签索引行数据  
df.iloc[]  通过位置获取行数据  

'''

t3 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('wxyz'))
print(t3)
'''
   w  x   y   z
a  0  1   2   3
b  4  5   6   7
c  8  9  10  11
'''
#
print(t3.loc['a','z'])    #  3
print(t3.loc['a'])    #  a 行
print(t3.loc['a',:])    #  a 行
print(t3.loc[:,'w'])    #  w 列
print(t3.loc[['a','c'],:])    #a 行 和c行

print(t3.loc['a':'c',['z','y']])  #连续的a行到c行,y列和z列 ,这里要注意的是 包含了c行


print('iloc是通过位置来选择的')
print(t3.iloc[0])  #代表0行
print(t3.iloc[0:2,])  #代表连续多行
print(t3.iloc[[0,2]])  #代表不连续多行
print(t3.iloc[:,1])  #代表第1列
print(t3.iloc[:,1:])  #代表1列以后的连续的列
print(t3.iloc[:,1:3])  #代表1列到3列
print(t3.iloc[:,[1,3]])  #代表1列 和第3列数据

#也是可以赋值的
t3.iloc[[0,2],[1,3]] = 10
print(t3.iloc[[0,2],[1,3]])  #代表1列 和第3列数据 ,第0行和第2行 之间的交叉区域数据


'p28:00'