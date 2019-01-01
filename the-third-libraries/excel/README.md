# 主要记载一些Excel操作
```python
# coding:utf-8

book = xlrd.open_workbook(file)
sh = book.sheet_by_index(0)
nrows = sh.nrows
# 得到具体的值
# rowx 是每一行，也就是横的
# colx 是每一列，也就是竖的
sh.cell_value(rowx=row,colx=1)

# 每一列可以使用一个数值表述，然后遍历每一行，就可以了。
```