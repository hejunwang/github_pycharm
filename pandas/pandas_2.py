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
d1 = [{'name':"xiaohong","age":12,"tel":'10089'},{'name':"xiaogang","sex":"male","add":"GD"}]
df = pd.DataFrame(d1)
print(df)
'''
       name   age    tel   sex  add
0  xiaohong  12.0  10089   NaN  NaN
1  xiaogang   NaN    NaN  male   GD
'''


#p26