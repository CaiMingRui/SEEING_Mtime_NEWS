# -*- coding: utf-8 -*-
import scrapy
import time
import json
import sys
import re
import getnesid
import chardet
import tutorial.main
import os

reload(sys)
sys.setdefaultencoding('utf-8')
from tutorial.items import CollectItem
from urlparse import urljoin
import tutorial
# from tutorial.items from CollectItem
ISOTIMEFORMAT='%Y-%m-%d %X'

name = "movietime"

class TaskEightSpider(scrapy.Spider):
    cot = 0
    download_delay = 3
    name = "movietime"
    start_urls =[]
    # movie_file_name = []
    sb = os.listdir("/home/caimingrui/桌面/2/")
    for i in sb:
        print i
        # movie_file_name.append(i)
        with open("/home/caimingrui/桌面/2/" + i) as f:
            urls = f.readlines()
            for url in urls:
                url2 = urls.remove('\n')
            for urlx in url2:
                start_urls.append(urlx)

    def parse(self,response):

        # for href in response.xpath("//div[@class='db_newsout']/div[@class='db_newsbox']/dl[@class='db_newslist']//h3/a/@href").extract():
        #     # url = response.urljoin(href)
        #     url = href
        #     yield scrapy.Request(url, callback=self.parse_dir_contents)
        # for next_page in response.xpath("//a[@id='key_nextpage']/@href").extract():
        #     url1=tutorial.main.unurl
        #     url2 = url1 + next_page
        #     print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"+url2
        #     # url = response.urljoin(next_page)
        #     url = url2
        url = response.url
        yield scrapy.Request(url, callback=self.parse)
        # gmovie = response.xpath("//div[@id='db_sechead']/div[@class='db_head']/div[@class='clearfix']/h1/a/text()").extract_first()#获取电影名，因为只有在这歌链接可以找到，到新闻里面就没了
        # self.moviename = gmovie
        # yield scrapy.Request(self.moviename, callback=self.parse_dir_contents)
        # print response

    def parse_dir_contents(self, response):
        # newkinds = response.url
        # kinds = re.findall(newkinds,"http://id.beritasatu.com/(.*?)/(.*?)",0)
        with open("/home/caimingrui/SJWJ/summerdate/html/" + str(self.cot) + '.html', "wb")as f:
            f.write(response.body)
        item = CollectItem()
        self.cot += 1
        item['news_id'] = self.cot
        item['cole_time'] = time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
        item['language'] = 'chi'
        item['classification'] = 'movies news'
        item['title'] = str(response.xpath("//div[@class='newshead ']/div[@class='newsheader ']/div[@class='newsheadtit']/h2/text()").extract_first())+str(response.xpath("//div[@class='newshead ']/div[@class='newsheader ']/div[@class='newsheadtit']/h3/text()").extract_first())
        item['request_url'] = response.url
        item['pub_time'] = re.findall('<p class="mt15 ml25 newstime ">(.*?) ',response.body)
        item['body'] = response.xpath("//div[@class='newsl']/div[@id='newsContent']/div/*/text()|//div[@class='newsl']/div[@id='newsContent']/div/text()|//div[@class='newsl']/div[@id='newsContent']/p/text()|//div[@class='newsl']/div[@id='newsContent']/p/*/text()|"
                                      "//div[@class='featureright']/div[@id='newsContent']/text()|//div[@class='featureright']/div[@id='newsContent']/a/text()").extract()
        yield item
