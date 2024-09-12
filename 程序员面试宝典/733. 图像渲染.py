# !/user/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/8/11 20:09

from queue import Queue


class Solution:
    def floodFill(self, image, sr: int, sc: int, newColor: int):
        # 起始颜色和目标颜色相同，则直接返回原图
        if newColor == image[sr][sc]:
            return image
        # 设置四个方向偏移量，一种常见的省事儿技巧
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        # 构造一个队列，先把起始点放进去
        que = Queue()
        que.put((sr, sc))
        # 记录初始颜色
        original_color = image[sr][sc]
        # 当队列不为空
        while not que.empty():
            # 取出队列的点并染色
            point = que.get()
            image[point[0]][point[1]] = newColor
            # 遍历四个方向
            for direction in directions:
                # 新点是(new_i,new_j)
                new_i = point[0] + direction[0]
                new_j = point[1] + direction[1]
                # 如果这个点在定义域内并且它和原来的颜色相同
                if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == original_color:
                    que.put((new_i, new_j))
        return image


image = [[0,0,0],[0,0,0]]
sr = 0
sc = 0
newColor = 2
a = Solution()
print(a.floodFill(image,sr,sc,newColor))
