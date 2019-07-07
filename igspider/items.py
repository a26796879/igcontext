# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item,Field

class IgspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    context = scrapy.Field()
    likes = scrapy.Field()
    concomments = scrapy.Field()
    href = scrapy.Field()


class ImageItem(Item):
    href = scrapy.Field()
    aftercode = scrapy.Field()
    count = scrapy.Field()
    userid = scrapy.Field()

class IgImage(scrapy.Item):
    title = scrapy.Field()
    image_urls = scrapy.Field()
    images = scrapy.Field()
    video_url = scrapy.Field()
