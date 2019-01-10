# enum 类
一个简单的枚举类
```py
import enum

class BugStatus1(enum.Enum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print('\n'.join(' '+s.name+":"+str(s.value) for s in BugStatus1))
```
但是这样的枚举类不能进行比较和排序，我们可以使用 IntEnum
```py
class BugStatus(enum.IntEnum):
    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1


print('\n'.join(' '+s.name for s in sorted(BugStatus)))
# enum 有两个属性值 name / value
for status in BugStatus:
    print(status.name,':',status.value)
```
上面的代码没什么意义，我也可以使用列表来实现，代码可能还简便得多。枚举类的主要优点，就是它的拓展性强，并不是单单定义一些12345,我们还可以定义其他的属性，枚举类的动作等等。
看一个简单的例子：
```py
# 一个更复杂的例子
class BugStatus3(enum.Enum):
    new = {
        'num': 7,
        'transitions': [
            'incomplete',
            'invalid',
            'wont_fix',
            'in_progress',
        ],
    }
    incomplete = {
        'num': 6,
        'transitions': ['new', 'wont_fix'],
    }
    def __init__(self, vals):
        self.num = vals['num']
        self.transitions = vals['transitions']

    def can_transition(self, new_state):
        return new_state.name in self.transitions

print(BugStatus3.new.value)
print(BugStatus3.new.transitions)
```


# 参考
《The Python3 Standard Library By Example》
