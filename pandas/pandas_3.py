#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: pandas_3.py
@time: 2019/12/17 18:24
@desc:
'''
import pandas as pd
import numpy as np
df = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('defg'),dtype=float)
print(df)

print(df['d'])
print(df.loc['a',:])
print(df.loc['a','g'])

# print(df.info())
print('*'*100)
print(df['d'].mean())




