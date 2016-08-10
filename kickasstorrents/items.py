# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KickasstorrentsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    #category = scrapy.Field()
    size = scrapy.Field()
    files = scrapy.Field()
    age = scrapy.Field()
    seed = scrapy.Field()
    leech = scrapy.Field()
    url = scrapy.Field()
    varified = scrapy.Field()
    mb = scrapy.Field()
    magnet = scrapy.Field()
    torrent = scrapy.Field()
    
