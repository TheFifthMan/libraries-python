# array
array 定义了一个非常类似list的模块，其array 函数接受两个参数，第一个参数是预先定义好的类型，第二个参数，一般为一个序列。 很少见到
代码：
```
import array

a = array.array('b',b'abcd')
print(a)
print(a[0])
```
输出：
```
array('b', [97, 98, 99, 100])
97
```
# heapq
heapq 是python中实现堆排序的模块。
```py
from heapq import *
import random
# 创建一个堆排序
data = []
for i in range(10):
    heappush(data,random.randint(1,20))

print(data)

# 使用 heappop 移除最小的元素
small_num = heappop(data)
print(small_num)
print('pop移除最小元素后: ',data)
# 使用heapreplace替换最小元素，会先执行pop，然后replace
n = heapreplace(data,100)
print(n)
print('执行replace后:',data)

# n个最大 / n个最小
lagest = nlargest(3,data)
small = nsmallest(3,data)

print("3个最大的值：",lagest)
print("3个最小的值：",small)

```
输出
```
[2, 3, 8, 7, 4, 18, 12, 17, 16, 13]
2
pop移除最小元素后:  [3, 4, 8, 7, 13, 18, 12, 17, 16]
3
执行replace后: [4, 7, 8, 16, 13, 18, 12, 17, 100]
3个最大的值： [100, 18, 17]
3个最小的值： [4, 7, 8]
```
# queue
队列，在线程一节有总结过，有先进先出队列，也有优先级队列，队列结合线程，可以保证线程之间通信的安全。这里主要看一下优先级队列

```py
from queue import PriorityQueue
import threading
import functools
Q = PriorityQueue()

@functools.total_ordering
class Job:
    def __init__(self,priority,desc):
        self.priority = priority
        self.desc = desc
        return 
    # 定义优先级比较
    def __eq__(self,other):
        try:
            self.priority == other.priority
        except AttributeError as e:
            return NotImplemented
    
    def __lt__(self,other):
        try:
            self.priority < other.priority
        except AssertionError:
            return NotImplemented




def worker():
    while not Q.empty():
        item = Q.get()
        import time 
        time.sleep(1)
        print(item.desc)
    
    Q.all_tasks_done


if __name__ == "__main__":
    Q.put(Job(3,"mid job"))
    Q.put(Job(10,"important job"))
    Q.put(Job(1,"low job"))
    ts = [threading.Thread(target=worker),threading.Thread(target=worker)]
    for t in ts:
        t.start()
    
    t.join()
```
输出
```
important job
mid job
low job 
```

