#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor  # 进程池


def work(n):
    print(f"给{n}打电话")
    time.sleep(3)
    print(f"{n}通话结束")


userlist = ["1", "2", "3", "4", "5"]

# 1、创建线程池
pool = ThreadPoolExecutor(max_workers=3)

# 2、循环指派任务
[pool.submit(work, user) for user in userlist]

# 3、关闭线程池
pool.shutdown()
