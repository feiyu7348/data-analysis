# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/10 8:59


p = [[1, 2], [2, 3], [2, 4], [1, 3], [3, 3]]
q = [[1, 2], [5, 3], [4, 6], [7, 5], [9, 0]]
p.sort(reverse=True, key=lambda x: x[1])

print(p)
