a = {"a":"A","b":"B"}
b = {"a":"C","d":"D"}
import collections
m = collections.ChainMap(a,b)
print(m['a']) # 显示 A

# Counter 用法
c = collections.Counter('Hello World')
print(c) # 返回 Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})
print(c['H'])

# 双端队列
# 双端队列两边既可以插入也可以弹出，具有队列和栈的双重特点
d = collections.deque("abcdefg")
print(d)
print(len(d))
print(d[0])
print(d[-1])
# 因为也是序列的一种，因此，也拥有序列的一些方法
# 右边插入
d.extend('poiuy')
print(d) # 右边插入 deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'p', 'o', 'i', 'u', 'y']) 
d.append('right')
print(d) # deque(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'p', 'o', 'i', 'u', 'y', 'right'])
# 左边插入
d.extendleft("rigth")
print(d) # deque(['h', 't', 'g', 'i', 'r', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'p', 'o', 'i', 'u', 'y', 'right'])
d.appendleft('abcd')
print(d)
# 弹出
print(d.pop()) # right
print(d) # deque(['abcd', 'h', 't', 'g', 'i', 'r', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'p', 'o', 'i', 'u', 'y'])



