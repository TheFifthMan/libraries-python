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