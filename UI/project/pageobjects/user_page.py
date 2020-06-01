# -*- coding: utf-8 -*-
#@Time      : 2020/5/30 19:56
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : user_page.py
"""


class userpage(basepage):

    获取用户余额
    def get_user_leftmoney(self):
        doc="个人页面_获取用户余额"
        等待元素
        self.wait_elevisible(loc.user_leftmoney.doc=doc)
        获取个人可用余额的文本内容
        text=self.get_text(loc.user_leftmoney,doc)
        截取数字部分--分隔符为 元
        return text.strip("元")

    获取第一条投资记录的时间、投资金额、收益余额--扩展
    def get_first_investrecord_info(self):
        pass






"""