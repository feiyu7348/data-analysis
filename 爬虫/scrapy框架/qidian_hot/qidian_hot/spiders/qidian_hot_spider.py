# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/7/4 20:30

from scrapy import Request
from scrapy.spiders import Spider
from qidian_hot.items import QidianHotItem


class HotSalesSpider(Spider):
    name = 'hot'
    qidian_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
    }
    current_page = 1

    def start_requests(self):
        url = "https://www.qidian.com/rank/hotsales?style=1&page=1"
        yield Request(url, headers=self.qidian_headers, callback=self.parse)

    def parse(self, response, **kwargs):  # 数据解析
        list_selector = response.xpath("//div[@class='book-mid-info']")
        for one_selector in list_selector:
            # 获取小说信息
            name = one_selector.xpath("h4/a/text()").extract()[0]
            # 获取作者
            author = one_selector.xpath("p[1]/a[1]/text()").extract()[0]
            # 获取类型
            type = one_selector.xpath("p[1]/a[2]/text()").extract()[0]
            # 获取形式
            form = one_selector.xpath("p[1]/span/text()").extract()[0]

            item = QidianHotItem()
            item["name"] = name
            item["author"] = author
            item["type"] = type
            item["form"] = form

            # # 定义字典
            # hot_dict = {
            #     "name": name,
            #     "author": author,
            #     "type": type,
            #     "form": form
            # }
            yield item

            # 获取下一页url
            self.current_page += 1
            if self.current_page <= 5:
                new_url = "https://www.qidian.com/rank/hotsales?style=1&page=%d" % self.current_page
                yield Request(new_url)
