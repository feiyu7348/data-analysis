#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse

# 发送GET请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf8"))

'''
# 发送POSt请求
param_dict = {'key': 'hello'}
param_str = urllib.parse.urlencode(param_dict)
param_datas = bytes(param_str, encoding="utf8")
response = urllib.request.urlopen("http://httpbin.org/post", data=param_datas)
print(response.read())
'''

# 超时时间
# response = urllib.request.urlopen("http://www.baidu.com", timeout=0.001)
# print(response.read())

# 响应状态码
response = urllib.request.urlopen("http://www.baidu.com")
print(response.status)

# 响应头信息
print("headers:", response.getheaders())
print("header data:", response.getheader("date"))