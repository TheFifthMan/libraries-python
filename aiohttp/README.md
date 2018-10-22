# aiohttp
aiohttp是一个异步框架，分为两个部分，一个是Client端，一个是server端。

# Client
Client端的操作有点类似于requests框架。

## 例子
使用aiohttp爬壁纸网站:[代码](_example.py)

## request设置
```py
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36"
}
headers=headers
```
## post参数设置
```
data = '{"xxx":3123}'
data=data
```
## 典型的例子
```py
async def fetch_url(i):
    # 保持同一个session
    #async with aiohttp.ClientSession() as session:
        async with aiohttp.request('GET',url.format(str(i)),headers=headers) as res:
            if res.status == 200:
                print("第{}页返回成功".format(i))
                result = await res.text()
            else:
                print("第{}页返回{}".format(i,res.status)) 
                result=None
            return result
```
## 二进制数据
```py
async with aiohttp.request('GET',url,headers=headers) as res:
    if res.status == 200:
        with open(folder+'/'+wallpaper_id+'.jpg','wb') as f:
            print("--------写入id为{}的图片".format(wallpaper_id))
            while 1:
                chunk = await res.content.read(10)
                if not chunk:
                    break
                f.write(chunk)
```