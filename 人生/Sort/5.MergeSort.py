#!/usr/bin/env python
# -*- coding:utf-8 -*-

def merge(arr, low, mid, high):
    # low 和 high 为整个数组的第一个和最后一个位置索引，mid 为中间位置索引
    # i 和 j 为指针，最初位置分别为两个有序序列的起始位置
    # ltmp 用来存放合并后的序列
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:  # 只要左右两边都有数
        if arr[i] < arr[j]:        # 当左边的数小于右边的数
            ltmp.append(arr[i])    # 将左边的数存入 ltmp
            i += 1                 # 左边的指针往右移一位
        else:                      # 当右边的数小于左边的数
            ltmp.append(arr[j])    # 将右边的数存入 ltmp
            j += 1                 # 右边的指针往右移一位
    # 上面的 while 语句执行完后，左边或者右边没有数了
    while i <= mid:                # 当左边还有数的时候
        ltmp.append(arr[i])        # 将左边剩下的数全部存入 ltmp
        i += 1
    while j <= high:               # 当右边还有数的时候
        ltmp.append(arr[j])        # 将右边剩下的数全部存入 ltmp
        j += 1
    arr[low:high+1] = ltmp         # 将排序后的数组写回原数组


def merge_sort(arr, low, high):       # low 和 high 为整个数组的第一个和最后一个位置索引
    if low < high:                    # 至少有两个元素
        mid = (low + high) // 2
        merge_sort(arr, low, mid)     # 把左边递归分解
        merge_sort(arr, mid+1, high)  # 把右边递归分解
        merge(arr, low, mid, high)    # 做归并
        print(arr)                    # 每一次归并打印一次


arr = [7, 1, 3, 2, 6, 9, 4]
merge_sort(arr, 0, len(arr)-1)
