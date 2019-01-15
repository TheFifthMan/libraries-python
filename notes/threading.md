# 多线程
## 简单示例
对于CPU计算密集型的任务，python的多线程跟单线程没什么区别，甚至有可能会更慢，但是对于IO密集型的任务，比如http请求这类任务，python的多线程还是有用处。在日常的使用中，经常会结合多线程和队列一起使用，比如，以爬取simpledestops 网站壁纸为例：
```
import os 
from datetime import datetime 
from queue import Queue
from threading import Thread
import requests
requests.packages.urllib3.disable_warnings()

from bs4 import BeautifulSoup
import re

if not os.path.exists('img'):
    os.mkdir('img')

# 声明一个队列
Q = Queue()

def producer(pages):
    for page in range(1,pages+1):
        # 提取每一页的图片 url 加入队列
        print("[-] 收集第 {} 页".format(str(page)))
        url = "http://simpledesktops.com/browse/"+str(page)+"/"
        r = requests.get(url,verify=False)
        html = r.text
        soup = BeautifulSoup(html,'html.parser')
        try:
            imgs = soup.find_all('img')
            for img in imgs:
                img_url = img['src']
                Q.put(img_url)
        except:
            pass

def worker(i):
   # 取出队列的值，按顺序取，下载图片
    while not Q.empty():
        img_url = Q.get()
        text = re.search('(http://static.simpledesktops.com/uploads/desktops/\d+/\d+/\d+/(.*?png)).*?png',img_url)
        new_img_url = text.group(1)

        r = requests.get(new_img_url,verify=False)
        path = "img/"+text.group(2)
        print("[-] 线程 {} 开始下载 {} 开始时间：{}".format(i,text.group(2),datetime.now()))

        with open(path,'wb') as f:
            f.write(r.content)
    
    Q.all_tasks_done


if __name__ =="__main__":
    # 一定要将数据加入队列，否则是启动不了的，因为队列为空 
    producer(50)
    # 线程的声明
    ts = [Thread(target=worker,args=(i,)) for i in range(50)]
    for t in ts:
        t.start()

    for t in ts:
        t.join()
```

我们使用start启动多线程，使用 join 防止主线程退出的时候结束所有的线程，使用队列有序的且并发的下载壁纸。 仔细观察就会发现代码其实有迹可循，更改其中的爬取内容的部分代码后，我们就可以应用于爬取别的网站。
## ThreadLocal
按照道理来说，多线程中，每个线程的处理逻辑应该是相同的，但是其处理的数据，却不一定是相同的，如果数据是全局的，那么我们就需要加锁，防止数据混乱，这样一来就会麻烦很多，所以线程处理的数据最好是局部的、其他线程不能干扰的。

代码示例：
```
# coding: utf-8 

import threading,time
import requests
requests.packages.urllib3.disable_warnings()
from datetime import datetime 

local_variable = threading.local()

# 逻辑处理函数
def worker():
    print("每个线程启动的时间： ",datetime.now())
    time.sleep(10)
    url = local_variable.url
    r = requests.get(url,verify=False)
    print(r.url,datetime.strftime(datetime.now(),'%H:%M:%S'),threading.current_thread().name)

# 线程处理函数
def process_thread(url):
    local_variable.url = url
    worker()


if __name__ == "__main__":
    ts = [threading.Thread(target=process_thread,args=(url,))for url in ['https://www.baidu.com','https://www.google.com','https://www.bing.com']]
    for t in ts:
        t.start()

    for t in ts:

        t.join()
```
输出：
```
线程Thread-1 启动的时间：2019-01-09 11:25:18.339631
线程Thread-2 启动的时间：2019-01-09 11:25:18.340646
线程Thread-3 启动的时间：2019-01-09 11:25:18.342635
https://www.baidu.com/ 11:25:28 Thread-1
https://cn.bing.com/ 11:25:29 Thread-3
https://www.google.com/ 11:25:29 Thread-2
```
# 多进程
## 进程池
python中使用 multiprocessing 来创建多进程，如果要创建多个子进程，则需要使用 进程池 Pool 来创建，一个简单的例子：
```
from multiprocessing import Pool
import os 
from datetime import datetime 


'''
@param {type} int
@return: None
'''
def print_num(i):
    print("进程{} 打印 {}".format(os.getpid(),i))


if __name__ == "__main__":
    p = Pool(4)
    for i in range(100):
        p.apply_async(print_num,args=(i,))
    # 关闭进程池，不再加入进程
    p.close()
    # 防止主进程结束，子进程无法继续运行
    p.join()
    
```
输出：
```
进程2624 打印 0
进程2625 打印 1
进程2626 打印 3
进程2627 打印 2
进程2624 打印 4
进程2625 打印 5
进程2626 打印 6
进程2627 打印 7
进程2624 打印 8
...
```
进程可以实现并行运行代码，但是一旦进程太多，CPU运行不过来也是需要进行等待，用了多进程以后，就可以不使用队列了，也可以实现多线程的效果

