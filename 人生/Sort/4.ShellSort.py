#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 希尔排序 两个函数
def insertion_sort_gap(arr, gap):
    for i in range(gap, len(arr)):
        tmp = arr[i]
        j = i - gap
        while j >= 0 and arr[j] > tmp:
            arr[j + gap] = arr[j]
            j -= gap
        arr[j + gap] = tmp


def shell_sort(arr):
    d = len(arr) // 2
    while d >= 1:
        insertion_sort_gap(arr, d)
        print(arr)
        d //= 2


# 第二种方法 一个函数
def shell_sort1(arr):
    d = len(arr) // 2
    while d >= 1:
        for i in range(d, len(arr)):
            tmp = arr[i]
            j = i - d
            while j >= 0 and arr[j] > tmp:
                arr[j + d] = arr[j]
                j -= d
            arr[j + d] = tmp
        print(arr)
        d //= 2


arr = [3, 5, 1, 9, 4, 7]
arr1 = [3, 5, 1, 9, 4, 7]
shell_sort(arr)
print('--------------------')
shell_sort1(arr1)
