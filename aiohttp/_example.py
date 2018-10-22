import aiohttp
import asyncio
from bs4 import BeautifulSoup
import os 
url = 'https://alpha.wallhaven.cc/latest?page={}'
from datetime import datetime 
segm = asyncio.Semaphore(10)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
}

async def fetch_url(i):
    #async with aiohttp.ClientSession() as session:
    async with aiohttp.request('GET',url.format(str(i)),headers=headers) as res:
        if res.status == 200:
            print("第{}页返回成功".format(i))
            result = await res.text()
        else:
            print("第{}页返回{}".format(i,res.status)) 
            result=None
        return result

async def fetch_picture(wallpaper_id):
    folder = 'picture2'
    if not os.path.exists(folder):
        os.mkdir(folder)
    url = 'https://alpha.wallhaven.cc/wallpapers/full/wallhaven-{}.jpg'.format(wallpaper_id)
    async with aiohttp.request('GET',url,headers=headers) as res:
        if res.status == 200:
            with open(folder+'/'+wallpaper_id+'.jpg','wb') as f:
                print("--------写入id为{}的图片".format(wallpaper_id))
                while 1:
                    chunk = await res.content.read(10)
                    if not chunk:
                        break
                    f.write(chunk)
        else:
            print('--------{}返回{}'.format(url,res.status))
            with open('aiohttp/error.txt','a')as f:
                f.writelines('{}:{}\n'.format(url,res.status))


async def parse_picture(i):
    async with segm:
        print("当前页码：{}".format(str(i)))
        res = await fetch_url(i)
        if res != None:
            print('开始解析第{}页的图片....'.format(i))
            soup = BeautifulSoup(res,'html.parser')
            figures = soup.find_all('figure')
            for figure in figures:
                wallpaper_id = figure['data-wallpaper-id']
                await fetch_picture(wallpaper_id)

if __name__ == "__main__":
    start = datetime.now()     
    loop = asyncio.get_event_loop()
    # ensure_future 保证异步协程的调用
    tasks = [asyncio.ensure_future(parse_picture(i)) for i in range(3)]
    loop.run_until_complete(asyncio.wait(tasks))
    end = datetime.now()
    duration = end - start
    print('一共耗时{}'.format(duration))
