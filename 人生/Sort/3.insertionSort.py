#!/usr/bin/env python
# -*- coding:utf-8 -*-


def insertion_sort(arr):
    for i in range(1, len(arr)):
        tmp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > tmp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = tmp
        print(arr)


arr = [4, 1, 5, 7, 8, 3]
insertion_sort(arr)

