# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class Car(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    location = scrapy.Field()
    brandId = scrapy.Field()

class Brand(scrapy.Item):
	id = scrapy.Field()
	name = scrapy.Field()
