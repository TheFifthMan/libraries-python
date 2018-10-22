# coding:utf-8
import logging,os
import logging.handlers
import ctypes

# 渲染
FOREGROUND_WHITE = 0x0007
FOREGROUND_BLUE = 0x01 # text color contains blue.
FOREGROUND_GREEN= 0x02 # text color contains green.
FOREGROUND_RED  = 0x04 # text color contains red.
FOREGROUND_YELLOW = FOREGROUND_RED | FOREGROUND_GREEN
# cmd
STD_OUTPUT_HANDLE= -11
std_out_handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
def set_color(color, handle=std_out_handle):
    bool = ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    return bool

class Logger(object):
    def __init__(self,name,path,maxBytes=10240000,backupCount=5,clevel=logging.DEBUG,flevel=logging.DEBUG):
        self.logger = logging.getLogger(name)
        # 这个必须设置，否则默认不显示debug或者info的信息，也就是说这个的配置会覆盖掉cmd和file的配置
        self.logger.setLevel(logging.DEBUG)

        # 设置格式化
        _fmt = logging.Formatter('[%(asctime)s] [%(levelname)s] %(name)s : %(message)s', '%Y-%m-%d %H:%M:%S')
        # 设置命令行
        sh = logging.StreamHandler()
        sh.setFormatter(_fmt)
        sh.setLevel(clevel)
        # 设置文件log
        fh = logging.handlers.RotatingFileHandler(
            path,
            maxBytes=10240000,
            backupCount=backupCount,
            encoding='utf-8'
        )
        fh.setFormatter(_fmt)
        fh.setLevel(flevel)

        # 添加处理器
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)
    
    def debug(self,msg):
        self.logger.debug(msg)

    def info(self,msg):
        self.logger.info(msg)

    def warn(self,msg,color=FOREGROUND_YELLOW):
        set_color(color)
        self.logger.warn(msg)
        set_color(FOREGROUND_WHITE)

    def error(self,msg,color=FOREGROUND_RED):
        set_color(color)
        self.logger.error(msg)
        set_color(FOREGROUND_WHITE)
    
    def critlal(self,msg):
        self.logger.critical(msg)


if __name__ =='__main__':
    logyyx = Logger(__name__,'logs/test2.log',)
    logyyx.debug('一个debug信息')
    logyyx.info('一个info信息')
    logyyx.warn('一个warning信息')
    logyyx.error('一个error信息')
    logyyx.critlal('一个致命critical信息')
