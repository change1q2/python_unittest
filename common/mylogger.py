"""
============================
作者:seak
时间:
邮件:274882401@qq.com
作用：
题目：日志封装一个可以创建日志收集器的函数
============================
要把一个一般函数放在类里面一般使用静态方法
"""
import logging

class MyLogger(object):

    @staticmethod #要把一个一般函数放在类里面一般使用静态方法
    def creat_logger():
        # 一、创建一个名为：python24的日志收集器
            my_log = logging.getLogger("python24")

        # 二、设置日志收集器的等级
            my_log.setLevel("DEBUG")

        # 三、添加输出渠道（输出到控制台）
            # 1、创建一个输出到控制台的输出渠道
            sh = logging.StreamHandler()
            # 2、设置输出等级
            sh.setLevel("ERROR")
            # 3、将输出渠道绑定到日志收集器上
            my_log.addHandler(sh)

            # 四、添加输出渠道（输出到文件）
            fh = logging.FileHandler(r"E:\py24_unittest\log\test.log", encoding="utf8")
            fh.setLevel("DEBUG")
            my_log.addHandler(fh)

            # 五、设置日志输出的格式
            # 创建一个日志输出格式
            formatter = logging.Formatter('%(asctime)s - [%(filename)s-->line:%(lineno)d] - %(levelname)s: %(message)s')
            # 将输出格式和输出渠道进行绑定
            sh.setFormatter(formatter)
            fh.setFormatter(formatter)

            return my_log

    # 调用类的静态方法，创建一个日志收集器
my_log = MyLogger.creat_logger()
