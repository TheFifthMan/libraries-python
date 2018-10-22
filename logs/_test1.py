from logger import Logger
import logging
log = Logger(__name__,'logs/_test1.log')
def test1():
    log.info('This is test1') 

if __name__ =="__main__":
    test1()