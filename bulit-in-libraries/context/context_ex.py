# coding: utf-8 
# 引入contextlib.contextmanager以后
from contextlib import contextmanager

class Query():
    def __init__(self):
        print("__init__")
    
    def query(self):
        print("quering")

@contextmanager
def create_query():
    print("start")
    q = Query()
    yield q
    print('end')

with create_query() as q:
    q.query()
    print(dir(q))

print(dir(create_query))


'''
start
__init__
quering
end
'''


# 第一种，使用装饰函数关闭资源
# @contextmanager
# def make_context():
#     i = 0
#     try:
#         yield i
#     except RuntimeError as err:
#         print("Error happen!")
#     finally:
#         print("Close and clean resource")

# @make_context()   
# def normal():
#     print("Normal testing")

# normal()

# with make_context():
#     print("somethins")

@contextmanager
def tag():
    print("<h1>")
    yield 
    print("</h1>")


with tag():
    print("Hello world")