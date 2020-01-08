#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: cpu.py
@time: 2020/1/3 20:36
@desc:
'''

# from .log
import psutil
import os
from cpuinfo.log import logger

def getcupinfo():
    # 获取当前运行的pid
    p1 = psutil.Process(os.getpid())

    # 打印本机的内存信息
    print('直接打印内存占用： ' + (str)(psutil.virtual_memory))

    # 打印内存的占用率
    print('获取内存占用率： ' + (str)(psutil.virtual_memory().percent) + '%')

    # 本机cpu的总占用率
    print('打印本机cpu占用率： ' + (str)(psutil.cpu_percent(0)) + '%')

    # 该进程所占cpu的使用率
    print(" 打印该进程CPU占用率: " + (str)(p1.cpu_percent(None)) + "%")

    # 直接打印进程所占内存占用率
    print(p1.memory_percent)

    # 格式化后显示的进程内存占用率
    # print("percent: %.2f%" %(p1.memory_percent()))

    logger.info("  cpu test")

if __name__ == '__main__':
    getcupinfo()
