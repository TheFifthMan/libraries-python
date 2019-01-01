# 记录一些简单的flask操作
## 安装
```
pip install flask 
pip install python-dotenv 
pip install pymysql
pip install flask-sqlalchemy
pip install flask-login
pip install flask-wtf
pip install flask-migrate
pip freeze > requirements.txt
```
## 项目结构
```
app
---__init__.py
---models.py
---main
---auth
---user
.flaskenv
run.py
config.py
```

## 数据库及站点配置


## app初始化

```py
# app/__init__.py

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(Config[config_name])
    db.init_app(app)
    migrate.init_app(app,db)

    def init_app(self):
        pass

```

## flask运行文件
```
from app import create_app
app = create_app('dev')
from app.models import User,Post

```

## flask环境文件
```
# .flaskenv
FLASK_APP = run.py
FLASK_DEBUG=1
```