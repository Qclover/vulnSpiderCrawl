# -*- coding: utf-8 -*-
import scrapy
from vulCrawl.items import VulcrawlItem
import datetime
import json
import os
class VulstartcrawlSpider(scrapy.Spider):
    name = 'vulStartCrawl'
    allowed_domains = ['anquanke.com']
    url="https://www.anquanke.com/vul?page="
    #url="http://www.cnnvd.org.cn/web/vulnerability/querylist.tag?pageno="
    offset=1
    parseTime=""
    oldTime=""
    start_urls =[url+str(offset)]
    #获取漏洞文件夹下的最后存储的漏洞文件
    vul_file=""
    #vul_dir="./vul-file/"
    def vul_dir_file(vul_dir):

        lists = os.listdir(vul_dir)
        print(list)
        #按时间排序
        lists.sort(key=lambda fn:os.path.getmtime(vul_dir+"/"+fn))
        #获取最新的文件保存到file_new
        vul_file = os.path.join(vul_dir,lists[-1])
        return vul_file
    vul_file=vul_dir_file("./vul-file")
    #获取原有漏洞库文件库中的最新漏洞时间，用来作为抓取漏洞的时间区间的结束时间end_date
    f=open(vul_file,'r',encoding='utf-8')
    for line in f.readlines()[0:2]:
        dic=json.loads(line)
        oldTimeText=dic['vulUpdateTime']
        if oldTimeText!="":
            oldTime=str(oldTimeText)
    #获取开始和结束时间区间
    def getEveryDay(self,begin_date,end_date):
        date_list=[]
        begin_date=datetime.datetime.strptime(begin_date,"%Y-%m-%d")
        end_date = datetime.datetime.strptime(end_date,"%Y-%m-%d")
        while begin_date <= end_date:
            date_str = begin_date.strftime("%Y-%m-%d")
            date_list.append(date_str)
            begin_date += datetime.timedelta(days=1)
        return date_list

    def parse(self, response):
        today=str(datetime.date.today())
        for each in response.xpath("//tr"):
            #初始化对象模型
            item=VulcrawlItem()
            #获取漏洞更新时间
            self.parseTime=each.xpath("normalize-space(./td[5]/text())").extract()[0]
            date_list1=self.getEveryDay(self.oldTime,today)
            #置换时间列表以最新时间开头
            date_list2=date_list1[::-1]
            for day in date_list2:
                if day==self.parseTime:

                    #漏洞名称
                    item['vulName']=each.xpath("normalize-space(./td[1]/div/a/text())").extract()[0]
                    #漏洞编号
                    item['vulNum']=each.xpath("normalize-space(./td[2]/a/text())").extract()[0]
                    #漏洞详情链接
                    domain="http://www.anquanke.com"
                    item['vulLink']=domain+each.xpath("normalize-space(./td[1]/div/a/@href)").extract()[0]
                    #漏洞更新时间
                    item['vulUpdateTime']=each.xpath("normalize-space(./td[5]/text())").extract()[0]
                else:
                    continue
            #item['vulUpdateTime']=data.xpath('normalize-space(string(.))').extract()[0]
            #item['vulUpdateTime']=each.xpath("./div[2]/text()").extract()[0]

            yield item
        if (self.offset<1000)&(self.parseTime>=date_list1[0]):
            self.offset +=1
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse)

