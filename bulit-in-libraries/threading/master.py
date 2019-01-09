import random,time,queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()

class QueueManager(BaseManager):
    pass

QueueManager.register('get_task_queue',callable=lambda:task_queue)
QueueManager.register('get_result_queue',callable=lambda:result_queue)

manager = QueueManager(address=('',5000),authkey=b'abc')
manager.start()

tasks = manager.get_task_queue()
results = manager.get_result_queue()

for i in range(10):
    n = random.randint(0,10000)
    print('put task {}'.format(n))
    tasks.put(n)

print('try get results...')
for i in range(10):
    r = results.get(timeout=100)
    print('result:{}'.format(r))

manager.shutdown()
print('master exit')