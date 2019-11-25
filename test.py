#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: test.py
@time: 2019/11/23 13:27
@desc:
'''

'''
在GitHub上创建仓库   
1 . vcs -->import into version --> share project on github  可以在GitHub上可以看到已经上传的代码 
2 .创建分支 
在底部的git:master  从origin master checkout一个分支到本地命名为dev   新建分支后可以看到current分支变为dev
可以看到在local branches 下看到dev 
注意，这个dev实际是本地的，origin并没有dev分支，不信到gitlab上看 
通过右下角的checkout可以自如的在dev和master分支上切换

一般情况下就在本地的dev上开发即可，开发完就可以删掉这个本地dev分支了，
如果想在origin上也创建一个dev分支，需要commit一下  

分支的代码编写完成之后 ,切换到master上, 就可以merge 到github 上了 
右键 git , respository -->push 



这个是test 更新文档,这是dev分支 branch 

'''