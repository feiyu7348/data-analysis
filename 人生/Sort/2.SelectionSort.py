#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 选择排序
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)


arr = [2, 4, 56, 43, 8, 13]
selection_sort(arr)
