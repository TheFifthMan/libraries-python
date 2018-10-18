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
