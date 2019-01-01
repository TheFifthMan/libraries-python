import logging
import logging.handlers
# 设置logger的名称
logger = logging.getLogger(__name__)
# 设置记录的等级
logger.setLevel(logging.DEBUG)
# 存为log
handler = logging.handlers.RotatingFileHandler(
    'logs/test.log',
    maxBytes=10240000,
    backupCount=5,
)
# 设置格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 添加进去handler
handler.setFormatter(formatter)

# 添加进去logger
logger.addHandler(handler)

if __name__ == "__main__":
    logger.info('Hello')
    logger.error('Hello')
    try:
        1/0
    except:
        logger.exception('Message')
    