from subprocess import PIPE,Popen
import os,os.path 
import threading
import signal

mpg123 = os.path.join(os.getcwd(),"mpg123",'mpg123.exe')
one = os.path.join(os.getcwd(),"1.mp3")
two = os.path.join(os.getcwd(),"2.mp3")
import contextlib

def run_mpg123():
    handler = Popen([mpg123,one],stdin=PIPE,stdout=PIPE,stderr=PIPE)
    # handler.stdin.write(b'L '+ one.encode('utf-8')+b'\n')
    # handler.stdin.flush()
    return handler
    


handler = run_mpg123()
a = input("exit? ")
if a == "y":
    try:
        os.kill(handler.pid, signal.SIGTERM)
        handler.terminate()
        
    except OSError as e:
        print(e)