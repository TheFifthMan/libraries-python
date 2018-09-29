# coding:utf-8
# author： hehehe

# python协程的使用
# 协程没有什么队列的概念
# 协程就是要处理好函数间的切换，当一个函数可以挂起的时候就挂起，直接进入下一个函数入口
# 所以如果要并发处理一堆任务，可以再分配任务循环的时候进行协程函数处理


import asyncio
from datetime import datetime

# 基础协程函数
async def test1():
    print("协程开始启动: {}".format(datetime.now()))
    await asyncio.sleep(5)
    print("协程结束时间: {}".format(datetime.now()))

'''
一共只耗时5秒左右，说明大致上是在同时进行。

协程开始启动: 2018-09-28 21:59:43.438225
协程开始启动: 2018-09-28 21:59:43.438344
协程开始启动: 2018-09-28 21:59:43.438378
协程结束时间: 2018-09-28 21:59:48.440394
协程结束时间: 2018-09-28 21:59:48.440481
协程结束时间: 2018-09-28 21:59:48.440523
'''

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    #ts = [ test1() for _ in range(3) ]
    # 如果是一个list，这里就需要使用到wait，否则不必。
    #loop.run_until_complete(asyncio.wait(ts))
