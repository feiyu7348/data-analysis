# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/5 14:54


def com_str(x, y):
    hashtable = dict()
    for c in y:
        if c in hashtable:
            hashtable[c] += 1
        else:
            hashtable[c] = 1

    count = 0  # 计算能拼接的次数
    n = len(x)
    m = 0  # 计算拼接一次的长度
    while True:
        for c in x:
            if c in hashtable and hashtable[c] >= 1:
                hashtable[c] -= 1
                m += 1

        if m == n:
            count += 1
            m = 0
        else:
            break

    key_n = 0
    for i, v in hashtable.items():
        key_n += 1

    return count, key_n


x = 'Mozilla'
y = 'MMMooozzziiilllllaaaswR'
print(com_str(x, y))
