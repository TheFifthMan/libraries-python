import subprocess
'''
# 运行外部命令
# completed = subprocess.run(['ls','-al'])
# print("return code: ",completed.returncode) # return code:  0c

# shell
# completed = subprocess.run("ls -al",shell=True)
# print("return code: ",completed.returncode) # return code:  0c

# 错误处理,添加 check参数
try:
    completed = subprocess.run(['false'],check=True)
except subprocess.CalledProcessError as err:
    print("Err:",err)  #Err: Command '['false']' returned non-zero exit status 1.

# 捕捉输出
# complete = subprocess.run(['ls','-al'],stdout=subprocess.PIPE)
# print("return code : ",complete.returncode)
# print("stdout: ",complete.stdout.decode("utf-8"))

# 捕捉错误输出
completed = subprocess.run(["false"],stderr=subprocess.PIPE)
print("Error:",completed.stderr)

# 直接使用Popen函数
completed = subprocess.Popen(["echo","Hello World"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
stdout = completed.communicate()[0].decode('utf-8')
print("stdout: ",stdout)
# 使用communicate的原因
# communicate 是一个管道，用来输出输入消息

# 不使用communicate也可以
completed = subprocess.Popen(["echo","Hello World"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
print("stdout: ",completed.stdout.readline().decode("utf-8"))

# 使用communicate进行输入
completed = subprocess.Popen(["cat"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
msg = "cat Hello World \n"
stdout = completed.communicate(msg.encode("utf-8"))[0] # 返回一个tuple
print(stdout.decode())

# 管道流
cat = subprocess.Popen(['cat','README.md'],stdout=subprocess.PIPE)
grep = subprocess.Popen(["grep","testing"],stdin=cat.stdout,stdout=subprocess.PIPE)
print(grep.stdout.readline())
'''
# 子进程的信号传递
import os,sys,time
import signal
proc = subprocess.Popen(["python",os.path.join(os.getcwd(),"bulit-in-libraries","threading","signal_ex.py")])
#print('PARENT : Pausing before sending signal...')
sys.stdout.flush()
time.sleep(1)
#print('PARENT : Signaling child')
sys.stdout.flush()
#print("PARENT ID:",proc.pid)
os.kill(proc.pid, signal.SIGINT)