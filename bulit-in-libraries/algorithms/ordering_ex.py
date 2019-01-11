import functools
#@functools.total_ordering
class MyObject():
    def __init__(self,priority):
        self.priority = priority

    
    def __eq__(self,other):
        print("执行等于操作")
        return  self.priority == other.priority
    
    def __lt__(self,other):
        print("执行小于操作")
        
        return self.priority < other.priority
    

if __name__ =="__main__":
    a = MyObject(1)
    b = MyObject(2)
    print(a == b)
      