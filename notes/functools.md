# functools
functools 包含了用于创建装饰函数，启动面向切面的编程，超出面向对象编程范围的代码复用，同时提供了装饰函数用于丰富的快捷比较的API, partial 模块还创建了包含函数参数的函数引用,也就是偏函数

## partial 偏函数
partial 的作用在于如果存在一个函数的参数过多，可以通过partial 固定某一些参数，需要的时候使用关键字参数传入即可.通过一个简单的例子理解
```py
import functools

def myfunc(a,b):
    print("This is myfuc params:{},{}".format(a,b))


a = functools.partial(myfunc,b=1)
a(10000)
```
可以看到，本来调用myfunc的话，要传入两个参数，现在通过固定住某些参数，可以直接调用一个参数即可。除此之外，还可以通过另外一种方式来进行传值
```py
import functools

def myfunc(a,b):
    print("This is myfuc params:{},{}".format(a,b))

a = functools.partial(myfunc,b=1)
value= {"a":1000}
a(**value)
```
## Comparison
functools还提供了丰富用于比较的API，在python2 中，在一个类中可以定义 __cmp__() 方法，用于对象中的比较操作，python3 废除了这样的做法，因为提供了更加详细的API方法，比如 __lt__() , __le__(), __eq__(),__ne__(),__gt__(),__ge__() 这些方法的含义如下：
> 1. lt：less than 小于
> 2. le：less than or equal to 小于等于
> 3. eq：equal to 等于
> 4. ne：not equal to 不等于
> 5. ge：greater than or equal to 大于等于
> 6. gt：greater than 大于

functools 提供了一个装饰器，让我们不需要写这么多定义，只要写一个，其他定义也会加上去。 看一个简单的例子
```py
import functools
@functools.total_ordering
class MyObject():
    def __init__(self,priority):
        self.priority = priority
    def __eq__(self,other):
        print('dengyu')
        return  self.priority == other.priority
    def __lt__(self,other):
        return self.priority < other.priority

if __name__ =="__main__":
    a = MyObject(1)
    print(dir(a))
```
在实际实验中，加不加并没有区别。仅作了解

## lru_cache
这是个有趣的装饰器，传入的参数被打上了hash，当下一次传入的参数是一样的时候，就会从cache中直接取出对应的值，而不需要进行重新的运算。一个简单的例子
```py
import functools

@functools.lru_cache()
def test_method(a,b):
    print("execute {} * {} = {}".format(a,b,a*b))
    return a*b

s = 0
for i in range(2):
    for j in range(2):
        s+=test_method(i,j)

print(test_method.cache_info())


for i in range(2):
    for j in range(3):
        s+=test_method(i,j)

print(test_method.cache_info())
print(s) # 4 说明该执行的还是有执行，只不过是从cache中直接取出而已
```
## 通用函数
对于python来说，很难去固定一个参数必须是什么类型的，只能在具体的代码里面进行检查，functools提供了一个装饰器，可以去做这样的类型检查.一个简单的例子
```py
import functools

@functools.singledispatch
def myfunc(args):
    print(args)

@myfunc.register(list)
def myfunc_list(args):
    for i in args:
        print("List item: {}".format(i))


if __name__ == "__main__":
    # 传入两个不同的类型参数，其处理逻辑也是不同
    myfunc([1,2,3,6,4,5])
    # 但是其调用的接口是一样的。 这样做的好处是可以帮助我们分离代码逻辑
    myfunc("Hello World")
```
输出：
```
List item: 1
List item: 2
List item: 3
List item: 6
List item: 4
List item: 5
Hello World
```
我们也可以把这种做法应用于自己写的类上面，具体就不在赘述。