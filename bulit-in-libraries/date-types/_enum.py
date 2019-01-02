# coding: utf-8 
import enum
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

# 一个更复杂的例子
class BugStatus(enum.Enum):
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

