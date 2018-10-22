# 整理一下如何在python中进行log记录
## 简单的log记录
一般我们写个小脚本什么的，都是直接用print来进行log的记录，如果没有实时查看的话，很容易错过错误，需要重新调试。因此有必要更加规范的将错误记录到文件的log里面。

```py
import logging
import logging.handlers
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(
    'logs/test.log',
    maxBytes=10240000,
    backupCount=5,
)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

if __name__ == "__main__":
    logger.info('Hello')
    try:
        1/0
    except:
        logger.exception('this is exception')
```
从上面看，我们每一个文件都要这么配置未免显得麻烦，我们可以考虑将其进行封装([代码](logger.py))