除此之外，还可以多进程和多线程结合起来使用，一个简单的例子
```
from multiprocessing import Pool
import threading
import os,time 
import queue 
from datetime import datetime 

def producer(i):
    Q = queue.Queue()
    start = 25*(i-1)
    end = 100 * int(i / 4)

    for x in range(start,end):
        Q.put(x)
  
    
    return Q

def process_thread(Q,j):
    while not Q.empty():
        item = Q.get()
        print("进程{}: 线程{} 正在消耗:{} 时间：{}".format(os.getpid(),j,item,datetime.now()))

    Q.all_tasks_done


def tasks(i):
    Q = producer(i)
    ts = [threading.Thread(target=process_thread,args=(Q,j)) for j in range(10)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()


if __name__ == "__main__":
    start = datetime.now()
    p = Pool(4)
    for i in range(1,5):
        print(i)
        p.apply_async(tasks,args=(i,))
    p.close()
    p.join()
    end = datetime.now()
    waste = end-start
    print("一共花费了： {}".format(waste))
    
```
先将要处理的数据，填进队列，然后创建4个进程，10个线程运行。 其输出为：
```
'''
(venv) C:\project\libraries-python>python bulit-in-libraries\threading\multithreading.py
进程17020: 线程0 正在消耗:1 时间：2019-01-09 12:50:48.701523
进程17020: 线程1 正在消耗:2 时间：2019-01-09 12:50:48.703521
进程17020: 线程3 正在消耗:4 时间：2019-01-09 12:50:48.704365
进程17020: 线程2 正在消耗:3 时间：2019-01-09 12:50:48.704365

进程2804: 线程0 正在消耗:5 时间：2019-01-09 12:50:48.706349
进程2804: 线程1 正在消耗:6 时间：2019-01-09 12:50:48.707352
进程2804: 线程4 正在消耗:9 时间：2019-01-09 12:50:48.708355
进程2804: 线程3 正在消耗:8 时间：2019-01-09 12:50:48.708355
进程2804: 线程2 正在消耗:7 时间：2019-01-09 12:50:48.708355

进程16060: 线程0 正在消耗:10 时间：2019-01-09 12:50:48.728409
进程16060: 线程1 正在消耗:11 时间：2019-01-09 12:50:48.730413
进程16060: 线程4 正在消耗:14 时间：2019-01-09 12:50:48.732418
进程16060: 线程3 正在消耗:13 时间：2019-01-09 12:50:48.732418
进程16060: 线程2 正在消耗:12 时间：2019-01-09 12:50:48.732418

进程7588: 线程3 正在消耗:18 时间：2019-01-09 12:50:48.761808
进程7588: 线程4 正在消耗:19 时间：2019-01-09 12:50:48.761808
进程7588: 线程0 正在消耗:15 时间：2019-01-09 12:50:48.761808
进程7588: 线程1 正在消耗:16 时间：2019-01-09 12:50:48.761808
进程7588: 线程2 正在消耗:17 时间：2019-01-09 12:50:48.761808
```
后来实验了打印出10万个数，4个进程，每个进程400个线程，花费了39秒。而400个线程，只花费了17秒。所以有时候，也并不是多就是好。进程线程切换都需要使用一定的时间。
## 子进程
在python中，如果要运行系统命令，会使用 subprocess 来运行，这个模块会打开一个子进程，并返回一个CompletedProcess 的实例，官方建议使用run 方法来运行系统命令，更高级的用法是直接使用其 Popen 接口。
其函数格式为：
```py
subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)
```
可以看几个简单的例子：
### 直接使用
```py
import subprocess
subprocess.run(['ls','-al'])
```
在python3.7 之前，默认系统命令执行的结果(输出/错误)不存在stdout/stderr 里面，需要设置 capture_output=True，而在python3.6 版本，如果你需要使用执行的结果，你就需要设置 stdout. 如下所示
```py
# python 3.6
>>> a = subprocess.run(['ls','-al'],stdout=subprocess.PIPE)
>>> a.stdout

# python3.7 
>>> a = subprocess.run(['ls','-al'],capture_output=True)
>>> a.stdout
```
所以可以看出python3.7 又做了一层封装，为了让大家使用更上一层的接口。可以看一下几个参数的含义为：
```py
args 列表，为shell命令
shell boolean值， 设置后，args可以直接接受shell命令
capture_output = True , 设置后，stdout/stderr会存储值
check=True， 设置后，如果程序异常退出，会跑出一个CalledProcessError异常
cwd 是工作目录，可以为str，或者path-like 类
```
### 错误处理
程序运行完会返回一个数值，来确认程序是否运行正确。这个处理需要使用 check 参数来实现。 
```py
import subprocess
try:
    subprocess.run(['false'], check=True)
except subprocess.CalledProcessError as err:
    print('ERROR:', err)
```
这里因为 false 命令不存在，会返回一个非 0 的数值，来表示程序运行异常


