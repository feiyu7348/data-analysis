#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 一个元祖表示一个活动，数字表示开始时间和结束时间
activitives = [(1,4),(3,5),(1,6),(5,7),(3,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
# 保证活动是按照结束时间排序的
activitives.sort(key=lambda x: x[1])

def activity_selection(a):
    res = [a[0]]  # 第一个结束的活动先放进去
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:  # 当前活动的开始时间小于等于最后一个入选活动的结束时间
            #不冲突
            res.append(a[i])
    return res

print(activity_selection(activitives))
