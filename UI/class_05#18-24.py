# -*- coding: utf-8 -*-
#@Time      : 2020/5/19 22:44
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : class_05#18-24.py
'''
鼠标操作--使用actionchains类模拟鼠标操作
支持的操作：
double_click 双击
context_click 右键
drag_and_drop 拖拽
move_to_element() 鼠标悬停
perform（）  实现动作

引入actionchains类：
from selenium.webdriver.common.action_chains import actionchains
先找到鼠标要操作的元素
ele=driver.find_element_by_xpath('元素定位')
实例化actionchains类
ac=actionchains(driver)
将鼠标操作添加到actions列表中
ac.move_to_element(ele)
调用perform()来执行鼠标操作
ac.preform()

下拉列表
1.非select下拉框
快捷键：ctrl+shift+c 定位下拉框选项
2.select下拉框--select类
选择下拉列表的值：
1.select_by_index(index)--通过下表值，从0开始
2.select_by_value（value值）--通过value值
3.select_by_visible_text(文本内容)--通过文本内容

引入类：from selenium.webdriver,support.ui import select
找到select元素
select_ele=driver.find_element_by_xpath('定位内容')
 实例化select类
 s=select(select_ele)
选择下拉列表值
方式一：s.select_by_index(下表值)
方式二：s.select_by_value('value属性值')
方式三：s.select_by_visible_text('文本内容')

键盘操作
引入库：from selenium.webdriver.common.keys import keys

元素基本操作：
send_keys()
click()
定位.text--获取文本内容
定位内容.get_attribute("属性名称")--获取元素属性值

JS处理
滚动条操作
1.移动到元素element对象的“底端”与当前窗口的“底部”对齐
driver.execute_script("arguments[0].scrollintoview(false);",element)
2.移动到元素element对象的“顶端”与当前窗口的“顶部”对齐
driver.execute_script("arguments[0].scrollintoview();",element)
3.移动到页面底部
driver.execute_script("window.scrollto(0，document.body.scrollheight)")
4.移动到页面顶部
driver.execute_script("window.scrollto(document.body.scrollheight,0)")
操作：
1.找到要滚动到可视区域的元素
2.使用js进行滚动操作

针对只读属性的控件--选择时间框控件
首先在页面console中把js调试通过，然后把js复制下来赋给变量
js='var ele=document.getelementbyid("定位内容");ele.readonly=false;ele.value="2020-05-24";'
driver.execute_script(js)

上传操作
注：选择文件窗口时window系统的，不是html页面和浏览器的，需要其他工具辅助定位
第一种情况：如果时input可以直接输入路径的，那么直接调send_keys输入路径
第二种情况：非input标签的上传，需要借助第三方工具--python pywin32库，识别对话框句柄，进而操作
工具：pywin32库和spy++
安装pywin32库和spy++，使用spy++对文件选择窗口进行定位，然后用python代码时间定位
第一步：引入库：import win32gui
import win32con
第二步：定位文件名称输入框：
定位文件名称输入框:
dialog=win32gui.findwindow("window窗口的类名称（class）","window窗口的名称（title）")
comboxex32=win32gui.findwindowex(父级,0（遍历）," 要定位的类名称",对应的文本内容（text，如果无则为none）)
下面以此类推，一直定位到最终的定位目标
定位打开按钮：
button=win32gui.findwindowex(父级,0（遍历）," 要定位的类名称","打开（&0）")
第三步：发送文件路径
win32gui.sendmessage(edit,win32con.wm_settext,none,"文件路径")
第四步：点击打开按钮
win32gui.sendmessage(dialog,win32con.wm_command,1,button)

1.已经有了接口自动化，为什么还要做ui自动化？
客户直接接触前端，前端也有一些逻辑，要保证前端的功能正常
2.ui自动化的用处
回归，节省时间
解放双手
3.做ui自动化的条件
项目周期比较长（一年以上），功能越来越复杂
系统功能比较稳定了
业务功能不要偏向数据

过程：
1，熟悉业务--需求文档/手动测试/产品聊，了解模块之间的关系/测试聊，项目目前的阶段，棘手的问题
2.分析筛选模块--哪些模块比较适合自动化（核心模块、使用频率高的模块、稳定性、功能复杂性、bug率高的模块）
3.分析筛选测试用例--筛选自动化测试用例（核心功能、主流程、主功能点）
4.自动化测试计划--前三步的工作内容和原因、自动化类型（web/api）、选择框架（根据团队的水平）、团队人员、搭框架（分层级）、
定规范（代码）、时间规划（用例编写时间..）、效果（覆盖率、用例通过率）

把功能测试用例转化成自动化测试用例--预期结果一定要具体清楚
测试用例内容--前置、步骤、断言

页面对象模型（po模式）--分层设计思想--提高代码复用、好维护、易修改
pageobject（页面对象）--把每个页面的元素定位和元素行为封装成一个page类
页面对象和测试用例分离

架构：
pageobjects（page类）包：
login_page.py
index_page.py
testcases（测试用例）包：
test_login.py


登陆页面page类：
from selenium import webdriver
from selenium.webdriver.support.wait import webdriverwait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import by
import time

class LoginPage:

    def__init__(self,driver):--page类中不需要单独打开浏览器
    self.driver=driver

    登陆
    def login(self，username.passwd,remeber_user=true):
        输入用户名
        输入密码
        点击登陆
        name_text='//input[@name="phone"]'
        pwd_text='//input[@name="password"]'
        login_but='//button[@text()="登陆"]'
        webdriverwait(self.driver,20).until(ec.visibility_of_element_located((by.xpath,name)))
        self.driver.find_element_by_xpath(name_text).send_keys(username)
        self.driver.find_element_by_xpath(pwd_text).send_keys(passwd)
        判断一下remeber_user的值，来决定是否勾选
        self.driver.find_element_by_xpath(login_but).click()

        pass

    注册入口
    def register_enter()
        webdriverwait(self.driver,20).until(ec.visibility_of_element_located((by.xpath,"")))
        self.driver.find_element_by_xpath("").click()
        pass

    忘记密码

登陆测试用例：
import unittest
from selenium import webdriver
from pageobjects.login_page import loginpage
class testlogin(unittest.testcast):
    dif setup(self):
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
        self.lg.login("账号","密码")
        断言 首页找到特定元素
        等待10秒
        找元素 //a[@href="/index/logout.html"]
        self.driver.find_element_by_xpath('//a[@href="/index/logout.html"]')
        pass

    异常用例-手机号码格式不正确
    def test_login_user_wrongformat(self):
        步骤 输入用户名和密码
        self.lg.login("不正确账号","密码")
        断言 登陆页面提示：
        pass

    异常用例-用户名为空
    def test_login_nouser(self):
        步骤 输入用户名和密码
        self.lg.login("","密码")
        断言 登陆页面提示：
        pass

    异常用例-未注册手机号
    异常用例-错误的密码
    异常用例-未注册手机号










'''
