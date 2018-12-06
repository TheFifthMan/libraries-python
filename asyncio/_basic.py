# coding:utf-8
# 简单的例子
import asyncio
from datetime import datetime 
sega = asyncio.Semaphore(3)

async def test_asyncio():
    with(await sega):
        print("start : {}".format(datetime.now()))
        await asyncio.sleep(15)
        print('end : {}'.format(datetime.now()))


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = [asyncio.ensure_future(test_asyncio()) for i in range(10)]
    # 如果使用task，就必须要wait
    loop.run_until_complete(asyncio.wait(task))


