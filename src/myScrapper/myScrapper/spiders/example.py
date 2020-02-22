# -*- coding: utf-8 -*-
import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['www.indopenn.com']
    start_urls = ['http://www.indopenn.com/']

    def parse(self, response):
        pass
