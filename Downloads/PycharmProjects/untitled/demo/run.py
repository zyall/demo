import unittest
from test_case import Case01
import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(Case01('test_case_01'))

st = open('./report.html', 'wb')
# unittest.TextTestRunner().run(suite)

runner = HTMLTestRunner.HTMLTestRunner(stream=st, title="接口测试自动化项目")

runner.run(suite)