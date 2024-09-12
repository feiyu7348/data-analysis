# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/9/19 10:40


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @return ListNode类
#

class Solution:
    def reverseList(self, head):
        # write code here
        if not head or not head.next:
            return head

        per = head
        cur = head.next
        while cur:
            tmp = cur.next
            cur.next = per
            per = cur
            cur = tmp
        return cur


head = ListNode(1)
a = head.next
a = ListNode(2)
b = a.next
b = ListNode(3)
s = Solution()
print(head.next)
print(s.reverseList(head))

