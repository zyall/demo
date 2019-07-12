# coding:utf-8
# 注意
# 测试类，继承单元测试unittest.TestCase
# 测试方法（用例）必须以test开头
# 测试类就是多个用例的一个集合，相当于是测试用例的一个模块
import unittest

class Test(unittest.TestCase):
    def testAdd(self):
        a=1
        b=2
        c=a+b
        self.assertEqual(c,3)
'''
    def testMultiply(self):
        a=1
        b=2
        c=a*b
        self.assertEqual(c,5)
'''
if __name__ == "__main__":
    unittest.main()


