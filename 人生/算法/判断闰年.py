#!/usr/bin/env python
# -*- coding:utf-8 -*-

year = int(input('请输入年份：'))
if year % 4 == 0 and year % 100 != 0 or year % 4 == 0:
    print("{}年是闰年".format(year))
else:
    print("{}年不是闰年".format(year))


