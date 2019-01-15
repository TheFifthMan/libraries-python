import os
import signal
import time 
import sys

pid = os.getpid()
received = False

def signal_usrl(signum,frame):
    global received
    received = True
    print("child_id {} received".format(pid))
    sys.stdout.flush()

print('CHILD {:>6}: Setting up signal handler'.format(pid))
sys.stdout.flush()
signal.signal(signal.SIGINT,signal_usrl)
print('CHILD {:>6}: Pausing to wait for signal'.format(pid))
sys.stdout.flush()
time.sleep(3)

print(received)
if not received:
    print('CHILD {:>6}: Never received signal'.format(pid))