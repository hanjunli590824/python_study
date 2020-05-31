# -*- coding: utf-8 -*-
#@Time      : 2020/5/31 23:08
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : main.py
"""
import unittest
import os
form htmltestrunnernew import htmltestrunner
from common.dir_config import *

实例化套件对象
s=unittest.testsuite()
testloader的用法
1.实例化testloader对象
2.使用discover去找到一个目录下的所有测试用例
3.使用s
loader=unittest.testloader()
s.addtests(loader.discover(testcase_dir))
# 运行
# runner=unittest.texttestrunner()
# runner.run(s)

fp=open(htmlreport_dir+"/autotest_report.html","wb")
runner=htmltestrunner(
            stream=fp,
            title="单元测试报告"
            description="单元测试报告"
            tester="lance"
            ）
runner.run(s)




"""