# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

'''
class IgspiderPipeline(object):
    def process_item(self, item, spider):
        return item

import string
import scrapy
from scrapy.pipelines.images import ImagesPipeline, FilesPipeline
from scrapy.exceptions import DropItem

class IGimagePipeline(ImagesPipeline):  
    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url, meta = {'item': item})

        for video_url in item['videos_urls']:
            yield scrapy.Request(video_url, meta = {'item': item})

    def item_completed(self, results, item, info):
        image_paths = (x['path'] for ok, x in results if ok)
        if not image_paths:
            raise DropItem("Item contains no images")
        return item

class IgVideoPipeline(FilesPipeline):  
    def get_media_requests(self, item, info):
        for video_url in item['videos_urls']:
            yield scrapy.Request(video_url, meta = {'item': item})
'''