# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/10 23:29


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in s:
            if i.isalpha():
                res.append(i)
            elif i.isdigit():
                res.append(i)

        return res == res[::-1]