"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：启动文件
============================
"""

import unittest
from library.HTMLTestRunnerNew import HTMLTestRunner

# 第一步：创建测试套件
suite = unittest.TestSuite()

# 第二步加载用例到套件
loader = unittest.TestLoader()
suite.addTest(loader.discover(r"E:\py24_unittest\testcases"))


# 第三步：创建一个测试用例运行程序

report_path = (r"E:\py24_unittest\report\report.html")

with open(report_path,"wb") as f:
    runner = HTMLTestRunner(stream=f,
                   title="24期的测试报告",
                   description="测试报告的描述信息",
                   tester="seak"
                   )
    # 第一步：运行测试套件
    runner.run(suite)
