# 协程
在多线程中，我们结合队列来实现并发。而协程的概念，是我们通过控制函数来实现异步并发的效果，因此并不需要使用队列。而是要控制好每个函数口的发生点，而且一旦开始使用了协程，所有的程序就都需要使用协程。

# 简单的例子
```py
import asyncio
from datetime import datetime 

async def test_asyncio():
    print("start : {}".format(datetime.now()))
    await asyncio.sleep(5)
    print('end : {}'.format(datetime.now()))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = [asyncio.ensure_future(test_asyncio()) for i in range(10)]
    # 如果是task，则需要使用 asyncio.wait 进行等待
    loop.run_until_complete(asyncio.wait(task))
```

# 回调函数
回调函数可以再task执行完毕的时候自动取回结果，接受一个future对象
## 单个协程的回调函数
```py
# coding:utf-8 
import asyncio

async def test1():
    print("This is test1")
    await test2()
    print("test1 end")
    return "result done"

async def test2():
    await asyncio.sleep(4)
    print("This is test2")


def callback(future):
    print("callback: ",future.result())


loop = asyncio.get_event_loop()
task = asyncio.ensure_future(test1())
task.add_done_callback(callback)
loop.run_until_complete(task)

# 执行结果： 
# This is test1
# This is test2 在这里等待了，因为只有一个task，所以这里机器是空闲的状态
# test1 end
# callback:  result done
```
future 有四个状态： Pending/Runing/Done/Cancelled

## 如何取消协程？

```py
# coding:utf-8

import asyncio

async def test1():
    print('This is test1')
    await asyncio.sleep(10)
    print('test1 done')

loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(test1()) for i in range(100)]
# 如此便不会抛出异常
try:
    loop.run_until_complete(asyncio.wait(tasks))
except KeyboardInterrupt as e:
    for task in asyncio.Task.all_tasks():
        task.cancel()
    loop.stop()
    loop.run_forever()
finally:
    loop.close()
```
## 多个协程回调函数
```py

import asyncio

'''
I am test1 and the param is 2
the waitting x is 20
'''
async def test1(x):
    print("I am test1 and the param is {}".format(x))
    await asyncio.sleep(10)
    return x*10

# param 是一个future对象。想象一下，这个类来自未来。
def callback(param):
    print('the waitting x is {}'.format(param.result()))

#a = test1(2)
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(test1(x)) for x in range(10)]
#task.add_done_callback(callback)
loop.run_until_complete(asyncio.wait(tasks))
# 回调函数的值
for task in tasks:
    print(task.result())
```

# 如何使用阻塞和异步
很典型的例子就是requests，当我们发送请求的时候，会进入全局阻塞的状态，无法形成异步的效果。这个时候，只能通过另外开一个线程来进行requests请求。
```
import requests
import asyncio
import functools
urls = ["https://www.baidu.com","https://www.zhihu.com","https://www.163.com"]

async def run(url):
    loop = asyncio.get_event_loop()
    res = await loop.run_in_executor(None,functools.partial(requests.get,url,verify=False))
    print(res.url)

tasks = [ asyncio.ensure_future(run(url)) for url in urls]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
```
但是这样的性能其实有损坏，跟直接使用多线程其实没啥差别。因此一旦异步，接下去的所有代码最好都使用异步。才能真正的体现其性能。

# aiohttp
```py
# coding:utf-8 
import asyncio
import aiohttp
from datetime import datetime 

async def fetch(session,url):
    async with session.get(url) as response:
        print('start fetch {}'.format(datetime.now()))
        await asyncio.sleep(4)
        return response.url

async def run(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session,url)
        print(html,datetime.now())


urls  = ['https://www.baidu.com','https://www.163.com',"https://www.zhihu.com"]
loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(run(url)) for url in urls ]
loop.run_until_complete(asyncio.wait(tasks))
```
# 异步使用队列
> 这里使用 http://httpbin.org/get?a=1 进行举例：[代码](_queue.py)
通过实验这里没办法直接通过队列直接进行并发，但是可以通过传参进行并发:[代码](_thread.py)


# Reference
1. [Python3.5协程学习研究](https://thief.one/2018/06/21/1/)
2. [asyncio1](https://link.zhihu.com/?target=http%3A//www.dongwm.com/archives/%25E4%25BD%25BF%25E7%2594%25A8Python%25E8%25BF%259B%25E8%25A1%258C%25E5%25B9%25B6%25E5%258F%2591%25E7%25BC%2596%25E7%25A8%258B-asyncio%25E7%25AF%2587/)
3. [asyncio2](https://link.zhihu.com/?target=http%3A//www.dongwm.com/archives/%25E4%25BD%25BF%25E7%2594%25A8Python%25E8%25BF%259B%25E8%25A1%258C%25E5%25B9%25B6%25E5%258F%2591%25E7%25BC%2596%25E7%25A8%258B-asyncio%25E7%25AF%2587-%25E4%25BA%258C/)
4. [asyncio3](https://link.zhihu.com/?target=http%3A//www.dongwm.com/archives/%25E4%25BD%25BF%25E7%2594%25A8Python%25E8%25BF%259B%25E8%25A1%258C%25E5%25B9%25B6%25E5%258F%2591%25E7%25BC%2596%25E7%25A8%258B-asyncio%25E7%25AF%2587-%25E4%25B8%2589/)