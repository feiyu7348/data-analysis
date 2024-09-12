# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/8/3 14:46


from collections import Counter
import collections


def qeqw(s1, s2):
    counter1 = collections.Counter(s1)
    left = 0
    right = len(s1) - 1
    counter2 = collections.Counter(s2[0:right])

    while right < len(s2):
        counter2[s2[right]] += 1
        if counter1 == counter2:
            return True
        else:
            counter2[s2[left]] -= 1

        if counter2[s2[left]] == 0:
            del counter2[s2[left]]

        left += 1
        right += 1
    return False


s1 = 'qwe'
s2 = 'asdrewqsd'
print(qeqw(s1,s2))
