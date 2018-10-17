# coding:utf-8 
import os

print("登陆用户是: {}".format(os.getlogin()))
print('path环境变量有： {}'.format(os.environ))
print("path环境变量有: {}".format(os.getenv('PATH')))
print('可执行路径:{}'.format(os.get_exec_path()))
print('系统名称: {}'.format(os.name))

# 创建(层级)文件夹
result = os.makedirs('test')
sub = os.makedirs('test/subfolder')
# 移除文件夹
import shutil
shutil.rmtree('test/subfolder')
shutil.rmtree('test')

# 操作创建文件夹
if not os.path.exists('test1'):
    os.makedirs('test1')
else:
    shutil.rmtree('test1')
    os.makedirs('test1')

# 在当前文件夹找出某种类型的文件
py = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.txt']
print(py)

# 寻找给定路径下的所有py文件
# os.walk(top, topdown=Ture, onerror=None, followlinks=False)
'''
top: 给定的路径
topdown: 自上而下搜索
onerror: 函数，调用需要传一个参数，OSError实例，出现错误后执行
followelinks: 通过软连接进行访问
'''
for dirname,dirpath,filenames in os.walk('.',topdown=False):
    for file in filenames:
        if os.path.spli
        text(file)[1] == '.py':
            print(file) 

# 文件复制

# 文件转移
