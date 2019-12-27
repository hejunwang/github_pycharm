# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import re

from pymongo import MongoClient
class RunbookPipeline(object):
    def process_item(self, item, spider):
        item['content']= [ re.sub(r'\r\n','',i) for i in item['content']]     #清洗下数据
        print(dict(item))
        self.collection.insert(dict(item))                  #插入到数据库中
        with open('git.txt','a',encoding='utf-8') as fd :
            fd.write(str(item))

        return item

    def open_spider(self,spider):                        # 开始执行一次   默认是不显示的 ,自己可以单独写出来
        print("start open_spider")
        self.client = MongoClient()
        self.collection = self.client['test']['sites']

    def close_spider(self,spider):                                      #   最后执行一次
        print(" this is close_spider ")