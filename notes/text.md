# 概述
str 无疑是python最常用的字符串处理模块，除此之外还有一些补充 str 功能的第三方模块
比如 string 模块，有template函数，有一些字符串属性
比如 re 模块，主要用于字符串的匹配
# str 模块
可以直接使用 help(str) 查看其支持的函数
```py
s = "hello world"
print(s.capitalize())
print(s.casefold()) 
print(s.count('h')) # 1
print(s.find('llo')) #2
print(s.index('lo')) # 3
print(s.join(['john','www'])) # johnhello worldwww
print(s.replace('lo','rl'))
print(s.splitlines())
print(s.title()) # 首字母大写
print(s.zfill(10))
print(s.strip()) 
print(s.lower())
print(s.upper())
```
爬虫的时候，如果遇到需要转码的时候，可以使用
```py
'\\u0062'.encode('utf-8').decode('unicode-escape')
```
# string 模块
string模块主要使用的还是其template的功能，一个简单的例子：
```py
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
```
可以看到template处理的是多行字符串，但是这个在 str 模块，也可以使用format来进行转换，所以并没有什么卵用，如果只是格式化输出字符串，不管多行还是单行，使用 format，才是最简单方便的做法
```py
# 结合format 进行使用
t2 = """
Variable : {var}
Escape : {{}}
Variable in text : {var}iable
"""
print("format: ",t2.format(**values))
```
除此之外，Template  还存在高级的功能，可以通过自定义规则，来实现一个字符串中，有的格式化，有的不格式化.当然个人感觉也没有什么用。只做一个了解
```py

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
```
经过上面的实验，string这个模块可有可无，但是string 还提供了一些属性倒是可以方便我们写代码的时候引用，你可以使用
```py
ascii_letters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
ascii_lowercase='abcdefghijklmnopqrstuvwxyz'
ascii_uppercase='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits='0123456789'
hexdigits='0123456789abcdefABCDEF'
octdigits='01234567'
printable='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'
punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
whitespace=' \t\n\r\x0b\x0c'
```
比如你想写一个程序，随机生成高强度代码，那么你就可以使用下面的属性，很方便的写出来
```py
import random
def generate_passwd():
    uppercase_wd =random.choices(string.ascii_uppercase,k=random.randint(3,6)) 
    lowercase_wd = random.choices(string.ascii_lowercase,k=random.randint(3,6))
    digits_wd = random.choices(string.digits,k=random.randint(3,6))
    punctuation_wd = random.choices('!@#$%^&*()[<>?]',k=random.randint(3,6))
    a = uppercase_wd+lowercase_wd+digits_wd+punctuation_wd
    random.shuffle(a)
    print(''.join(a))
```

# re 模块
正则表达式的写法在网上一搜一大堆，可以集合一些比较常用的，需要的时候可以省去搜索的时间。
python中的re模块一共有以下几种函数可以使用
## re.search(pattern,string,flags=0)
搜索所有的字符串，匹配到内容返回，否则返回None
```py
import re
text = 'I have an pen 1234'
s = re.search('.*?(\d+)',text,re.I)
print(s.group(0))
print(s.group(1))
```
## re.match(pattern,string,flags=0)
只匹配开头就符合的字符串, 如果不是开头第一个字符就符合，返回None
```py
import re
s = re.match('I(.*)',text,re.I)
print(s.group(0))
print(s.group(1))
```
## re.split(pattern,string,maxsplit=0,flags=0)
根据正则切割字符串
```py
>>> re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE)
['0', '3', '9']
```
## re.findall(pattern,string,flags=0)
找到符合的字符串，返回一个列表
```py
text = 'I have an pen 1234'
s = re.findall('\w+',text,re.I)
print(s) # ['I', 'have', 'an', 'pen', '1234']
```

## re.sub(pattern,replace_content,string,count=0,flags=0)
替换字符串,返回一个字符串
```
s = re.sub('have',"Hello",text,re.I)
print(s) # I Hello an pen 1234
```

这里有一个count，如果count = n 意思是如果找到多个可替换的字符，只替换前n个

```py
s = re.sub('have',"Hello",text,flags=re.I,count=1)
print(s) # I Hello an  have pen 1234
```

## re.subn(pattern,repl,string,count=0,flags=0)
替换字符,但是返回的式tuple
```py
s = re.subn('have',"Hello",text,re.I)
print(s) # ('I Hello an  Hello pen 1234', 2)
```


## re.escape(pattern)
返回一个转义的字符
```py
>>> print(re.escape('python.exe'))
python\.exe
```


# 参考
《The Python3 Standard Library By Example》
常见的正则表达式： https://juejin.im/entry/5686056160b2e495ddd8b9a5  