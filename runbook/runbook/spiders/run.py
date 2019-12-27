# -*- coding: utf-8 -*-
import scrapy
from runbook.items import RunbookItem

class RunSpider(scrapy.Spider):
    name = 'run'
    allowed_domains = ['runoob.com']
    # start_urls = ['https://www.runoob.com/git/git-tutorial.html']
    start_urls = ['https://www.runoob.com/python/python-tutorial.html']


    def parse(self, response):
        #分组
        div_list  =response.xpath('//div[@class="col left-column"]/div[2]/div/a')
        # print(div_list)

        for la in  div_list:
            item=RunbookItem()
            item["title"] = la.xpath("./@title").extract_first()         #当前路径的 解析
            item["href"] = la.xpath("./@href").extract_first()
            item['href'] = 'https://www.runoob.com'+item["href"]     #地址补充完整
            # print(item)
            yield scrapy.Request(                                    #详情页的请求
                item['href'],                              #next_url
                callback= self.detail_parse,                 #处理页面
                meta={'item':item}             #把item传递过去
            )

    def detail_parse(self,response):                    #获取详情页的解析
        item = response.meta['item']
        item['content'] = response.xpath("//div[@class='col middle-column']/div[@class='article']/div[3]/div/p/text()").extract()
        item['image'] = response.xpath("//div[@class='col middle-column']/div[@class='article']/div[3]/div/img/@src").extract()
        # print(item)

        yield item


