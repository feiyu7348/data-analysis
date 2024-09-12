import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    # 基于终端指令
    # def parse(self, response):
    #     # 解析作者名称+段子内容
    #     div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
    #     # div_list = response.xpath('//*[@class="col1 old-style-col1"]//h2/text()').extract()  复制的相对路径
    #     # div_list = response.xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/a[2]/h2/text()').extract()  复制的绝对路径
    #     all_data = []  # 存储所有解析到的数据
    #
    #     for div in div_list:
    #         # xpath返回的是列表，列表元素是Selector类型的对象，extract可以将Seletor对象中的data参数存储的字符串提取出来
    #         # extract()/extract_first()方法本身都是用去提取节点的内容的，不是用来提取页面元素的Selector封装，所以无法对于这些提取的节点，使用xpath来做下一步的选取。
    #         author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
    #         content = div.xpath('./a[1]/div/span//text()').extract()
    #         content = ''.join(content)
    #
    #         dic = {
    #             'author':author,
    #             'content':content
    #         }
    #
    #         all_data.append(dic)
    #     return all_data
    #         # print(author, content)
    #         # break

    def parse(self, response):
        # 解析作者名称+段子内容
        div_list = response.xpath('//div[@class="col1 old-style-col1"]/div')
        # div_list = response.xpath('//*[@class="col1 old-style-col1"]//h2/text()').extract()  复制的相对路径
        # div_list = response.xpath('/html/body/div[1]/div/div[2]/div[1]/div[1]/a[2]/h2/text()').extract()  复制的绝对路径
        all_data = []  # 存储所有解析到的数据

        for div in div_list:
            # xpath返回的是列表，列表元素是Selector类型的对象，extract可以将Seletor对象中的data参数存储的字符串提取出来
            # extract()/extract_first()方法本身都是用去提取节点的内容的，不是用来提取页面元素的Selector封装，所以无法对于这些提取的节点，使用xpath来做下一步的选取。
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('./a[1]/div/span//text()').extract()
            content = ''.join(content)

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item  # 将item提交给了管道
