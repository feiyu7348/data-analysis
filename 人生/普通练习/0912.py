# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/12 23:47


def func(s):
    dp = [0] * 26
    for i in s:
        dp[ord(i) - ord('a')] += 1

    if 1 not in dp:
        return -1
    for i in range(len(s)):
        if dp[ord(s[i]) - ord('a')] == 1:
            break

    return i


s = 'aabcbddef'
# s = 'footballgamefinal'
print(func(s))

