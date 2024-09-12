#!/usr/bin/env python
# -*- coding:utf-8 -*

def bucket_sort(arr):
    max_num = max(arr)
    n = len(arr)
    buckets = [[] for _ in range(n)]         # 创建桶
    for var in arr:
        i = min(var // (max_num // n), n-1)  # i 表示 var 放到几号桶里
        buckets[i].append(var)               # 把 var 加到桶里边
        # 保持桶内的顺序
        for j in range(len(buckets[i])-1, 0, -1):
            if buckets[i][j] < buckets[i][j-1]:
                buckets[i][j], buckets[i][j-1] = buckets[i][j-1], buckets[i][j]
            else:
                break
    sorted_arr = []
    for buc in buckets:
        sorted_arr.extend(buc)
    return sorted_arr


arr = [7, 12, 56, 23, 19, 33, 35, 42, 42, 2, 8, 22, 39, 26, 17]
sorted_arr = bucket_sort(arr)
print(sorted_arr)
