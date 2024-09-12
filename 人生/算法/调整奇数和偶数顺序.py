# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/26

def exchange_liner(arr):
    a = []
    b = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            a.append(arr[i])
        elif arr[i] % 2 == 1:
            b.append(arr[i])
    return b + a

arr = [2,3,8]
print(exchange_liner(arr))

