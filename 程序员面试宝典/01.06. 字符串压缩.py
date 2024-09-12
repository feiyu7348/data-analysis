# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/8/2 23:11


def compress_string(s):
    count = 1
    s += ' '
    nem_s = ''
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            nem_s += s[i] + str(count)
            count = 1

    return nem_s if len(nem_s) < len(s)-1 else s[:len(s)-1]


s = "aabcccccca"
print(compress_string(s))
