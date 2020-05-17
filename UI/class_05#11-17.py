# -*- coding: utf-8 -*-
#@Time      : 2020/5/13 21:54
#@Author    : hanchuang
#@Email     : 13032178760@163.com
#@File      : class_05#11-17.py
'''
JavaScript简单语法：
格式：<script></script>
变量表达：var 变量名=值
列表：var 列表名称=[值,值]--列表名称[下标]
字典：var 字典名称=[键：值,键：值]--字典名称.键
函数：function 函数名称（参数）{
       :return 值；
}
调用函数：函数名称（参数）

一、HTML DOM（网页和脚本语言之间沟通的桥梁）
js并不能直接访问和操作页面，需要html dom作为中介来访问页面，从而改变页面的结构，样式和内容
dom独立于平台和脚本语言（可以供多种脚本语言使用）
dom查找元素：
1.元素的id属性：
document.getElementById（）
document.getElementsByClassName（）
document.getElementsByTagName（）
document.getElementsByName（）
document.querySelector（css）

2.获取元素属性：
document.getElementByxxx（）.getAttribute(s属性名称)

3.设置元素属性
document.getElementByxxx（）.属性名称=属性值

4.更改元素内容--有后代
document.getElementByxxx（）.innerHTML=newHTML

5.更改元素内容--纯文本
document.getElementByxxx（）.innerText=newtext

6.改变样式
document.getElementByxxx（）.style.样式名称=样式值
例:document.getElementByxxx（）.style.color="red"
7.事件

二、selenium
from selenium import  webdriver
启动谷歌浏览器，开启与浏览器之间的会话
driver=webdriver.Chrome()

访问网址
driver.get("http://www.baidu.com")

窗口最大化
driver.maxmize_window()

回退上一页
driver.back()

前进
driver.forward()

刷新
driver,refresh()

获取标题
print(driver.title)

获取网址
print(driver.current_url)

窗口的句柄
print(driver.current_window_handle)

关闭当前浏览器窗口
driver.close()

结束会话
driver,quit()

三、元素定位
方式一--id
driver.find_element_by_id()
方式二--classname
driver.find_elements_by_class_name()
driver.find_element_by_class_name()
方式三--name
driver.find_elements_by_name()
driver.find_element_by_name()
方式四--tagname
driver.find_elements_by_tag_name()
driver.find_element_by_tag_name()
方式五、六--针对链接
driver.find_element_by_link_text()
driver.find_element_by_partial_link_text()
方式七--xpath
driver.find_element_by_xpath()
相对定位--相对路径，以//开头，不依赖页面的顺序和位置，只看页面中是否存在符合表达式的元素
绝对定位--绝对路径，以/开头，非常依赖页面的顺序和位置，不提倡使用
注：通过f12定位时，可以在elements页面通过ctrl+f显示查找框，在其中书写表达式来校验定位是否成功
表达式：//标签名称[@属性名称="属性值"]
注：
（1）如果使用多个属性，可以用and/or连接属性--逻辑运算
//标签名称[@属性名称="属性值" and/or @属性名称="属性值"]
（2）定位时也可以使用上级或者下级标签来辅助定位--层级运算
//标签名称[@属性名称="属性值"]/下级标签名称[@属性名称="属性值"]
（3）通过文本内容定位--使用函数
text（）函数
表达式：//标签名称[text()="文本内容"]
contains（）函数--包含函数
表达式1：//标签名称[contains（text（）,"文本内容"）]
表达式2：//标签名称[contains（@属性名称,"属性值内容"）]
（4）轴定位
轴名称：
ancestor:祖先解点，包括父节点
parent：父节点
preceding-sibling:当前元素节点标签之前的所有兄弟节点
following-sibling:当前元素节点标签之后的所有兄弟节点
使用语法：/轴名称::节点名称[@属性名称="属性值"]
例：//span[text()="文本内容"]/ancestor::a/following-sibling::div//a
方式八--css

四、事件
1.等待
强制等待
driver.sleep（秒）
隐形等待
driver.implicitly_wait(秒)
设置最长等待时间，在时间范围内容加载完成，则执行下一步，超过超过最长设置时间，然后抛出timeoutexception
在整个driver的会话周期内设置一次既可口，可全局使用
显性等待
webdriverwait(会话，等待时长，轮询周期).until()/until_not(期望条件)
常见期望条件；
presence_of_element_located:元素存在
visibility_of_element_located:元素可见
element_to_be_clickable:元素可点击
明确等待条件满足后，再执行下一步操作
程序会每隔几秒查看一下，如果条件满足了，便执行下一步，否则则继续等待，直到
超过最长设置时间，然后抛出timeoutexception
使用方法：
使用之前需要引入相关的库：
form selenium.webdriver.support.wait import webdriverwait
form selenium.webdriver.support import expected_conditions as ec
form selenium.webdriver.common.by import by
1.先确定元素的定位表达式
定位表达式="xxx"
2.调用webdriverwait类设置等待总时长，轮询周期，并调用unitl、until_not方法
webdriverwait(会话，等待时长，轮询周期).until()/until_not(期望条件)
3.使用expected_conditions对应的方法来生成判断条件
ec.期望条件类名（(by.定位方式、定位表达式)）
注：第三步内容可以直接放在until()/until_not()中

2.iframe切换
（1）进入另一个iframe
方式一：driver.switch_to.frame()
注：可通过frame下标（从1开始）、名称、页面元素来定位frame
切换后等待一下
方式二：ec.frame_to_be_available_and_switch_to_it(定位表达式)
（2）返回原来的页面
driver,switch_to.default_content()

3.窗口切换
方式一：
step1:获取窗口总数和句柄--放在引起窗口数量变化之前
handles=driver.window_handles
print(handles)
当前窗口句柄:
print(driver.current_window_handle)
step2:切换句柄
driver.switch_to.window(handles[下标])
方式二：
ec.new_window_is_opened()

4.alter切换--不是html页面元素
方式一：
alter=driver.switch_to.alter
关闭弹出框
alert.accept()
alter.dismiss()
打印弹出框内容
print(alter.text)
方式二：
ec.alter_is_present()
alter=driver.switch_to.alter









'''