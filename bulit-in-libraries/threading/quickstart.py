# coding:utf-8 
# 多线程的使用一般结合队列来做。
# All done: 0:00:17.692017

import queue 
from datetime import datetime 
import time,threading

Q = queue.Queue()

def put_items():
    for i in range(1,100000):
        Q.put(i)


def worker(i):
    while not Q.empty():
        item = Q.get()
        print('线程{}处理完数据{}，结束时间{}'.format(i,item,datetime.now()))
    Q.all_tasks_done

if __name__ == "__main__":
    start = datetime.now()
    put_items()
    ts = [threading.Thread(target=worker,args=(i,))for i in range(400)]
    for t in ts:
        t.start()

    for t in ts:
        t.join()
    end = datetime.now()

    print("All done: {}".format(end - start))
