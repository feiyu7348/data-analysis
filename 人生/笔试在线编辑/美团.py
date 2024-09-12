# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/11 15:50

n, m, q = map(int, input().split())
arr = []
for i in range(m):
    x, y = map(int, input().split())
    arr.append([x, y])

for i in range(q):
    a, b = map(int, input().split())
    tmpa = []
    tmpb = []
    for j in range(len(arr)):
        if arr[j][0] == a:
            tmpa.append([j, 0])
            if arr[j][1] == b:
                tmpb.append([j, 1])
        elif arr[j][1] == a:
            tmpa.append([j, 1])
            if arr[j][0] == b:
                tmpb.append([j, 0])
        elif arr[j][0] == b:
            tmpb.append([j, 0])
            if arr[j][1] == a:
                tmpa.append([j, 1])
        elif arr[j][1] == b:
            tmpb.append([j, 1])
            if arr[j][0] == a:
                tmpa.append([j, 0])

    for i in range(len(tmpa)):
        arr[tmpa[i][0]][tmpa[i][1]] = b
    for i in range(len(tmpb)):
        arr[tmpb[i][0]][tmpb[i][1]] = a


res = [0] * (n+1)
for i in range(len(arr)):
    res[arr[i][0]] += 1
    res[arr[i][1]] += 1


ans = ''
for i in range(1, len(res)):
    ans += str(res[i]) + ' '

print(ans)
