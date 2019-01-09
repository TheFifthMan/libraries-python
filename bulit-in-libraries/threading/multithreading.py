'''
(venv) C:\project\libraries-python>python bulit-in-libraries\threading\multithreading.py
进程17020: 线程0 正在消耗:1 时间：2019-01-09 12:50:48.701523
进程17020: 线程1 正在消耗:2 时间：2019-01-09 12:50:48.703521
进程17020: 线程3 正在消耗:4 时间：2019-01-09 12:50:48.704365
进程17020: 线程2 正在消耗:3 时间：2019-01-09 12:50:48.704365
进程2804: 线程0 正在消耗:5 时间：2019-01-09 12:50:48.706349
进程2804: 线程1 正在消耗:6 时间：2019-01-09 12:50:48.707352
进程2804: 线程4 正在消耗:9 时间：2019-01-09 12:50:48.708355
进程2804: 线程3 正在消耗:8 时间：2019-01-09 12:50:48.708355
进程2804: 线程2 正在消耗:7 时间：2019-01-09 12:50:48.708355
进程16060: 线程0 正在消耗:10 时间：2019-01-09 12:50:48.728409
进程16060: 线程1 正在消耗:11 时间：2019-01-09 12:50:48.730413
进程16060: 线程4 正在消耗:14 时间：2019-01-09 12:50:48.732418
进程16060: 线程3 正在消耗:13 时间：2019-01-09 12:50:48.732418
进程16060: 线程2 正在消耗:12 时间：2019-01-09 12:50:48.732418
进程7588: 线程3 正在消耗:18 时间：2019-01-09 12:50:48.761808
进程7588: 线程4 正在消耗:19 时间：2019-01-09 12:50:48.761808
进程7588: 线程0 正在消耗:15 时间：2019-01-09 12:50:48.761808
进程7588: 线程1 正在消耗:16 时间：2019-01-09 12:50:48.761808
进程7588: 线程2 正在消耗:17 时间：2019-01-09 12:50:48.761808


100000 花费 47秒
'''

from multiprocessing import Pool
import threading
import os,time 
import queue 
from datetime import datetime 

def producer(i):
    Q = queue.Queue()
    start = 2500*(i-1)
    end = 100000 * int(i / 4)

    for x in range(start,end):
        Q.put(x)
  
    
    return Q

def process_thread(Q,j):
    while not Q.empty():
        item = Q.get()
        print("进程{}: 线程{} 正在消耗:{} 时间：{}".format(os.getpid(),j,item,datetime.now()))

    Q.all_tasks_done


def tasks(i):
    Q = producer(i)
    ts = [threading.Thread(target=process_thread,args=(Q,j)) for j in range(400)]
    for t in ts:
        t.start()
    for t in ts:
        t.join()


if __name__ == "__main__":
    start = datetime.now()
    p = Pool(4)
    for i in range(1,5):
        print(i)
        p.apply_async(tasks,args=(i,))
    p.close()
    p.join()
    end = datetime.now()
    waste = end-start
    print("一共花费了： {}".format(waste))


