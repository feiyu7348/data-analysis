#!/usr/bin/env python
# -*- coding:utf-8 -*-

def binary(n):
    s = []
    while n:
        s.append(str(n % 2))
        n = n // 2
    s.reverse()
    return ''.join(s)


print(binary(64))