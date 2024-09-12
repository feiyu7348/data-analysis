#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib.request
import urllib.parse
import urllib.error

url = "http://13124adaeqw.com"
try:
    request = urllib.request.Request(url=url)
    response = urllib.request.urlopen(request)
except urllib.error.URLError as e:
    print(e.reason)

try:
    response = urllib.request.urlopen("http://douban.com/abc")
except urllib.error.HTTPError as e:
    print(e.reason)
    print(e.code)
    print(e.headers)
except urllib.error.URLError as err:
    print(err.reason)
