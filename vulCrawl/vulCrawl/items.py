# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VulcrawlItem(scrapy.Item):
    # define the fields for your item here like:
    #漏洞名称
    vulName = scrapy.Field()

    #漏洞编号
    vulNum=scrapy.Field()

    #漏洞详情链接
    vulLink=scrapy.Field()

    #漏洞更新时间
    vulUpdateTime=scrapy.Field()
