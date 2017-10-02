# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CquptItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    StdNum = scrapy.Field()
    Name = scrapy.Field()
    Sex = scrapy.Field()
    Class = scrapy.Field()
    MajorNum = scrapy.Field()
    Major = scrapy.Field()
    Academy = scrapy.Field()
    Grade = scrapy.Field()