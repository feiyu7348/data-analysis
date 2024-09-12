# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/7/6 10:00

from scrapy import cmdline

cmdline.execute("scrapy crawl music -o music.csv".split())
