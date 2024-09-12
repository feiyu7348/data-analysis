#!/usr/bin/env python
# -*- coding:utf-8 -*-


'''
    数据地址：  https://www.lmonkey.com/ask
    数据字段：  问题，时间，作者, url
'''

import requests
import re
import json

# 1、定义请求的url和请求头
url = ' https://www.lmonkey.com/ask'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'
}

# 2、发起请求
res = requests.get(url, headers=headers)

# 3、检测请求是否成功
if res.status_code == 200:
    # 4、获取返回的数据
    res_html = res.text
    # with open('./reg.html', 'w', encoding='utf-8') as fp:
    #     fp.write(res_html)

    # 5、进行数据解析
    # 定义解析问题标题的正则
    reg = '<div class="topic_title mb-0 lh-180 ml-n2">(.*?)<small'
    # 调用正则方法去获取问题的标题
    title_list = re.findall(reg, res_html)
    # 定义解析作者的正则
    reg = '<strong>(.*?)</strong>'
    author_list = re.findall(reg, res_html)
    # 定义解析时间的正则
    reg = '<span data-toggle="tooltip" data-placement="top" title="(.*?)">'
    time_list = re.findall(reg, res_html)
    # 定义解析问题url的正则
    reg = '<a href="(https://www.lmonkey.com/ask/\d+)" target="_blank">'
    url_list = re.findall(reg, res_html)

    # 列表推导式
    data = list(zip(title_list, author_list, time_list, url_list))
    data_list = [{'title': i[0], 'author':i[1], 'time':i[2], 'url':i[3]}for i in data]

    # 数据入库
    with open('./data.json', 'w', encoding='utf-8') as fp:
        json.dump(data_list, fp)

