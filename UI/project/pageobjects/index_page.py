# -*- coding: utf-8 -*-
#@Time      : 2020/5/26 22:51
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : index_page.py
"""
from selenium.webdriver.support import expected_conditions as ec
from common.basepage import basepage
import random


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

    选标操作
    默认选第一个=元素定位得时候，过滤调不可以投的标
    def click_first_bid(self):
        webdriverwait(self.deriver,10).until(ec.visibility_of_element_located((loc.bid_button)))
        self.driver.find_element(*loc.bid_button).click()

    随机选择一个标
    def click_did_by_random(self):
        webdriverwait(self.deriver,10).until(ec.visibility_of_element_located((loc.bid_button)))
        eles=self.driver.find_elements(*loc.bid_button)
        随机数
        index=random.randint(0,len(eles)-1)
        eles[index].click()



"""