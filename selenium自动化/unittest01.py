#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:Zfy  date:2021/6/2 14:29

import unittest


class Testcases(unittest.TestCase):
    def setUp(self) ->None:
        print("每个用例的前置")

    def tearDown(self) ->None:
        print("每个用例的后置")

    def test01(self):
        print("执行用例01")

    def test02(self):
        print("执行用例02")

    def test03(self):
        print("执行用例03")

    def test04(self):
        print("执行用例04")


if __name__ == '__main__':
    unittest.main()
