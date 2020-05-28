# -*- coding: utf-8 -*-
#@Time      : 2020/5/26 22:51
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : login_page.py
"""
from selenium import webdriver
from selenium.webdriver.support.wait import webdriverwait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import by
import time
from pagelocator.loginpage_locators import loginpagelocator as loc

class LoginPage:

    def__init__(self,driver):--page类中不需要单独打开浏览器
    self.driver=driver

    登陆
    def login(self，username.passwd,remeber_user=true):
        输入用户名
        输入密码
        点击登陆
        webdriverwait(self.driver,20).until(ec.visibility_of_element_located(loc.name_text))
        self.driver.find_element(*loc.name_text).send_keys(username)
        self.driver.find_element(*loc.pwd_text).send_keys(passwd)
        判断一下remeber_user的值，来决定是否勾选
        self.driver.find_element(*loc.login_but).click()

    注册入口
    def register_enter()
        webdriverwait(self.driver,20).until(ec.visibility_of_element_located((by.xpath,"")))
        self.driver.find_element_by_xpath("").click()


    获取错误提示信息--登陆区域
    def get_errormsg_from_loginarea(self):
    webdriverwait(self.driver,20).until(ec.visibility_of_element((by.xpath,"//div[@class="form-error-info"]")))
    return self.driver.find_element_by_xpath("//div[@class="form-error-info"]").text

    获取错误信息--页面正中间
    def get_errornag_from_pagecenter(self):
    webdriverwait(self.driver,20).until(ec.visibility_of_element((by.xpath,"//div[@class="layui-layer-content"]")))
    return self.driver.find_element_by_xpath("//div[@class="layui-layer-content"]").text


    忘记密码





"""