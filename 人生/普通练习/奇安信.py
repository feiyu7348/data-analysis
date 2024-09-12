# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/23 15:24

"""
合并区间：以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。
        输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
        输出：[[1,6],[8,10],[15,18]]
        解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].￼
"""


def func(intervals):
    intervals.sort(key=lambda x: x[0])
    res = []
    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i - 1][1]:
            res.append([intervals[i - 1][0], intervals[i][1]])
        else:
            res.append(intervals[i])
    return res


intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(func(intervals))
