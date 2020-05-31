# -*- coding: utf-8 -*-
#@Time      : 2020/5/26 22:51
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : login_page.py
"""
from pagelocator.loginpage_locators import loginpagelocator as loc
from common.basepage import basepage

class LoginPage(basepage):

    登陆操作
    def login(self，username.passwd,remeber_user=true):
        输入用户名
        输入密码
        点击登陆
        doc="登陆页面_登陆功能"
        self.wait_elevisible(loc.user_input,doc=doc)\
        self.input_text(loc.user_input,username,doc)
        self.input_text(loc.passwd_input,passwd,doc)
        判断一下remeber_user的值，来决定是否勾选
        self.click_element(loc.login_button,doc)

    获取错误提示信息--登陆区域
    def get_errormsg_from_loginarea(self):
        doc="登陆页面_获取登陆区域的错误提示"
        self.wait_elevisible(loc.form_error_info,doc=doc)
        return self.get_text(loc.form_error_info,doc)

    获取错误信息--页面正中间
    def get_errornag_from_pagecenter(self):
        doc="登陆页面_获取页面正中间的错误提示"
        self.wait_elevisible(loc.pagecenter_error_info,poll_frequency=0.2,doc=doc)
        return self.get_text(loc.pagecenter_error_info,doc)

    忘记密码

    注册入口
    def register_enter(self):
        webdriverwait(self.driver,20).until(ec.visibility_of_element_located((by.xpath,"")))
        self.driver.find_element_by_xpath("").click()




"""