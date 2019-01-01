import aiodns
import asyncio
from datetime import datetime 


sema = asyncio.Semaphore(1)
async def fetch_dns():
    resolver = aiodns.DNSResolver()
    return resolver


async def query_dns(name):
    with(await sema):
        print("query {} {}".format(name,datetime.now()))
        resolver = aiodns.DNSResolver(nameservers=['114.114.114.114','8.8.8.8'])
        try:
            results = await resolver.query(name,'A')
            for result in results:
                print(result.host)
        except:
            pass
        

loop = asyncio.get_event_loop()
res = asyncio.wait([query_dns(i) for i in ['google','baidu.com','test.com','qq.com','sina.com','t00ls.net','test.t00ls.net','ctolib.com']])
loop.run_until_complete(res)
