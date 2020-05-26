# -*- coding: utf-8 -*-
#@Time      : 2020/5/26 22:51
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : index_page.py
"""
from selenium import webdriver
from selenium.webdriver.support.wait import webdriverwait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import by
import time

class LoginPage:

    def__init__(self,driver):--page类中不需要单独打开浏览器
    self.driver=driver

    def isexist_logout_ele(self):
    如果存在就返回true，如果不存在，就返回false
    try:
        webdriverwait(self.driver,10).until(ec.visibility_of_element_located((by.xpath,"//a[@href="/index/logout.html"]")))
        return true
    except:
        return false



"""