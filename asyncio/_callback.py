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