# -*- coding: utf-8 -*-
#@Time      : 2020/5/30 18:39
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : test_invest.py
"""
独立的测试账号
###############尽量不要依赖环境数据##################
前提：
1、用户已登录
2、有能够投资的标--如果没有标，则先加标--接口的方式加标
3.用户有余额可以投资
    1.充很多钱
    2.接口方式：查询当前用户的余额，如果够，不用充值，否则，充值

步骤：
1.在首页选标--不根据标名，根据抢投标，默认第一个标
2.标页面--获取投资前的用户余额
3.标页面--输入投资金额，点击投资按钮
4.标页面--点击投资成功的弹出框--查看并激活，进入个人页面

断言：
钱--投资后的金额，是不是少了投资的量
1.个人页面--获取投资后的金额
2.投资金额=投资前的金额-投资后的金额
3.投资记录对不对
注：
异常用例：非常好创造  环境，非常好写的
异常用例：--这些比较麻烦或者执行以后会影响到其他用例的用例可手工执行，不一定非要转化成自动化用例
1.全投操作--标的可投金额>个人金额
2.投资金额>标的可投金额


import unittest
from selenium import webdriver
from pageobjects.bid_page import bidpage
from pageobjects.index_page import indexpage
from testdatas import common_datas as cd
from testdatas import invest_datas as id
import ddt

@ddt.ddt
class testinvest(unitest.testcase):

    @classmethod
    def setupclass(cls):
        初始化浏览器会话
        logging.info("===用例类前置：初始化浏览器会话，登陆前程贷系统===")
        cls.driver=webdriver.chrome()
        cls.driver.maximize_window()
        cls.driver.get(cd.web_login_url)
        cls.driver.get(cls.driver).login(cd.user,cd.passwd)
        首页--选一个标--直接选择第一个标---/随机选一个
        indexpage(cls.driver).click_first_bid()
        cls.bid_page=bidpage(cls.driver)

    @classmethod
    def teardownclass(cls):
        logging.info("===用例类后置：关闭浏览器会话，清理环境===")
        cls.driver.quit()

    def teardown(self):
        logging.info("===每个用例后置：刷新当前页面===")
        self.driver.refresh()
        time.sleep(0.5)

    def test_invest_success(self):
        步骤
        logging.info("***投资用例：正常场景-投资成功***")
        标页面--获取投资前的用户余额
        usermoney_beforeinvest=self.bid_page.get_user_money()
        标页面--输入投资金额，点击投资按钮
        self.bid_page.invest(id.success["money"])
        标页面--投资成功的弹出框,点击查看并激活按钮
        self.bid_page.click_activebutton_on_success_popup()
        验证
        个人页面--获取用户当前的金额
        usermoney_afterinvest=userpage(self.driver).get_user_leftmoney()
        余额：投资前获取一下，投资后再获取一下。求差值，如果等于投资金额，则正确
        assert id.success["money"]==int(float(usermoney_beforeinvest)-float(usermoney_afterinvest))

    @ddt.data(*id.wrong_format_money)
    def test_invest_0_failed_by_no100(self,data):
        logging.info("***投资用例：异常场景：投资金额为非100的整数倍、错误的格式等***")
        标页面--获取投资前的个人余额
        usermoney_beforeinvest=self.bid_page.get_user_money()
        标页面--输入投资金额，点击投标按钮
        self.bid_page.invest(data["money"])
        获取提示信息
        errormsg=self.bid_page.get_errormsg_from_pagecenter()
        刷新
        self.driver.refresh()
        获取用户余额
        usermoney_afterinvest=self.bid_page.get_user_money()
        断言
        assert errormsg==data["check"]
        assert usermoney_afterinvest==usermoney_beforeinvest

    def test_invest_failed_no10(self):
        pass














"""
