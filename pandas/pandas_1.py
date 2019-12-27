#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: pandas_1.py
@time: 2019/12/9 20:38
@desc:
'''

'''
pandas 处理numpy 之外的 工具,处理原始的数据  比较复杂的 不只是数组类型的 数据  
pandas的常用数据类型分两类 :  
Series  一维,带标签的数组  
DataFrame 二维 ,Series容器  

'''
import numpy as np
import pandas as pd

t =pd.Series(np.arange(5))   #带标签的数组
print(t)
print(type(t))
'''
0    0
1    1
2    2
3    3
4    4
dtype: int32
<class 'pandas.core.series.Series'>
'''
t1 = pd.Series([1,2,3,4,5],index=list('abcde'))   #指定数组的index
print(t1)
# a    1
# b    2
# c    3
# d    4
# e    5
# dtype: int64

temp_dict={"name":"abc","age":30,"add":"xsdfsdfsdf"}
t2 = pd.Series(temp_dict)                      #通过字典的方式 创建
print(t2)
'''
name           abc
age             30
add     xsdfsdfsdf
dtype: object
'''
print('#索引 --- 一个的时间直接传入序号这是index ,多个的时间传入序号或者是index列表'
      ' 和切片---直接传入start  end  step即可    ')
name = t2['name']     #通过关键字
print(name)
'name           abc'

add = t2[2]          #通过位置 索引
print(add)
'add     xsdfsdfsdf'
print("*"*20)
x1 = t2[:2]     # 取前两行
print(x1)
'''
name    abc
age      30
dtype: object
'''


x1 = t2[[0,2]]     # 取不连续的行   t2[['name','add']]  这样也是可以的
print(x1)
# name           abc
# add     xsdfsdfsdf


# x1 = t2['tel']     #如果数组中没有对应的关键字,取数据的时间,可能得到nan 或者是报错
# print(x1)

#bool 索引
x1 = t1[t1>2]
print(x1)

print(t2.index)       #属性值
# 'Index(['name', 'age', 'add'], dtype='object')'
print("*"*100)
print(t2.values)
# ['abc' 30 'xsdfsdfsdf']
print("*"*100)
print(type(t2.values))
#<class 'numpy.ndarray'>


'''
读取外部文件   
'''
df = pd.read_csv('pandas_1.csv')
print(df)


