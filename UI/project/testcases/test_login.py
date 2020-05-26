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

    def setupclass(cls):
        通过excel读取本功能中需要的所有测试数据
        pass

    def setup(self):
        前置 访问登陆页面
        self.driver=wedriver.chrome()
        self.driver.get("网址")
        lg=loginpage(self.driver)

    def teardown(self):
        后置 关闭浏览器
        self.driver.quit()

    正常用例-登陆成功
    def test_login_success(self):
        步骤 输入用户名和密码
        self.lg.login(ld.success_data["user"],ld.success_data["passwd"])
        断言 首页找到特定元素  //a[@href="/index/logout.html"]
        self.asserttrue(indexpage(self.driver).isexist_logout_ele())


    异常用例-手机号码格式不正确（大于11位、小于11位、为空、不在号码段）  ddt
    @ddt.data(*ld.phone_data)
    def test_login_user_wrongformat(self,data):
        步骤 输入用户名和密码
        self.lg.login(data["user"],data["passwd"])
        断言 登陆页面提示：请输入正确的手机号
        比对文本内容与期望的值是否相等
        self.assertequal(self.lg.get_errormsg_from_loginarea(),data["check"])



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