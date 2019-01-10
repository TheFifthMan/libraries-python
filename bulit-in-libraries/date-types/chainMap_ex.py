import collections
## 赋值，合并字典的作用
a = {'a':"A"}
b = {"b":"B"}

m = collections.ChainMap(a,b)
for k,v in m.items():
    print('key: {} | value:{}'.format(k,v))

print(m)
## 如果有重复的值
a = {"a":"A","b":"B"}
b = {"b":"C"}
m2 = collections.ChainMap(a,b)
print(m2)

for k,v in m2.items():
    print('key: {} | value:{}'.format(k,v))

'''
输出：
ChainMap({'a': 'A', 'b': 'B'}, {'b': 'C'})
key: a | value:A
key: b | value:B

结论：
结果是没有合并，如果只是合并字典的值，还是直接使用update即可
'''
