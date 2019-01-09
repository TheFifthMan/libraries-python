# coding: utf-8 

import threading,time
import requests
requests.packages.urllib3.disable_warnings()
from datetime import datetime 

local_variable = threading.local()

# 逻辑处理函数
def worker():
    print("线程{} 启动的时间：{} ".format(threading.current_thread().name,datetime.now()))
    # 可以看到，当前的sleep并不能阻塞其他程序的运行
    time.sleep(10)
    url = local_variable.url
    r = requests.get(url,verify=False)
    print(r.url,datetime.strftime(datetime.now(),'%H:%M:%S'),threading.current_thread().name)

# 线程处理函数
def process_thread(url):
    local_variable.url = url
    worker()


if __name__ == "__main__":
    ts = [threading.Thread(target=process_thread,args=(url,))for url in ['https://www.baidu.com','https://www.google.com','https://www.bing.com']]
    for t in ts:
        t.start()

    for t in ts:
        t.join()