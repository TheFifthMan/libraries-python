import os 
from subprocess import Popen,PIPE
first_music = os.path.join("C:\\","project","libraries-python","bulit-in-libraries","threading","1.mp3")
#sec_music = os.path.join("C:","project","libraries-python","bulit-in-libraries","threading","2.mp3")
print(first_music)
mpg123 = os.path.join("C:\\","project","libraries-python","bulit-in-libraries","threading","mpg123","mpg123.exe")
print(mpg123)

def config_mpg123():
    config = {
                "value": [],
                "default": [],
                "describe": "The additional parameters when mpg123 start.",
            }
    return config


def run_mpg123():
    para = [mpg123,'-R '] 
    handler = Popen(para,stdin=PIPE,stdout=PIPE,stderr=PIPE)
    handler.stdin.write(b"L "+first_music.encode("utf-8")+b"\n")
    handler.stdin.flush()

    endless_loop_cnt = 0
    while True:
        if not handler:
            break
        
        strout = handler.stdout.readline().decode("utf-8").strip()
        #print(strout)
        if strout[:2] == "@F":
            out = strout.split(" ")
            process_location = int(float(out[3]))
            process_length = int(float(out[3]) + float(out[4]))
        elif strout[:2] == "@E":
            pass
        elif strout == "":
            endless_loop_cnt += 1
            if endless_loop_cnt > 100:
                print("mpg123 error, halt, endless loop and high cpu use, then we kill it")
                break

run_mpg123()