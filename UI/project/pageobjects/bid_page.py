# -*- coding: utf-8 -*-
#@Time      : 2020/5/30 19:55
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : bid_page.py
"""
from pagelocator.loginpage_locators import loginpagelocator as loc
from common.basepage import basepage

class bidPage(basepage):

    投资
    def invest(self,money):
        在输入框中，输入金额
        doc="标详情页面_投资操作
        self.wait_elevisible(loc.money_input,doc)
        self.input_text(loc.money_input,money,doc)
        点击投标按钮
        self.click_element(loc.money_input,doc)

    获取用户余额
    def get_user_money(self):
        webdriverwait(self.deriver,30).until(ec.visibility_of_element_located((loc.money_input)))
        return self.driver.find_element(*loc.money_input).get_attribute("data-amount")

    投资成功的提示框--点击查看并激活
    def click_activebutton_on_success_popup(self):
        webdriverwait(self.deriver,30).until(ec.visibility_of_element_located((loc.active_button_on_successpop)))
        self.driver.find_element(*loc.active_button_on_successpop).click()

    错误提示框--页面中间
    def get_errormsg_from_pagecenter(self):
        获取文本内容
        webdriverwait(self.deriver,30).until(ec.visibility_of_element_located((loc.invest_failed_popup)))
        msg=self.driver.find_element(*loc.invest_failed_popup).text
        关闭弹出框
        self.driver.find_element(*loc.invest_close_failed_popup_button).click()
        return msg

    获取提示信息--投标按钮上面的
    def get_errormsg_from_investbutton(self):
        pass




"""