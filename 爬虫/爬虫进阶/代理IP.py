#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


url = 'http://httpbin.org/get'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}

# 定义代理ip
proxies = {
    'http': '',
    'https': ''
}

try:
    res = requests.get(url, headers=headers, proxies=proxies)
    if res.status_code == 200:
        data = res.json()
        print(data['origin'])
except:
    print("请求失败")