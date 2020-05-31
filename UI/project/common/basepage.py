# -*- coding: utf-8 -*-
#@Time      : 2020/5/31 19:36
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : basepage.py
"""
1.封装基本函数--执行日志、异常处理、失败截图
2.所有的页面公共的部分

from selenium.webdriver.support.wait import webdriverwait
from selenium.webdriver.support import expected_conditions as ec
import logging
import datetime

class basepage:

    def__init__(self,driver):
        self.driver=driver

    等待元素可见
    def wait_elevisible(self,locator,times=30,poll_frequency=0.5,doc=""):
        '''
        param locator:元素定位。元组形式。（元素定位类型、元素定位方式）
        param times：
        param poll_frequency:
        param doc:模块名称_页面名称_操作名称
        return :none
        '''
        logging.info("等待元素{0}可见".format(locator))
        try:
            开始等待的时间
            start=datetime.datetime.now()
            webdriverwait(self.driver,times,poll_frequency).until(ec.visibility_of_element_located(locator))
            结束等待的时间
            end=datetime.datetime.now()
            求一个插值，写在日志中--等待了多久
            wait_times=(end-start).seconds
            logging.info("{0}:元素{1}已可见，等待起始时间：{2}，等待结束时间：{3}，等待时长为：{4}")
        except:
            logging.exception("等待元素可见失败！")
            截图
            self.save_screenshot(doc)
            raise

    等待元素存在
    def wait_elepresence(self):
        pass

    查找元素
    def get_element(self,locator，doc=""):
        logging.info("查找元素：{}"format(locator))
        try:
            return self.driver.find_element(*locator)
        except:
            logging.exception("查找元素失败！")
            截图
            self.save_screenshot(doc)
            raise

    点击操作
    def click_element(selflocator,doc=""):
        找元素
        ele=self.get_element(locator,doc)
        元素操作
        logging.info("{0}点击元素：{1}".format(locator,doc))
        try:
            ele.click()
        except:
            logging.exception("元素点击操作失败！")
            截图
            self.save_screenshot(doc)
            raise

    输入操作
    def input_text(self,locator,doc=""):
        找元素
        ele=self.get_element(locator,doc)
        输入操作
        try:
            ele.send_keys(text)
        except:
            logging.exception("元素输入操作失败！")
            截图
            self.save_screenshot(doc)
            raise

    获取元素的文本内容
    def get_text(self,locator,doc=""):
        找元素
        ele=self.get_element(locator,doc)
        try:
            return ele.text
        except:
            logging.exception("获取元素文本内容失败！")
            截图
            self.save_screenshot(doc)
            raise

    获取元素的属性
    def get_element_attribute(self,locator,attr,doc=""):
        找元素
        ele=self.get_element(locator,doc)
        try:
            return ele.get.atttibute(attr)
        except:
            logging.exception("获取元素属性失败！")
            截图
            self.save_screenshot(doc)
            raise

    alert处理
    def alert_action(self,action="accept"):
        pass

    iframe切换
    def switch_iframe(self,iframe_reference):
        pass

    上传操作
    def upload_file(self):
        pass

    滚动条处理

    窗口切换

    截图操作
    def save_screenshot(self，name):
        图片名称：模块名称_页面名称_操作名称_年-月-日_时分秒.png
        filepath=指定的图片保存目录/model(页面功能名称)_当前时间到秒.png
        filepath=dir_config.screenshot_dir+\
        "/{0}_{1}.png".format(doc,tome.strftime(%y-%m-%d-%h-%m-%s,time.localtime()))
        截图文件存放在screenshot目录下
        driver方法：self.driver.save_screenshot(）
        try:
            self.driver.save_screenshot(filepath）
            logging.info("截屏成功。图片路径为{0}".format(filepath))
        except:
            logging.exception("截图失败")



"""