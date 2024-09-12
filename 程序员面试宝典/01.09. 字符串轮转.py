# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/8/3 14:37


def is_fliped_string(s1, s2):
    if len(s1) != len(s2):
        return False
    if len(s1) == 0:
        return True
    for i in range(len(s1)):
        if s1[i] == s2[0]:
            if s1[i:] == s2[0:len(s2)-i] and s1[0:i] == s2[len(s2)-i:]:
                return True
            else:
                continue
    return False


def is_flip_string(s1, s2):
    return (len(s1) == len(s2)) and s1 in (s2+s2)
