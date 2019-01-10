import collections

def default_value():
    return "Default value"


m = collections.defaultdict(default_value,foo='aaa')
print(m['fxx']) # 返回 Default value