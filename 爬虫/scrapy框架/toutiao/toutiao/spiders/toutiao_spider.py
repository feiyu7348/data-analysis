import scrapy
from scrapy import Request
from toutiao.items import ToutiaoItem
from selenium import webdriver


class ToutiaoSpiderSpider(scrapy.Spider):
    name = 'toutiao'

    def __init__(self):
        self.driver = webdriver.PhantomJS()  # 无界面浏览器驱动

    def start_requests(self):
        url = "https://www.toutiao.com/"
        yield Request(url)

    def parse(self, response):
        item = ToutiaoItem()
        list_selector = response.xpath("//div[@class='ttp-feed-module']/div[@class='feed-card-wrapper "
                                       "feed-card-article-wrapper']")
        for div in list_selector:
            try:
                title = div.xpath(".//div[@class='feed-card-article-l']/a/@title").extract()
                source = div.xpath(".//div[@class='feed-card-footer-cmp-author']/a/text()").extract()
                comment = div.xpath(".//div[@class='feed-card-footer-comment-cmp']/a/@aria-label").extract()
                item["title"] = title
                item["source"] = source
                item["comment"] = comment
                yield item
            except:
                continue

