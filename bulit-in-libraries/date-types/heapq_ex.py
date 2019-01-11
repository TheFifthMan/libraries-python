from heapq import *
import random
# 创建一个堆排序
data = []
for i in range(10):
    heappush(data,random.randint(1,20))

print(data)

# 使用 heappop 移除最小的元素
small_num = heappop(data)
print(small_num)
print('pop移除最小元素后: ',data)
# 使用heapreplace替换最小元素，会先执行pop，然后replace
n = heapreplace(data,100)
print(n)
print('执行replace后:',data)

# n个最大 / n个最小
lagest = nlargest(3,data)
small = nsmallest(3,data)

print("3个最大的值：",lagest)
print("3个最小的值：",small)
