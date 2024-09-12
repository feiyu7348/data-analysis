#!/usr/bin/env python
# -*- coding:utf-8 -*-

def wanshu():
    result = []
    for i in range(1, 1000):
        sum = 0
        for j in range(1, i):
            if i % j == 0:
                sum +=j
        if i == sum:
            result.append(i)
    return result

print(wanshu())