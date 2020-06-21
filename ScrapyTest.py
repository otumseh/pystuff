# Scrapy tutorial test1

import scrapy

#
class QuotesSpider(scrapy.Spider):
# name = sets the name of the spider
    name = "quotes"

# must return an iterable of Requests
    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
# a method that will be called to handle the response downloaded by the requests
    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

