# coding: utf-8 
import re 

# 首先是正则表达式的规则
# 其次是python正则表达式的方法
text = 'I have an pen 1234'
s = re.search('.*?(\d+)',text,re.I)
print(s.group(0))
print(s.group(1))

s = re.match('I(.*)',text,re.I)
print(s.group(0))
print(s.group(1))

text = 'I have an  have pen 1234'
s = re.findall('\w+',text,re.I)
print(s) # ['I', 'have', 'an', 'pen', '1234']

s = re.sub('have',"Hello",text,flags=re.I,count=1)
print(s) # I Hello an  have pen 1234