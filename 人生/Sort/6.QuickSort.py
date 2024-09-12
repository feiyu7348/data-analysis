#!/usr/bin/env python
# -*- coding:utf-8 -*-

def partition(arr, left, right):
    # 归位操作，left，right 分别为数组左边和右边的位置索引
    tmp = arr[left]
    while left < right:
        while left < right and arr[right] >= tmp:  # 从右边找比 tmp 小的数，如果比 tmp 大，则移动指针
            right -= 1                             # 将指针左移一个位置
        arr[left] = arr[right]                     # 将右边的值写到左边的空位上
        while left < right and arr[left] <= tmp:   # 从左边找比 tmp 大的数，如果比 tmp 小，则移动指针
            left += 1                              # 将指针右移一个位置
        arr[right] = arr[left]                     # 将左边的值写到右边的空位上
    arr[left] = tmp                                # 把 tmp 归位
    return left                   # 返回 left，right 都可以，目的是便于后面的递归操作对左右两部分进行排序


def quick_sort(arr, left, right):
    if left < right:
        mid = partition(arr, left, right)
        # print(arr)                         # 每次归位后打印一次
        quick_sort(arr, left, mid-1)       # 对左半部分进行归位操作
        quick_sort(arr, mid+1, right)      # 对右半部分进行归位操作


arr = [5, 7, 4, 6, 3, 1, 2, 9, 8]
quick_sort(arr, 0, len(arr)-1)
print(arr)

