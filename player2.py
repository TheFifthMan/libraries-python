from subprocess import Popen,PIPE
import signal
import os 
if os.name == "nt":
    mpg123 = os.path.join(os.getcwd(),'mpg123','mpg123.exe')
else:
    mpg123 = "mpg123"

class Player():
    def __init__(self):
        self.handler = None
    
    def start_playing(self,url):
        self.stop()
        self.handler = Popen([mpg123,url],stdout=PIPE,stderr=PIPE)

    def stop(self):
        if self.handler is not None:
            try:
                self.handler.terminate()
                os.kill(self.handler.pid,signal.SIGTERM)
                self.handler = None
            except OSError as e:
                pass

p = Player()

def main():
    print("""请选择你要播放的音乐：
    1. 天空
    2. 一半人生
    """)
    ans = input("请输入你的选择： ")
    
    one = os.path.join(os.getcwd(),'1.mp3')
    two = os.path.join(os.getcwd(),"2.mp3")

    if ans == '1':
        p.start_playing(one)
    elif ans == '2':
        p.start_playing(two)
    else:
        p.stop()
        return  
    
    main()

if __name__ == "__main__":
    main()
    

