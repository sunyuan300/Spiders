# -*- coding: utf-8 -*-
import scrapy
from cqupt.items import CquptItem

class InforSpider(scrapy.Spider):
    name = "infor"
    allowed_domains = ["jwzx.cqupt.edu.cn"]
    url_head='http://jwzx.cqupt.edu.cn/jwzxtmp/'
    start_urls = [url_head+'pubBjsearch.php?action=bjStu']

    def parse(self, response):
        urls=response.xpath("//table/tbody/tr/td")
        for url in urls:
        	url_tail = url.xpath("./a/@href")
        	if not url_tail:
        		continue
        	url_tail=url_tail.extract()[0]
        	yield scrapy.Request(self.url_head+url_tail,callback=self.getInfor)
    def getInfor(self,response):
    	infors = response.xpath("//tbody/tr")
    	for infor in infors:
    		item = CquptItem()
    		detail = infor.xpath("./td/text()").extract()
    		item['StdNum'] = detail[1].encode("utf-8")
    		item['Name'] = detail[2].encode("utf-8")
    		item['Sex'] = detail[3].encode("utf-8")
    		item['Class'] = detail[4].encode("utf-8")
    		item['MajorNum'] = detail[5].encode("utf-8")
    		item['Major'] = detail[6].encode("utf-8")
    		item['Academy'] = detail[7].encode("utf-8")
    		item['Grade'] = detail[8].encode("utf-8")
    		yield item
