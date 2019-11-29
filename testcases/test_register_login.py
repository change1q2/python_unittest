import os
import unittest
from common.contants import DATA_DIR
from login_register.login import login_check
from login_register.register import register
from common.readexcel import ReadExcel
from library.ddt import ddt, data
from common.mylogger import my_log
file_path = os.path.join(DATA_DIR,"cases.xlsx")#引入os模块，解决路径问题
# 定义登录的测试用例类
@ddt  # @ddt 做的事情等同于这句代码==> LoginTestCase = ddt(LoginTestCase)
class LoginTestCase(unittest.TestCase):
    excel = ReadExcel(file_path, "login")
    cases = excel.read_data()

    @data(*cases)
    def test_login(self, case):
        # 第一步：准备用例的执行的数据
        case_data = eval(case["data"])
        expected = eval(case["expected"])
        case_id = case["case_id"]
        # 第二步：调用功能函数，获取实际结果
        result = login_check(*case_data)

        # 第三步：比对实际结果和预期结果
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            # 用例执行未通过
            self.excel.write_data(row=case_id + 1, column=5, value="未通过")
            my_log.info("用例：{}--》执行未通过".format(case["title"]))
            my_log.error(e)
            raise e
        else:
            my_log.info("用例：{}--》执行通过".format(case["title"]))
            self.excel.write_data(row=case_id + 1, column=5, value="通过")


@ddt
class RegisterTestCase(unittest.TestCase):
    excel = ReadExcel(file_path, "register")
    cases = excel.read_data()

    @data(*cases)
    def test_register(self, case):
        # 第一步：准备用例的执行的数据
        case_data = eval(case["data"])
        expected = eval(case["expected"])
        case_id = case["case_id"]
        # 第二步：调用功能函数，获取实际结果
        result = register(*case_data)

        # 第三步：比对实际结果和预期结果
        try:
            self.assertEqual(expected, result)
        except AssertionError as e:
            # 用例执行未通过
            self.excel.write_data(row=case_id + 1, column=5, value="未通过")
            my_log.info("用例：{}--》执行未通过".format(case["title"]))
            my_log.error(e)
            raise e
        else:
            my_log.info("用例：{}--》执行通过".format(case["title"]))
            self.excel.write_data(row=case_id + 1, column=5, value="通过")
