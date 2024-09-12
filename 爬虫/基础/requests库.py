#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
requests库
"""

import requests

## 11.3.2requests库基本使用方法
# 例11-9 向测试地址“http://httpbin.org/get”发送GET请求

# response = requests.get("http://httpbin.org/get")
# print("response类型：{}".format(type(response)))
# print("状态码status_code={}".format(response.status_code))
# #获取响应内容
# print(response.text)

#
# response = requests.get("http://httpbin.org/get?key=python&page=10")
# print(response.url)
# print(response.text)

# data = {
#     "key": "python",
#     "page":10
# }
# response = requests.get("http://httpbin.org/get",params=data)
# print(response.url)

# data = {
#     "key": "python",
#     "page":10,
#     "version": 3.6
# }
# response = requests.post("http://httpbin.org/post", data=data)
# print(response.text)

# 例11-12 编写爬虫程序，在京东商城搜索手机，将搜索结果网页爬取下来
def spider_jd(keyword):
    # 请求参数
    params = {
        "keyword": keyword,
        "enc": "utf-8",
        "pvid": "c150090b2d79478fb921a5e6f4b067d8"
    }

    # 请求头信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
        "Referer": "https://www.jd.com/?cu=true&utm_source=baidu-pinzhuan&utm_medium=cpc&utm_campaign=t_288551095_baidupinzhuan&utm_term=0f3d30c8dba7459bb52f2eb5eba8ac7d_0_4873e590265c4772a6c241f6b1ab87bf",
        "host": "search.jd.com",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }

    url = "https://search.jd.com/Search"

    # 获取网页内容
    response = requests.get(url, headers=headers, params=params)
    # 通过状态码判断是否获取成功
    if response.status_code == 200:
        # 回去响应内容编码格式
        print("encoding:{}".format(response.encoding))
        # 为解决中文乱码问题，重新设置编码格式utf-8
        response.encoding = "utf-8"
        print(response.text)


if __name__ == '__main__':
    spider_jd("手机")
