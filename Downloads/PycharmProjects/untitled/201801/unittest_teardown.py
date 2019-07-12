# coding:utf-8
# 后置条件：tearDown(self):
# 后置条件就是做数据清理，就好比只测新增草稿箱这个功能（为了保持数据是干净，做后置清理的操作）

import unittest

class Blog(unittest.TestCase):
    def  setUp(self):
        # 前置可以写一些测试用例的一些准备工作，如数据准备，登录等
        pass
    def test_01(self):
        # 操作步骤
        # 获取结果
        # assert断言
        pass
    def tearDown(self):
        # 后置处理，清理垃圾数据，不影响后续用例
        pass
if __name__="__main__":
    unittest.main()