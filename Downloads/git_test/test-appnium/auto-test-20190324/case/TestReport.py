import unittest
import time
import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
from utils.common import get_parent_path
from utils.HTMLTestRunner import HTMLTestRunner

if __name__ == "__main__":
    case_path = os.path.join(root_path, "case")
    print(case_path)
    report_path = os.path.join(root_path, "report")
    print(report_path)
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.path.join(report_path,"auto_result_"+now+".html")
    print(report_path)
    report_file = open(report_path,"wb")
    #
    runner= HTMLTestRunner(stream=report_file,title=u'自动化测试报告',description='执行测试结果')
    cases = unittest.defaultTestLoader.discover(case_path, pattern="Test*.py", top_level_dir=None)
    runner.run(cases)
    report_file.close()


