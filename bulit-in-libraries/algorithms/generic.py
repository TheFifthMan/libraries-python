import functools

@functools.singledispatch
def myfunc(args):
    print("{}".format(args))

@myfunc.register(list)
def myfunc_list(args):
    for i in args:
        print("List item: {}".format(i))


if __name__ == "__main__":
    myfunc([1,2,3,6,4,5])
    myfunc("Hello World")