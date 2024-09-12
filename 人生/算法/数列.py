# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/26

import math

def shulie(n, m):
    sum = 0
    arr = []
    for i in range(m):
        sum += n
        arr.append(n)
        n = math.sqrt(n)

    return round(sum, 2)


a = shulie(81, 4)
print(a)
