# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/8/13 16:35

class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lever_order(self, root):
        if not root:
            return []

        res = []
        queue = [root]
        while queue:
            res.append([node.val for node in queue])
            tmp_queue = []
            for node in queue:
                if root.left:
                    tmp_queue.append(node.left)
                if root.right:
                    tmp_queue.append(node.right)
            queue = tmp_queue
        return res


a = TreeNode()
a = [3, 9, 20, None, None, 15, 7]
b = Solution()
print(b.lever_order(a))
