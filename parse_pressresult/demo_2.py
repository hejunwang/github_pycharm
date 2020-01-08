#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: demo_2.py
@time: 2020/1/8 10:23
@desc:
'''


import re
import xlwt
if __name__ == '__main__':
    #打开文件 读取内容
    with open('PressurePushTimeArriveTest_2020-01-08_09_17_58.txt',encoding='utf-8') as fd :
        lines= fd.readlines()

    print(type(lines))

    #解析查找数据 ,并进行保存
    for line in lines:
        # print(line)
        if re.search(r'成功',str(line)):    #判断这一行 是否有成功 ,如果有成功 ,就从里面提取 数字
            time_cg = re.compile(r'第 \d*',str(line))
            current_fstime = re.compile(r'是: \d*',str(line))
            print(time_cg)
            print(current_fstime)

        # if re.search(r'到达',line):
        #     time_dd = re.compile(r'第 \d*', line)
        #     current_ddtime = re.search('是: \d*')
        #     # print(time_dd,current_ddtime)






    #写如到csv文件中 ,pandas 对比数据 进行统计分析 结果


