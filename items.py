# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ThemeforestSampleItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    short_link = scrapy.Field()
    name = scrapy.Field()
    author = scrapy.Field()
    updated = scrapy.Field()
    #ratings = scrapy.Field()
    theme_website = scrapy.Field()
    downloads = scrapy.Field()
    
    
