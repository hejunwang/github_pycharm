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

pandas  的常用数据类型  

Series  一维,带标签的数组  
DataFrame 二维 ,Series容器  

'''
import numpy as np
import pandas as pd

t =pd.Series(np.arange(10))
print(t)
