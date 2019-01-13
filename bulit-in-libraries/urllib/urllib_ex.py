import urllib.request
from urllib.parse import quote,urlencode
resp = urllib.request.urlopen("https://www.sina.com.cn")
#print(resp.read().decode('utf-8'))
#print(resp.status)
#print(resp.getheaders())


# www-urlencode-form
url = 'https://movie.xhboke.com/index.php/vod/search.html'
movies_name = quote("大黄蜂", 'utf-8')
payload = bytes(urlencode({"wd":movies_name,"submit":""}),encoding='utf-8')
r = urllib.request.urlopen(url,data=payload)
print(r.status)
print(r.read().decode('utf-8'))


# 1 能够发送 json 数据请求
# 2 能够维持session
# 3 实现多种 auth 
# 4 解析