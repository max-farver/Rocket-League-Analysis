# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose



class RlScrapingItem(scrapy.Item):
    file_urls = scrapy.Field()
    files = scrapy.Field()
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
