#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import json
from lxml import etree


# 请求的地址 猿著
url = 'https://www.lmonkey.com/essence'
# 请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}
# 发送请求
res = requests.get(url=url, headers=headers)
# if res.status_code == 200:
#     # 写入文件
#     with open('./yq.html', 'w', encoding='utf-8') as fp:
#         fp.write(res.text)

# 解析数据
html = etree.parse('./yq.html', etree.HTMLParser())

# 提取数据 作者 文章标题 文章地址url
authors = html.xpath('//div[contains(@class,"list-group-item-action")]//strong/a/text()')
print(authors)
titles = html.xpath('//div[contains(@class,"list-group-item-action")]//div[contains(@class,"topic_title")]/text()')
titles_url = html.xpath('//div[contains(@class,"list-group-item-action")]//div[contains(@class,"flex-fill")]/a/@href')

# 整理数据
data = []
for i in range(len(authors)):
    res = {'author': authors[i], 'title': titles[i], 'title_url': titles_url[i]}
    data.append(res)

# 写入数据
with open('./yq.json', 'w', encoding='utf-8') as fp:  # yq 猿圈
    json.dump(data, fp)
