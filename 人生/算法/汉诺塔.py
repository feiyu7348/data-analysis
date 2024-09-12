#!/usr/bin/env python
# -*- coding:utf-8 -*-

def hanoi(n, a, b, c):              # n个盘子
    if n > 0:
        hanoi(n - 1,a ,c, b)        # 把n-1个盘子从A经过C移动到B
        print (a,'-->',c)           # 把第n个盘子从A移动到C
        hanoi(n - 1, b, a, c)       # 把n-1个盘子从B经过A移动到C


hanoi(3,'A','B','C')
