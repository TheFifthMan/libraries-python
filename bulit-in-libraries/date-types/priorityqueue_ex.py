from queue import PriorityQueue
import threading
import functools
Q = PriorityQueue()

@functools.total_ordering
class Job:
    def __init__(self,priority,desc):
        self.priority = priority
        self.desc = desc
        return 
    
    def __eq__(self,other):
        try:
            self.priority == other.priority
        except AttributeError as e:
            return NotImplemented
    
    def __lt__(self,other):
        try:
            self.priority < other.priority
        except AssertionError:
            return NotImplemented




def worker():
    while not Q.empty():
        item = Q.get()
        import time 
        time.sleep(1)
        print(item.desc)
    
    Q.all_tasks_done


if __name__ == "__main__":
    Q.put(Job(3,"mid job"))
    Q.put(Job(10,"important job"))
    Q.put(Job(1,"low job"))
    ts = [threading.Thread(target=worker),threading.Thread(target=worker)]
    for t in ts:
        t.start()
    
    t.join()

    
   
       
    
