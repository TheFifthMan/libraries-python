# coding:utf-8 
# 多线程的使用一般结合队列来做。

import queue 
from datetime import datetime 
import time,threading

Q = queue.Queue()

def put_items():
    for i in range(1,100000):
        Q.put(i)


def worker(i):
    while not Q.empty():
        print("线程{}开始处理数据,开始时间：{}".format(i,datetime.now()))
        item = Q.get()
        time.sleep(1)
        print('线程{}处理完数据{}，结束时间{}'.format(i,item,datetime.now()))
        Q.tasks_done()

if __name__ == "__main__":
    put_items()
    ts = [threading.Thread(target=worker,args=(i,))for i in range(20)]
    for t in ts:
        t.start()

    for t in ts:
        t.join()

    print("All done")
