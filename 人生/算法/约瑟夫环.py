#!/usr/bin/env python
# -*- coding:utf-8 -*-

# n=20,m=3,x=5
# n个人，报m出列，留下x个人
people = list(range(1, 21))
while len(people) > 5:
    i = 1
    while i < 3:
        people.append(people.pop(0))
        i += 1
    print('{}号被淘汰了'.format(people.pop(0)))
