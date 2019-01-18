# coding: utf-8 
import random 
'''
# 生成0 - 1 之间的随机小数
for i in range(100):
    print("0 ~ 1: ",random.random())

# 生成其他的随机小数
for i in range(1,100):
    print("1 ~ 100  :",random.uniform(1,100))

# 随机数生成的算法 ： min + (max -min) * random()
# 如果你要生成整数

for i in range(100):
    print("1 ~ 100: ",random.randint(1,100))
'''
# 种子
# 每次运行脚本生成的随机数都是一样的
random.seed(10)
for i in range(10):
    print("seed: ",random.random())

'''
# 第一次运行
seed:  0.5714025946899135
seed:  0.4288890546751146
seed:  0.5780913011344704
seed:  0.20609823213950174
seed:  0.81332125135732
seed:  0.8235888725334455
seed:  0.6534725339011758
seed:  0.16022955651881965
seed:  0.5206693596399246
seed:  0.32777281162209315

# 第二次运行
seed:  0.5714025946899135
seed:  0.4288890546751146
seed:  0.5780913011344704
seed:  0.20609823213950174
seed:  0.81332125135732
seed:  0.8235888725334455
seed:  0.6534725339011758
seed:  0.16022955651881965
seed:  0.5206693596399246
seed:  0.32777281162209315
'''

# randrange
for i in range(10):
    print(random.randrange(0,100,5))

'''
35
55
5
65
20
95
55
60
65
45
'''

# 随机选择

a = ["How are you?", "How old are you?", "How do you do?"]
for i in range(100):
    print(random.choice(a))

# 打乱顺序
a = [1,2,3,4,5,6,7,8,9]
random.shuffle(a)
print(a) # [2, 3, 1, 6, 7, 9, 8, 5, 4]

# 生成样本
sample = [
    "streamlet",
    "impestation",
    "violaquercitrin",
    "mycetoid",
    "plethoretical",
]

for w in random.sample(sample,5):
    print(w)