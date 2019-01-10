from collections import OrderedDict

d = OrderedDict()
d['a']= 'A'
d['b'] = 3
d['s']= 1
d['d']='B'
d['c']='C'
for k,v in d.items():
    print(k,'=>',v)

