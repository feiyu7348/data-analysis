#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import deque

class BitreeNode:
    def __init__(self,data):
        self.data = data
        self.lchild = None
        self.rchild = None

def pre_order(root):         # 前序遍历
    if root:
        print(root.data,end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

def in_order(root):         # 中序遍历
    if root:
        in_order(root.lchild)
        print(root.data,end=',')
        in_order(root.rchild)

def post_order(root):       # 后序遍历
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data,end=',')

def level_order(root):      # 层次遍历
    queue = deque()  # 空队列
    queue.append(root)  # root进队
    while len(queue) > 0:   # 只要队不空
        node = queue.popleft()  # 出队
        print(node.data, end=',')
        if node.lchild:
            queue.append(node.lchild)  # 左孩子入队
        if node.rchild:
            queue.append(node.rchild)  # 右孩子入队
