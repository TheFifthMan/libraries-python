# contextlib
在python 中只要正确实现了上下文管理管理，就可以使用 with 语句。而 contextlib 就是一个帮助实现上下文管理的模块。
所以什么是上下文管理？ 一般来说，只要实现了 __enter__() 和 __exit__() 两个方法，在python 中就算是实现了上下文管理
一个简单的例子
```py
class Context():
    def __init__(self):
        print("__init__")
    
    def __enter__(self):
        print("__enter__")
    
    def __exit__(self,exc_type, exc_val, exc_tb):
        print("__exit__")

with Context():
    print("doing some works")
```
## contextmanager装饰器
接下来研究一下contextmanager。contextmanager是一个装饰器，用于实现上下文管理  
首先，要明确的一点是能够使用 with 语句不一定就是说能够正确的关闭资源，能够使用with 只是说明了实现了上下文管理器。比如：
```py
@contextmanager
def tag():
    print("<h1>")
    yield 
    print("</h1>")


with tag():
    print("Hello world")
```
这里也可以使用 with 但是只是实现了tag 函数的上下文管理，没有关闭任何资源。其输出：
```
<h1>
Hello world
</h1>
```
如果跟关闭资源有关，我们需要在函数的上下文中定义好关闭资源的方法，比如以连接mysql数据库为例：
```py
from contextlib import contextmanager
import pymysql

# 定义连接上下文
@contextmanager
def create_connection():
    connection = pymysql.connect(host='localhost',
                             user='root',
                             password='qwe123',
                             db='apitesting',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    try:
        yield connection
    finally:
        connection.close()

# 使用 with...as 输出上下文管理
with create_connection() as conn:
    with conn.cursor() as cursor:
        sql = "select * from account;"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
    conn.commit()
```
所以关闭资源是关闭资源，跟上下文管理不存在关系。


## closing
如果一个对象没有实现上下文，就不能使用with语句. 这个时候可以使用closing 将其装饰为一个实现了上下文管理的对象，但是注意的是，对象必须要有 close 方法
```py
from contextlib import closing

class TestObj():
    def __init__(self):
        print("init test obj")
    def test(slef):
        print("test")
    def close(self):
        print("close")
    

with closing(TestObj()) as t:
    t.test()
```
