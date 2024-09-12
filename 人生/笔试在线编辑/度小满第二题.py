# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/5 15:53

def func(s, n):
    res = []
    for c in s:
        if c == 'O':
            res.append('1')
        elif c == 'X':
            res.append('0')
    res = ''.join(res)

    ans = []
    for nums in n:
        conut = 0
        for i in range(len(res)):
            if res[i] == '0' and nums[i] == '1':
                ans.append('NO')
                break
            conut += 1

        if conut == len(res):
            ans.append('YES')

    return ans


s = 'OOXX'
n = ['1111', '1100', '0100']
print(func(s, n))

