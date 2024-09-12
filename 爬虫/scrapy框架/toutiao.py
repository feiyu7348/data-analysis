import scrapy


class ToutiaoSpider(scrapy.Spider):
    name = 'toutiao'
    allowed_domains = ['www.xxx.com']
    start_urls = ['http://www.xxx.com/']

    def parse(self, response):
        pass
