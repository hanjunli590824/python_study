# -*- coding: utf-8 -*-
#@Time      : 2020/5/26 22:52
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : test_login.py
"""
import unittest
from selenium import webdriver
from pageobjects.login_page import loginpage
from pageobjects.index_page import indexpage
from testdatas import common_datas as cd
from testdatas import login_datas as ld
import ddt

@ddt.ddt
class testlogin(unittest.testcast):

    @classmethod
    def setupclass(cls):
        cls.driver=wedriver.chrome()
        cls.driver.get("网址")
        cls.lg=loginpage(cls.driver)

    @classmethod
    def teardownclass(cls):
        cls.driver.quit()

    def setup(self):
        pass

    def teardown(self):
        self.driver.refresh()

    正常用例-登陆成功
    def test_login_1_success(self):
        步骤 输入用户名和密码
        self.lg.login(ld.success_data["user"],ld.success_data["passwd"])
        断言 首页找到特定元素  //a[@href="/index/logout.html"]
        self.asserttrue(indexpage(self.driver).isexist_logout_ele())


    异常用例-手机号码格式不正确（大于11位、小于11位、为空、不在号码段）  ddt
    @ddt.data(*ld.phone_data)
    def test_login_0_user_wrongformat(self,data):
        步骤 输入用户名和密码
        self.lg.login(data["user"],data["passwd"])
        断言 登陆页面提示：请输入正确的手机号
        比对文本内容与期望的值是否相等
        self.assertequal(self.lg.get_errormsg_from_loginarea(),data["check"])

    def test_login_wrongpwd_noreg(self):--仿照上面
        步骤 输入用户名和密码  点击登陆
        断言 登陆页面 页面正中间提示：xxx
        登陆页面中--获取提示框的文本内容
        比对文本内容与期望的值是否相等


    异常用例-用户名为空
    def test_login_nouser(self):
        步骤 输入用户名和密码
        self.lg.login("","密码")
        断言 登陆页面提示：
        登陆页面中--获取提示框的文本内容



    异常用例-未注册手机号
    异常用例-错误的密码
    异常用例-不输入密码


"""