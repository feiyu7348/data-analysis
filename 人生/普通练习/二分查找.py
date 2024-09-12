# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/18 16:27

def func(arr, target):
    left = 0
    right = len(arr) - 1
    # if target > arr[right]:
    #     return -1
    # if target < arr[left]:
    #     return -1

    while left < right:
        mid = (left + right) // 2
        if target == arr[mid]:
            return mid
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


arr = [1, 2, 3, 5, 6, 7]
print(func(arr, 0))
