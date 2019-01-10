# collections 数据类型
collections 数据类型主要是为了弥补 list /tuple / dict 的额外数据类型

## ChainMap
代码：
```py
import collections
## 赋值，合并字典的作用
a = {'a':"A"}
b = {"b":"B"}

m = collections.ChainMap(a,b)
for k,v in m.items():
    print('key: {} | value:{}'.format(k,v))

print(m)
```
如果字典中有重复的key值

```py
a = {"a":"A","b":"B"}
b = {"b":"C"}
m2 = collections.ChainMap(a,b)
print(m2)

for k,v in m2.items():
    print('key: {} | value:{}'.format(k,v))

```

输出：
```
ChainMap({'a': 'A', 'b': 'B'}, {'b': 'C'})
key: a | value:A
key: b | value:B
```
结论：
结果是没有合并，如果只是合并字典的值，还是直接使用update即可, 这个模块不怎么会用到，了解即可

## Counter
Counter 顾名思义，就是计算总数的意思，可以计算出一个序列中每个元素的个数，一个简单的例子
```sh
>>> import collections
>>> collections.Counter("Hello World")
Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})
```
可以使用如下的写法，来得到自己想要的元素的个数

```py
>>> a =  collections.Counter("Hello World")
>>> a['W']
1
```
除此之外，Counter对象还支持直接运算

```py
import collections

c1 = collections.Counter("Hello World")
c2 = collections.Counter("Hello Python")

print("c1 + c2 =",c1 + c2)
print("c1 - c2 = ",c1 - c2)
print("c1 | c2 = ",c1 | c2)
print("c1 & c2 = ",c1 & c2)
```
输出：
```sh
c1 + c2 = Counter({'l': 5, 'o': 4, 'H': 2, 'e': 2, ' ': 2, 'W': 1, 'r': 1, 'd': 1, 'P': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1})
c1 - c2 =  Counter({'l': 1, 'W': 1, 'r': 1, 'd': 1})
c1 | c2 =  Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1, 'P': 1, 'y': 1, 't': 1, 'h': 1, 'n': 1})
c1 & c2 =  Counter({'l': 2, 'o': 2, 'H': 1, 'e': 1, ' ': 1})
```
## defaultdict
众所周知，当需要获取一个字典的值，可以使用 xx[key] 这样的形式去获取，如果key值不存在，那么就会抛出一个错误，所以大部分推荐的做法是，使用 get 方法来获取字典的值，比如：
```py
test = {"a":"b"}
test.get("a")
# 如果获取一个不存在的 key 值
test.get("b") # 返回None
# 但是通过get 可以指定一个 key 值
test.get("b","this is b") # 返回 this is b
```
defaultdict 也差不多是这样的道理，当你获取一个不存在的 key 值的时候，返回默认值
```py
import collections

def default_value():
    return "Default value"


m = collections.defaultdict(default_value,foo='aaa')
print(m['fxx']) # 返回 Default value
```
## deque
双端队列，元素可以从两端弹出，插入和删除操作限定在队列的两边进行
```py
from collections import deque
d = deque("abcdefg")
print(d) # deque(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
d.remove('c')
print(d) # deque(['a', 'b', 'd', 'e', 'f', 'g'])
d.append('h')
print(d) #deque(['a', 'b', 'd', 'e', 'f', 'g', 'h'])
d.appendleft("1")
print(d) #deque(['1', 'a', 'b', 'd', 'e', 'f', 'g', 'h'])
# 使用pop 获取队列中的值
d.pop()
print(d) # deque(['1', 'a', 'b', 'd', 'e', 'f', 'g'])
d.popleft()
print(d) # deque(['a', 'b', 'd', 'e', 'f', 'g'])
```
也可以使用线程来消费双端队列
```py
from collections import deque
import time
import threading


# deque 也可以用线程通信
d1 = deque(range(1000))
def task(direction,i,nextSource):
    while True:
        try:
            item = nextSource()
            print("方向：{} 线程： {} 正在处理： {} ".format(direction,i,item))
        except IndexError as e:
            break
        else:
            time.sleep(1)
    

right_ts = [threading.Thread(target=task,args=('right',i,d1.pop))for i in range(10)]
left_ts = [threading.Thread(target=task,args=('left',i,d1.popleft)) for i in range(10)]

for tl in left_ts:
    tl.start()

for tr in right_ts:
    tr.start()

for tl in left_ts:
    tl.join()

for tr in right_ts:
    tr.join()

```
## OrderedDict
使用字典的时候，其输出时，不一定按照当时添加的顺序输出，例如：
```
d = {}
d['a']= 'A'
d['b'] = 3
d['c']= 1
d['d']='B'
d['c']='C'
for k,v in d.items():
    print(k,'=>',v)
```
输出：
```
a => A
b => 3
c => C
d => B
```
但是 OrderedDict 会
```
d = OrderedDict()
d['a']= 'A'
d['b'] = 3
d['s']= 1
d['d']='B'
d['c']='C'
for k,v in d.items():
    print(k,'=>',v)

```
输出：
```
a => A
b => 3
s => 1
d => B
c => C
```
当需要使用dict 来作为运算和存储的时候，这就是一个比较有用的特点了。

# 总结
以上这些在日常使用的时候如果不了解，很少会去用到，但如果想写出优雅，简洁的代码，这些概念会起到一定的帮助作用

# 参考
《The Python3 Standard Library By Example》
