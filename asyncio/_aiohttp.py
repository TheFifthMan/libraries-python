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