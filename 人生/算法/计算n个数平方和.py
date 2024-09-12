#!/usr/bin/env python
# -*- coding:utf-8 -*-

def cala(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i*i
    return sum

a = cala(1,2,3,4)
print(a)