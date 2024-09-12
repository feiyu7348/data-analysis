#!/usr/bin/env python
# -*- coding:utf-8 -*-

def radix_sort(li):
    max_num = max(li)      # 最大值 9->1次循环, 99->2次循环, 888->3次循环, 10000->5次循环
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in li:
            # var=987, it=1, 987//10->98, 98%10->8; it=2, 987//100->9, 9%10=9
            digit = (var // 10 ** it) % 10   # 依次取一位数
            buckets[digit].append(var)
        # 分桶完成
        li.clear()
        for buc in buckets:
            li.extend(buc)
        it += 1            # 把数重新写回 li
    return arr


arr = [3221, 1, 10, 9680, 577, 9420, 7, 5622, 4793, 2030, 3138, 82, 2599, 743, 4127]
sorted_arr = radix_sort(arr)
print(sorted_arr)
