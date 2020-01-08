#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: androidinfo.py
@time: 2020/1/6 13:11
@desc:
'''

import os
import re
from cpuinfo.log import logger

import sys
type = sys.getfilesystemencoding()

GETPACKAGE_NAME ="adb shell dumpsys window | findstr mCurrentFocus "
MEM_CMD = "adb shell dumpsys meminfo "


"获取当前的包名"
def getCurrentPackage():
    lines = os.popen(GETPACKAGE_NAME).read()
    # print(type(lines))
    for i in lines:
        print(i.decode('UTF-8').encode(type))
    # logger.info("PACKAGET_NAME :"+lines)



'获取内存的占用大小'
def getTotalPss(packagename):
    lines = os.popen(MEM_CMD+packagename).readlines() #逐行读取
    total = "TOTAL"
    for line in lines:
        if re.findall(total, line): # 找到TOTAL 这一行
            lis = line.split(" ")  #将这一行，按空格分割成一个list
            while '' in lis:       # 将list中的空元素删除
                lis.remove('')
            return lis[1] #返回总共内存使用


'获取cpu的占用'
def getCpu(packagename):
    li = os.popen("adb shell top -m 100 -n 1 -s cpu").readlines()
    name = packagename
    for line in li:
        if re.findall(name,line):
            cuplist = line.split(" ")
            if cuplist[-1].strip() == name:
                while '' in cuplist:       # 将list中的空元素删除
                    cuplist.remove('')
                return float(cuplist[2].strip('%')) #去掉百分号，返回一个float



if __name__ == '__main__':
    package = getCurrentPackage()
    logger.info(package)
    # mem = getTotalPss(package)
    # cpuin = getCpu(package)
