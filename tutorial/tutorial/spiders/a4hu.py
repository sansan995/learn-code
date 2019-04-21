# -*- coding: utf-8 -*-
import scrapy


class A4huSpider(scrapy.Spider):
    name = '4hu'
    allowed_domains = ['568.cn']
    start_urls = ['https://www.568.cn/']

    def parse(self, response):

        pass
