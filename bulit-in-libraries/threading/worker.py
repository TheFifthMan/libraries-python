import time,sys,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass


QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

server_addr = '127.0.0.1'
print('connect to server...')
m = QueueManager(address=(server_addr,5000),authkey=b'abc')
m.connect()

tasks = m.get_task_queue()
results = m.get_result_queue()

for i in range(10):
    try:
        n = tasks.get(timeout=1)
        print('run task %d * %d...' % (n, n))

        r = '{} * {} = {}'.format(n,n,n*n)
        time.sleep(1)
        results.put(r)
    except Queue.Empty:
        print('task queue is empty.')

print('worker exit.')