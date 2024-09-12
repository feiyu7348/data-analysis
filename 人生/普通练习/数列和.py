# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/4 17:46

import math


def func(m, n):
    sum = 0
    for i in range(n):
        sum += m
        m = math.sqrt(m)

    return round(sum, 2)


print(func(2, 2))
