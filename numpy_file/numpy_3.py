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

#第二行和第三行进行数据交换
n1[[1,2],:] = n1[[2,1],:]
print(n1)
'''
[[ 0  1  2  3  4  5]
 [12 13 14 15 16 17]
 [ 6  7  8  9 10 11]
 [18 19 20 21 22 23]]
'''

#随机数组
b1 = np.random.randint(1,20,(4,5))
print('--------------------------')
print(b1)

#获取最大值和最小值的位置   axis =0 表示的是列中的位置
index_max = np.argmax(b1,axis=0)
print(index_max)

index_min = np.argmin(b1,axis=1)
print(index_min)

#快速的生成矩阵,斜对都是1
xx= np.eye(6)
print(xx)


#修改里面的数据   bool索引
print(n1<10)
'''
[[ True  True  True  True  True  True]
 [ True  True  True  True False False]
 [False False False False False False]
 [False False False False False False]]
'''
n1[n1<15]=3            # 部分替换
print(n1)

#这里使用where 三目运算符来操作,进行替换  ,条件替换
n1 = np.where(n1>14,10,15)
print(n1)

#裁剪
n1.clip(10,20)
print(n1)

#生成4 行5列的 随机数组
t1 = np.random.randint(10,20,(4,5)).astype(float)
print(t1.shape)    # 得到一个tuple元组
print(t1.shape[0])    #tuple元组的第一个数值  就是 行数

#构造一个全为 0的数据 类型和t1相同的数组
# zero_data = np.zeros((4,1),dtype=float)
zero_data = np.zeros((t1.shape[0],1)).astype(int)
print(zero_data)

#构造一个全为1的数组
one_data = np.ones((t1.shape[0],1),dtype=float,order="C")
print(one_data)


#拼接 数据
n1 = np.hstack((t1,zero_data))
print(n1)

n2 = np.hstack((t1,one_data))
print(n2)

#总的数据拼接
n3 =np.vstack((n1,n2))
print(n3)

#生成随机数组
x1 = np.random.randint(1,10,(3,4))
print(x1)
x1 = np.random.random((3,5))    #random 自动的是选择0--1之间的
print(x1)

np.random.seed(4)      #使用了随机种子后 ,以后随机的数组都是一样的
x1 = np.random.random((3,5))
print(x1)

'''
nan  不是一个数字 ,不知道是什么东西    
inf   无穷大 或者无穷小 
'''

print(np.nan !=np.nan )      #True   里面有nan的时间 ,连个数组是不是相等的

x1[:,1]= 0    #替换成 0
x1[1,2]=np.nan
print(x1)
'''
统计不为0的个数 
'''
w = np.count_nonzero(x1)
print(w)

w1 = np.count_nonzero(x1!=x1)     #统计 nan的个数
print(w1)

w = np.count_nonzero(np.isnan(x1))
print(w)

np.random.seed(10)
t3 = np.random.randint(1,10,(3,4)).astype(float)
print(t3)
t3[1,2]=np.nan
w = np.sum(t3,axis=0)               #统计一列的和,但是操作其中数组里面有nan的时间 ,直接强行的删除 不太合适
print(w)
'''
常用的统计函数 
'''
print("--------常用的统计函数--------- ,如果不带axis 就表示是真个数组的计算操作 ")
print(t3.sum(axis=0))      # 求和

print(t3.mean(axis=0))     #均值

print(np.median(t3,axis=0))     #中值

print(t3.std(axis=0))     #标准差

print(np.ptp(t3,axis=0))   #极值  就是最大值和最小值的差

'''
案例   把数组中的nan的值替换成均值  
'''


def fill_nan(a1):
    #把每列的均值替换成 当前nan的值上
    #1从每列中查找
    for i in range(a1.shape[1]):  #总共有多少列
        #当前的列
        temp_col = a1[:,i]
        #当前列中有几个nan
        nan_num = np.count_nonzero(temp_col!=temp_col)     #通过nan的的方式来判断
        #统计nan的个数
        if nan_num!=0 :    #证明里面有nan
            temp_not_nan_num = temp_col[temp_col==temp_col]      #相等表示里面没有nan 的array
            #把列中是是nan的地方 赋值  均值
            temp_col[np.isnan(temp_col)]=temp_not_nan_num.mean()
    return a1

if __name__ == '__main__':
    # 定义一个numpy数组
    a1 = np.arange(24).reshape((4, 6)).astype(float)
    print(a1)
    # 设置任意的值为nan
    a1[1, 2:] = np.nan
    print(a1)
    a1 = fill_nan(a1)
    print(a1)



