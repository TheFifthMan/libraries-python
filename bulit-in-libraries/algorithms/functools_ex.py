import functools

def myfunc(a,b):
    print("This is myfuc params:{},{}".format(a,b))


a = functools.partial(myfunc,b=1)
value= {"a":1000}
a(**value)