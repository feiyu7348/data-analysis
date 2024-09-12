#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  time:2021/5/27

"""
外观模式：
    - 内容：为子系统中的一组接口提供一个一致的界面，外观模式定义了一个高层接口，这一接口使得这一子系统更加容易使用
    - 角色：
        - 外观
        - 子系统类
    - 优点：
        - 减少系统相互依赖
        - 提高了灵活性
        - 提高了安全性
"""


class Cpu:
    def run(self):
        print("cpu开始运行")

    def stop(self):
        print("cpu停止运行")


class Disk:
    def run(self):
        print("硬盘开始工作")

    def stop(self):
        print("硬盘停止工作")


class Memory:
    def run(self):
        print("内存通电")

    def stop(self):
        print("内存断电")


class Computer:
    def __init__(self):
        self.cpu = Cpu()
        self.disk = Disk()
        self.memory = Memory()

    def run(self):
        self.cpu.run()
        self.disk.run()
        self.memory.run()

    def stop(self):
        self.cpu.stop()
        self.disk.stop()
        self.memory.stop()


# client
computer = Computer()
computer.run()
computer.stop()
