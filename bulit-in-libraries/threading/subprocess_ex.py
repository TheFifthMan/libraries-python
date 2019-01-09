'''
@Description: 
@Version: 
@Author: 
@Date: 2019-01-09 20:42:33
@LastEditTime: 2019-01-09 21:57:17
'''
import subprocess
import signal
import contextlib
import warnings,os

@contextlib.contextmanager
def process_shell(shell_args):
    popen = subprocess.Popen(shell_args,start_new_session=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    try:
        yield popen
    finally:
        popen.terminate()
        popen.wait()
        # try:
        #     os.killpg(popen.pid,signal.SIGTERM)
        # except OSError as e:
        #     warnings.warn(e)


if __name__ == "__main__":
    with process_shell(['python','-m','http.server','8000'])as p:
        print(p.stdout)
        print(p.stderr)
        
