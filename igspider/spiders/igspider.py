# -*- coding: utf-8 -*-

import scrapy
from ..items import ImageItem, IgspiderItem
import json
from bs4 import BeautifulSoup

class InstagramSpider(scrapy.Spider):
    name = 'igcrawler'
    start_urls = ['https://www.instagram.com/oppsweiiiii']
    def parse(self, response):
        items = IgspiderItem()
        urldata = response.body
        soup = BeautifulSoup(urldata, 'html.parser')
        json_part = soup.find_all("script", type="text/javascript")[3].string
        json_part = json_part[json_part.find('=')+2:-1]
        link = []
        data = json.loads(json_part)
        a = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['edges']
        aftercode = data['entry_data']['ProfilePage'][0]['graphql']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        userid = data['entry_data']['ProfilePage'][0]['graphql']['user']['id']

        # 取出個別文章中的文字
        for i in range(len(a)):
            #item = IgspiderItem()
            items['href'] = 'https://www.instagram.com/p/' + \
                a[i]['node']['shortcode'] + '/'
            link.append(items)
            href_url = items['href']
            yield scrapy.Request(href_url, self.parse_context)

        nexturl = 'https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%22' + userid + '%22%2C%22first%22%3A12%2C%22after%22%3A%22' + aftercode.replace('=', '') + '%3D%3D"%7D'
        url = response.urljoin(nexturl)
        yield scrapy.Request(url, self.parse_json)

    def parse_context(self, response):
        item = IgspiderItem()
        urldata = response.body
        soup = BeautifulSoup(urldata, 'html.parser')
        json_part = soup.find_all("script", type="text/javascript")[3].string
        json_part = json_part[json_part.find('=')+2:-1]
        data = json.loads(json_part)
        a = data['entry_data']['PostPage'][0]['graphql']['shortcode_media']
        #contents = a['edge_media_to_caption']['edges'][0]['node']['text']
        item['context'] = a['edge_media_to_caption']['edges'][0]['node']['text']

        yield item

    def parse_json(self,response):
        items = IgspiderItem()
        urldata = response.body
        soup = BeautifulSoup(urldata, 'html.parser')
        rdata = json.loads(soup.text)
        ra = rdata['data']['user']['edge_owner_to_timeline_media']['edges']
        aftercode = rdata['data']['user']['edge_owner_to_timeline_media']['page_info']['end_cursor']
        userid = rdata['data']['user']['edge_owner_to_timeline_media']['edges'][0]['node']['owner']['id']
        link = []
        # 取出個別文章中的文字
        for i in range(len(ra)):
            #item = IgspiderItem()
            items['href'] = 'https://www.instagram.com/p/' + \
                ra[i]['node']['shortcode'] + '/'
            link.append(items)
            href_url = items['href']
            yield scrapy.Request(href_url, self.parse_context)
        if aftercode  is not None:
            nexturl = 'https://www.instagram.com/graphql/query/?query_hash=f2405b236d85e8296cf30347c9f08c2a&variables=%7B%22id%22%3A%22' + userid + '%22%2C%22first%22%3A12%2C%22after%22%3A%22' + aftercode.replace('=', '') + '%3D%3D"%7D'
            url = response.urljoin(nexturl)
            yield scrapy.Request(url, self.parse_json)       
