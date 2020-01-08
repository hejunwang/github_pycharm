#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: texttocsv.py
@time: 2020/1/6 14:38
@desc:
'''

import pandas as pd

#导入到csv中   sep=','表示去除逗号，按照逗号对数据进行分割。sep='\D*'表示去除非数字字符，按照非数字字符对数据进行分割
# xg = pd.read_csv("cpuinfo/xg.txt",sep=' ',header=None)
# # print(xg.head())
pos = []
Efield = []
t3 =[]
with open("xg.txt",'r') as fd :
    while True:
        lines = fd.readlines()
        if not lines:
            break
        else:
            p1,p2,p3 =[i for i in lines.split(':')]


