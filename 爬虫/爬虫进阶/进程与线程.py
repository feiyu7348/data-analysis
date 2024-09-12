#!/usr/bin/env python
# -*- coding:utf-8 -*-

from multiprocessing import Process  # 进程
from threading import Thread  # 线程
import time
import os
import threading


def work(n):
    print(f"给{n}打电话，进程号：{os.getpid()}, 线程号:{threading.current_thread()}")
    time.sleep(3)
    print(f"{n}通话结束，进程号：{os.getpid()}, 线程号:{threading.current_thread()}")


userlist = ["1", "2", "3"]

# 普通方式
# 启动了一个进程，进程中有一个主线程
# for item in userlist:
#     work(item)


# 需要放到这里面才能运行
if __name__ == '__main__':
    # 多进程 类似于创建多个部门
    # plist = []
    # for item in userlist:
    #     # 循环创建进程
    #     p = Process(target=work, args=(item,))
    #     # 启动进程
    #     p.start()
    #     # 把创建的进程加入到列表中
    #     plist.append(p)
    # # 阻塞终止进程的执行
    # [i.join() for i in plist]

    # 多线程 类似于给这个部门增加人手
    plist = []
    for item in userlist:
        # 循环创建线程
        p = Thread(target=work, args=(item,))
        # 启动线程
        p.start()
        # 把创建的线程加入到列表中
        plist.append(p)
    # 阻塞终止进程的执行
    [i.join() for i in plist]
