#!/usr/bin/env python
# -*- coding:utf-8 -*-


import urllib.parse
import urllib.request

url = "http://httpbin.org/post"
headers = {"User-Agent": "Mozilla/5.0(Macintosh;Inter Mac OS X 10_13_6)AppleWebKit/537.36(KHTML,"
                        "like Gecok)Chrome/69.0.3497.100 Safari/537.36"}
data_dict = {"world": "hello world"}
data = bytes(urllib.parse.urlencode(data_dict), encoding="utf8")
request_obj = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(request_obj)
print(response.read().decode("utf8"))