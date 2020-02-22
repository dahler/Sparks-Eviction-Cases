import scrapy;


class ExtractUrls(scrapy.Spider):
    # This name must be unique always
    name = "extract"

    # Function which will be invoked
    def start_requests(self):
        # enter the URL here
        urls = ['http://www.indopenn.com/', ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):

        # Extra feature to get title
        title = response.css('title::text').extract_first()

        # Get anchor tags
        links = response.css('a::attr(href)').extract()

        for link in links:
            yield
            {
                'title': title,
                'links': link
            }

            print(link)
            if 'aal' in link:
                yield scrapy.Request(url=link, callback=self.parse)




def run():
    r = ExtractUrls();
    r.start_requests();


run()

                    # def parse(self, response):
#     return scrapy.FormRequest.from_response(
#         response,
#         formdata={'username': 'randomuser', 'password': 'topsecret'},
#         callback=self.after_login
#      )

"""


def after_login(self, response):
    if "Error while logging in" in response.body:
        self.logger.error("Login failed!")
    else:
        self.logger.error("Login succeeded!")
        item = SampleItem()
        item["quote"] = response.css(".text").extract()
        item["author"] = response.css(".author").extract()
        return item


def after_login(self, response):
    if "Error while logging in" in response.body:
        self.logger.error("Login failed!")
    else:
        self.logger.error("Login succeeded!")
        item = SampleItem()
        item["quote"] = response.css(".text").extract()
        item["author"] = response.css(".author").extract()
        return item

"""