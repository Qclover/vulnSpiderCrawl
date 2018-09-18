# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import datetime
class VulcrawlPipeline(object):
    #创建爬取数据保存的文件格式
    def __init__(self):
        today=str(datetime.date.today())
        self.filename=open("vul_"+today+".json","w")
        #self.filename=open("vul.json","r+")
    def process_item(self, item, spider):
        text=json.dumps(dict(item),ensure_ascii=False)+"\n"
        self.filename.write(text)
        return item

    def close_spider(self,spider):
        self.filename.close()

