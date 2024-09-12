from scrapy import Request
from scrapy.spiders import Spider
from lianjia_home.items import LianjiaHomeItem


class HomeSpider(Spider):
    name = 'home'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['https://su.lianjia.com/ershoufang/']

    current_page = 1

    def start_requests(self):
        url = "https://su.lianjia.com/ershoufang/"
        yield Request(url)

    def parse(self, response, **kwargs):
        list_selector = response.xpath("//li/div[@class='info clear']")
        for one_selector in list_selector:
            try:
                name = one_selector.xpath("div[@class='flood']/div[@class='positionInfo']/a/text()").extract_first()
                other = one_selector.xpath("div[@class='address']/div[@class='houseInfo']/text()").extract_first()
                other_list = other.split('|')
                type = other_list[0].strip(' ')
                area = other_list[1].strip(' ')
                direction = other_list[2].strip(' ')
                fitment = other_list[3].strip(' ')
                elevator = other_list[4].strip(' ')
                price_list = other_list.xpath("div[@class='priceInfo']//span/text()")
                total_price = price_list[0].extract()
                unit_price = price_list[1].extract()
                item = LianjiaHomeItem()  # 生成对象 下面将以获取的字段保存与item对象中
                item["name"] = name.strip(" ")
                item["type"] = type
                item["area"] = area
                item["direction"] = direction
                item["fitment"] = fitment
                item["elevator"] = elevator
                item["total_price"] = total_price
                item["unit_price"] = unit_price
                # 获取详情页
                url = other_list.xpath("div[@class='title']/a/@href").extract_first()
                yield Request(url, meta={"itme": item}, callback=self.property_page)
            except:
                pass

            # 获取下一页
            self.current_page += 1
            if self.current_page <= 2:
                next_url = "https://su.lianjia.com/ershoufang/pg%d/" % self.current_page
                yield Request(next_url)

    def property_page(self, response):  # 详细页
        property = response.xpath("//div[@class='base']/div[@class='content']/ul/li[last()]/text()").extract_first()
        item = response.meta["item"]
        item["property"] = property
        yield item
