#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: numpy_3.py
@time: 2019/12/5 19:10
@desc:
'''

import numpy as np
n1 =np.arange(24).reshape(4,6)
print(n1)
'''
[[ 0  1  2  3  4  5]
 [ 6  7  8  9 10 11]
 [12 13 14 15 16 17]
 [18 19 20 21 22 23]]
'''

#修改里面的数据   bool索引
print(n1<10)
'''
[[ True  True  True  True  True  True]
 [ True  True  True  True False False]
 [False False False False False False]
 [False False False False False False]]
'''
n1[n1<15]=3
print(n1)

t1 = np.random.randint(10,20,(4,5))
print(t1)