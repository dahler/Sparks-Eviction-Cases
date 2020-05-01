

import scrapy

class MySpider(scrapy.Spider):

    name = 'myspider'
    directory = '../html/'

    #allowed_domains = ['http://quotes.toqoute.com']

    def start_requests(self):
        urls = [
            'https://www.masscourts.org/eservices/search.page.3.1?x=STLrMU9lNBSE9oW*OplFfgdJEY61ByqG6dfUdy7DUyyqLBmt69JRurMOCC0*djgIAJ1okb3odkJpC5IrYFWs5g'
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