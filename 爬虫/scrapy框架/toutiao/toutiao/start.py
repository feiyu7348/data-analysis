# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/7/7 17:08

from scrapy import cmdline

cmdline.execute("scrapy crawl toutiao -o toutiao.csv".split())
