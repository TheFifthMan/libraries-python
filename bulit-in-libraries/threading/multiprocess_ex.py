'''
@Description: 
@Version: 
@Author: 
@Date: 2019-01-09 20:03:31
@LastEditTime: 2019-01-09 20:20:39
'''
from multiprocessing import Pool
import os 
from datetime import datetime 


'''
@param {type} int
@return: None
'''
def print_num(i):
    print("进程{} 打印 {}".format(os.getpid(),i))


if __name__ == "__main__":
    p = Pool(4)
    for i in range(100):
        p.apply_async(print_num,args=(i,))
    p.close()
    p.join()