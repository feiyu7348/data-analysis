#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


def fanyi(kw):
    url = 'https://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'  # 去掉了_o
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    data = {
        'i': kw,
        'doctype': 'json'
    }

    res = requests.post(url, headers=headers, data=data)
    code = res.status_code
    # print(code)
    if code == 200:
        # print(res.json())  # 返回的是json数据，可以直接解析
        res_json = res.json()
        if res_json['errorCode'] == 0:
            # 请求成功
            print(res_json['translateResult'][0][0]['tgt'])
    else:
        print("翻译失败")


while True:
    keyword = input("请输入需要翻译的内容：")
    if keyword == 'q':
        break
    else:
        fanyi(keyword)
