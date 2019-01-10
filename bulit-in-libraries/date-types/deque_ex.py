from collections import deque
import time

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
    
import threading

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