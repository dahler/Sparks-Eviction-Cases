

import scrapy

class MySpider(scrapy.Spider):

    name = 'myspider'
    directory = '../html/'

    #allowed_domains = ['http://quotes.toqoute.com']

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
            'https://www.masscourts.org/eservices/search.page.3.5?x=gjqNue7Jqoq4haRZvIu12g'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(self.directory+filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

# --- it runs without project and saves in `output.csv` ---

from scrapy.crawler import CrawlerProcess

c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0'
})
c.crawl(MySpider)
c.start()