# coding:utf-8

import asyncio

async def test1():
    print('This is test1')
    await asyncio.sleep(10)
    print('test1 done')



loop = asyncio.get_event_loop()
tasks = [asyncio.ensure_future(test1()) for i in range(100)]
# loop.run_until_complete(asyncio.wait(tasks))
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

