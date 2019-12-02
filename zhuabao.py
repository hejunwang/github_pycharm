#!/usr/bin/env python
# encoding: utf-8
'''
@author: toby
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
@contact: hejunwang01@gmail.com
@software: pycharm 
@file: zhuabao.py
@time: 2019/11/28 12:53
@desc:
'''

"使用fiddler进行抓包"
"""
使用firfox 浏览器 ,设置浏览器的代理 本地代理127.0.0.1 :8888  ,这个时间要打开fiddler代理 ,否则是没有办法上网的

例如抓取淘宝的评价 
可以在responese的 textview中搜索里面的文字,查找相应的session  就可以看到是具体的url,然后保存起来备用 

抓包分析  :  找规律 
抓包地址 千图网    
https://www.58pic.com/piccate/3-156-909-p1.html
https://www.58pic.com/piccate/3-156-909-p2.html
https://www.58pic.com/piccate/3-156-909-p3.html


https://www.58pic.com/newpic/32799161.html
https://www.58pic.com/newpic/35210185.html
https://www.58pic.com/newpic/32787748.html
https://preview.qiantucdn.com/58pic/32/79/91/61S58PICwpk8Q58PICUDh258PIC3c_PIC2018.jpg!w1024_new_0
https://preview.qiantucdn.com/58pic/35/21/01/85K58PIC46f9vZ884MdW0_PIC2018.jpg!w1024_new_small
https://preview.qiantucdn.com/58pic/32/78/77/48u58PICUeceN858PICh55d4Q_PIC2018.jpg!w1024_new_0
"""
import urllib.request
import re
import urllib.error
def get_pic():
    for i in range(1,10):
        print("start")
        pageurl = "https://www.58pic.com/piccate/3-156-909-p"+str(i)+".html"
        data = urllib.request.urlopen(pageurl).read().decode('utf-8',"ignore")
        pat = "<img class='lazy' .*? src=(.*?).jpg! "
        imglist = re.compile(pat).findall(data)
        print('second')
        print(imglist)
        for j in range(0,len(imglist)):
            try:
                eachimg = imglist[j]
                imgurl = eachimg+"_1024.jpg"
                file = "imgurl/"+str(i)+str(j)+'.jpg'
                urllib.request.urlretrieve(imgurl,filename=file)
                print("第"+str(i)+"页"+"第"+str(j)+"个")
            except urllib.error.UrlError as e:
                if hasattr(e,'code'):
                    print(e.code)
                if hasattr(e,'reason'):
                    print(e.reason)
            except Exception as e:
                print(e)

if __name__ == '__main__':
    get_pic()