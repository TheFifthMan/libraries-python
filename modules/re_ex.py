import re
r = re.search(r"windows(?:2000|95|98)","windows2000")
print(r.group(0))
# print(r.group(1)) no such group

# 反向肯定预查
r1 = re.search(r"(?<=2000)windows","2000windows")
print(r1.group(0)) # 匹配到了windows

# 反向否定预查
r2 = re.search(r"WINDOWS(?!=2000|98)","windows31",re.I|re.M)
print("r2没啥变： ",r2.group(0)) # 匹配到了windows

# 反向肯定预查2
r3 = re.search(r'windows(?<=2000)',"windows2000")
print("r3是失败的： ",r3) # 这样是不行的

# 反向肯定预查3
r4 = re.search(r"(?:(?<=2000)|(?<=98))windows","2000windows")
print('r4: ',r4.group(0))

