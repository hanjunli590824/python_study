# -*- coding: utf-8 -*-
#@Time      : 2020/5/26 23:36
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : login_datas.py
"""
正常场景--测试数据
success_data={"user":"18684720553","passwd":"python"}

异常场景--手机号码格式不正确（大于11位、小于11位、为空、不在号码段）
phone_data=[
    {"user":"186847205","passwd":"python","check":"请输入正确的手机号"},
    {"user":"18684720553123","passwd":"python","check":"请输入正确的手机号"},
    {"user":"","passwd":"python","check":"请输入手机号"},
    {"user":"11684720553","passwd":"python","check":"请输入正确的手机号"}
]

异常场景


"""