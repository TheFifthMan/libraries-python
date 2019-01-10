# coding: utf-8 
# string 文件内容和模板
# string 模块出现在最早版本的 python 中，如今大多数的函数已经迁移到了str 中
# 但是还有维护一些高级的功能 

# Functions
import string
s = "The quick brown fox jumped over the lazy dog"
print(s)
print(string.capwords(s)) # 首字母大写

# Templates
values = {'var':'foo'}
t = string.Template("""
Variable : $var
Escape : $$
Variable in text : ${var}iable
""")
# $var 变量
# $$ 如果要输出 $，要用$进行转义
# ${var} 变量
print("Templates:",t.substitute(values))

# 结合format 进行使用
t2 = """
Variable : {var}
Escape : {{}}
Variable in text : {var}iable
"""
print("format: ",t2.format(**values))
# 如果提供了一个变量，但是没有赋值，那么会抛出一个keyerror的错。

# Advanced Templates
# 我们还可以使用正则表达式来决定哪些值要替换，哪些值无需替换
class MyTemplates(string.Template):
    delimiter = '%'
    idpattern = '[a-z]+_[a-z]+'

text = """
replaced: %need_replace
ignored: %ignored
"""
d = {
    'need_replace': "Haha replaced",
    "ignored": "hh ignored"
}
t = MyTemplates(text)
print(t.safe_substitute(d))
# 符合正则表达式，并且前面有一个 % 就成功替换了，否则就没有成功替换
# 不过这个好像没什么用

# 除此之外，string 还有一些属性
'''
ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVW
XYZ'
ascii_lowercase='abcdefghijklmnopqrstuvwxyz'
ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits='0123456789'
hexdigits='0123456789abcdefABCDEF'
octdigits='01234567'
printable='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQ
RSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
whitespace=' \t\n\r\x0b\x0c'
'''


def covert(values):
    text = """
    Variable : {var}
    Escape : {{var}}
    Variable in text : {var}iable
    """
    print("format: ",text.format(**values))

import random
def generate_passwd():
    uppercase_wd =random.choices(string.ascii_uppercase,k=random.randint(3,5)) 
    lowercase_wd = random.choices(string.ascii_lowercase,k=random.randint(3,6))
    digits_wd = random.choices(string.digits,k=random.randint(3,6))
    punctuation_wd = random.choices('!@#$%^&*()[<>?]',k=random.randint(3,4))
    a = uppercase_wd+lowercase_wd+digits_wd+punctuation_wd
    random.shuffle(a)
    print(''.join(a))


if __name__ == "__main__":
    generate_passwd()