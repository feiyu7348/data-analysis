#!/usr/bin/env python
# -*- coding:utf-8 -*-

def min(x, y):
    if x > y:
        return y
    else:
        return x

def max(x, y):
    if x < y:
        return y
    else:
        return x

def search_min(list, left, right):  #left为左边的索引，right为右边的索引
    if left == right or right - left == 1:
        return min(list[left],list[right])
    else:
        mid = (left + right) // 2
        list[left] = search_min(list, left, mid)
        list[right] = search_min(list, mid, right)
        return min(list[left],list[right])

def search_max(list, left, right):
    if left == right or right - left == 1:
        return max(list[left],list[right])
    else:
        mid = (left + right) // 2
        list[left] = search_max(list, left, mid)
        list[right] = search_max(list, mid+1, right)
        return max(list[left],list[right])

list = [2,5,98,20,50,14]
list1 = list.copy()
left = 0
right = len(list) - 1
print(search_min(list,left,right))
print(list)
print(search_max(list1,left,right))