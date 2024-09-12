# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/14 17:58

def func(s):
    dit = {}
    for i in s:
        if i not in dit:
            dit[i] = 1
        else:
            dit[i] += 1
    return dit


def change(dit):
    res = []
    for k, v in dit.items():
        _count = 0
        flag = v
        for key, val in dit.items():
            if dit[key] < flag:
                _count += flag - dit[key]
            elif dit[key] > flag:
                _count += dit[key] - flag
        res.append(_count)
    return min(res)


s = input()
print(change(func(s)))







