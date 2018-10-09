# 一些关于字符的小trick

# 如何转换类似 '\\u0062' 这样的字符？

```
'\\u0062'.encode('utf-8').decode('unicode-escape')
```
