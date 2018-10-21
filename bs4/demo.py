#coding:utf-8 
# 简单的例子
# 以爬取bookdl为例子
import requests
from bs4 import BeautifulSoup
res = requests.get(url)
html = res.text
# 初始化，指定解析器，默认是html.parser
soup = BeautifulSoup(html,"html.parser")
p = soup.find_all('p')
