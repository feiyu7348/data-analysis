#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 顺序查找
def liner_search(li, val):
    for ith,v in enumerate(li):
        if v == val:
            return ith
    else:
        return None

# 二分查找
# def binary_search(li, val):
#     left = 0
#     right = len(li) - 1
#     while left <= right:       # 候选区有值
#         mid = (left +  right) // 2
#         if li(mid) == val:
#             return mid
#         elif li(mid) > val:     # 待查找的值在mid左侧
#             right = mid - 1
#         else:                   # 待查找的值在mid右侧
#             left = mid + 1
#     else:
#         return None


li = [1,2,3,4,5,6,7,8,9]
print(liner_search(li, 6))
