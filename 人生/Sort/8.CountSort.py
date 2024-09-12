#!/usr/bin/env python
# -*- coding:utf-8 -*-


def count_sort(arr):
    if len(arr) < 2:                       # 如果数组长度小于 2 则直接返回
        return arr
    max_num = max(arr)
    count = [0 for _ in range(max_num+1)]  # 开辟一个计数列表
    for val in arr:
        count[val] += 1
    arr.clear()                        # 原数组清空
    for ind, val in enumerate(count):  # 遍历值和下标（值的数量）
        for i in range(val):
            arr.append(ind)
    return arr


arr = [2, 3, 8, 7, 1, 2, 2, 2, 7, 3, 9, 8, 2, 1, 4, 2, 4, 6, 9, 2]
sorted_arr = count_sort(arr)
print(sorted_arr)
