from multiprocessing import Pool
import threading
import os,time 
import queue 
from datetime import datetime 

def producer(i):
    Q = queue.Queue()
    if i == 1:
        for x in range(1,5):
            Q.put(x)
    elif i == 2:
        for x in range(5,10):
            Q.put(x)
    elif i ==3:
        for x in range(10,15):
            Q.put(x)
    elif i == 4:
        for x in range(15,20):
            Q.put(x)
    
    return Q

def process_thread(Q,j):
    while not Q.empty():
        item = Q.get()
        print("进程{}: 线程{} 正在消耗:{} 时间：{}".format(os.getpid(),j,item,datetime.now()))
    
    Q.all_tasks_done


def tasks(i):
    Q = producer(i)
    ts = [threading.Thread(target=process_thread,args=(Q,j)) for j in range(10)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()





if __name__ == "__main__":
    p = Pool(4)
    for i in range(5):
        p.apply_async(tasks,args=(i,))
    p.close()
    p.join()

