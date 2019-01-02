text 包含四个部分
1. string
2. textwrap
3. re
4. difflib


str 无疑是text中用的最多的模块，除此之外还有以上四个模块用于高级操作
# 如何转换类似 '\\u0062' 这样的字符？
```
'\\u0062'.encode('utf-8').decode('unicode-escape')
```
