# coding:utf-8 
# selenium的基础用法

# 使用绝对路经的方式
# name = os.path.dirname(os.path.abspath(__file__))
# print(os.path.join(name,'chromedriver.exe'))


from selenium import webdriver
import os 
# demo 
driver = webdriver.Chrome(executable_path='C://project//libraries-python//selenium//chromedriver.exe')
driver.get('https://www.baidu.com')
print(driver.title)