### 高级使用
Popen的构造函数：
```py
class subprocess.Popen(args, bufsize=-1, executable=None, stdin=None, stdout=None, stderr=None, preexec_fn=None, close_fds=True, shell=False, cwd=None, env=None, universal_newlines=False, startupinfo=None, creationflags=0, restore_signals=True, start_new_session=False, pass_fds=(), *, encoding=None, errors=None)
```
一个简单的例子
```py
p = subprocess.Popen(['ls','-al'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
```
其次，通过Popen.communicate() ，子进程可以在启动了以后，还可以进行参数的输入
```py
import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
print(output.decode('utf-8'))
print('Exit code:', p.returncode)
其输出：
$ nslookup
Server:        192.168.19.4
Address:    192.168.19.4#53

Non-authoritative answer:
python.org    mail exchanger = 50 mail.python.org.

Authoritative answers can be found from:
mail.python.org    internet address = 82.94.164.166
mail.python.org    has AAAA address 2001:888:2000:d::a6

Exit code: 0
```
## 分布式多进程
python的分布式接口简单，使用起来也十分简单，可以参考[廖雪峰的教程][1]，需要的时候，修改代码，即可完成属于自己的分布式程序

这里贴出代码：
```py
# master
import random,time,queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)

manager = QueueManager(address=('',5000),authkey=b'abc')
manager.start()

tasks = manager.get_task_queue()
results = manager.get_result_queue()

for i in range(10):
    n = random.randint(0,10000)
    print('put task {}'.format(n))
    tasks.put(n)

print('try get results...')
for i in range(10):
    r = results.get(timeout=100)
    print('result:{}'.format(r))

manager.shutdown()
print('master exit')

# worker
import time,sys,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

# master的主机地址
server_addr = '127.0.0.1'
print('connect to server...')
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
m.connect()

tasks = m.get_task_queue()
results = m.get_result_queue()

for i in range(10):
    try:
        n = tasks.get(timeout=1)
        print('run task %d * %d...' % (n, n))

        r = '{} * {} = {}'.format(n,n,n*n)
        time.sleep(1)
        results.put(r)
    except Queue.Empty:
        print('task queue is empty.')

print('worker exit.')

```
# 参考
[https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431929340191970154d52b9d484b88a7b343708fcc60000](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431929340191970154d52b9d484b88a7b343708fcc60000)
[https://docs.python.org/3.6/library/subprocess.html](https://docs.python.org/3.6/library/subprocess.html)
[https://docs.python.org/3.7/library/subprocess.html](https://docs.python.org/3.7/library/subprocess.html)


  [1]: https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431929340191970154d52b9d484b88a7b343708fcc60000