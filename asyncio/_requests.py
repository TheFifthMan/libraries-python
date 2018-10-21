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
