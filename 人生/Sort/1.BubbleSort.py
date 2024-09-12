#!/usr/bin/env python
# -*- coding:utf-8 -*

# 冒泡排序
def bubble_sort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)


# 改进后
def bubble_sort1(arr):
    for i in range(len(arr)-1):
        flag = False
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            return
        print(arr)


arr = [2,34,56,34,58,98,4,7,14,17]
arr1 = [2,34,56,34,58,98,4,7,14,17]
bubble_sort(arr)
print('--------------------')
bubble_sort1(arr1)
