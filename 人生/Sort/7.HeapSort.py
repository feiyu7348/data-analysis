#!/usr/bin/env python
# -*- coding:utf-8 -*

def sift(arr, low, high):
    """
    :param li: 列表
    :param low: 堆的根节点位置
    :param high: 堆的最后一个元素的位置
    """
    i = low                 # i最开始指向根节点
    j = 2 * i + 1           # j开始是左孩子
    tmp = arr[low]          # 把堆顶存起来
    while j <= high:        # 只要j位置有数
        if j + 1 <= high and arr[j+1] > arr[j]:   # 如果右孩子有并且比较大
            j = j + 1       # j指向右孩子
        if arr[j] > tmp:
            arr[i] = arr[j]
            i = j           # 往下看一层
            j = 2 * i + 1
        else:               # tmp更大，把tmp放到i的位置上
            arr[i] = tmp    # 把tmp放到某一级领导位置上
            break
    else:
        arr[i] = tmp        # 把tmp放到叶子节点上


def heap_sort(arr):
    n = len(arr)
    print('建堆过程：')
    print(arr)
    for i in range((n-2)//2, -1, -1):   # i表示建堆的时候调整的部分的根的下标
        sift(arr, i, n-1)
        print(arr)
    # 建堆完成
    print('堆排序过程：')
    print(arr)
    for i in range(n-1, -1, -1):        # i 指向当前堆的最后一个元素
        arr[0], arr[i] = arr[i], arr[0]
        sift(arr, 0, i - 1)             # i-1是新的high
        print(arr)


arr = [2, 7, 26, 25, 19, 17, 1, 90, 3, 36]
heap_sort(arr)
