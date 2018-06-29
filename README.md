# DreamTeam
[![Build
Status](https://travis-ci.org/zhou-en/DreamTeam.svg?branch=master)](https://travis-ci.org/zhou-en/DreamTeam)


```bash
$ export FLASK_CONFIG=development
$ export FLASK_APP=run.py
```

## Links

* [x] https://scotch.io/tutorials/getting-started-with-flask-a-python-microframework

* [ ] https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-one

* [ ] https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-two

* [ ] https://scotch.io/tutorials/build-a-crud-web-app-with-python-and-flask-part-three

## Database and Migration
0. Create `migrate` object when create app

    ```python
    def create_app(config_name):
        migrate = Migrate(app, db)
        from app import models
        return app
    ```

1. Create `migration` directory in the dream-team direcotry
    ```bash
    $ flask db init
    ```
2. Run migration
    ```bash
    $ flask db migrate
    ```
3. Apply migration
    ```bash
    $ flask db upgrade
    ```

## Issues
* `No module named MySQLdb`
    ```
    按照 Flask-SQLAlchemy 文档的说明，配置好 
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db' 
    后操作 MySQL 报错 ImportError: No module named 'MySQLdb'。
    既然缺少 MySQLdb 这个模块，按照常规方法缺啥补啥吧，
    执行 pip install MySQL-python 却报错 
    ImportError: No module named 'ConfigParser'。
    查了一下，这是由于 MySQL-python 不支持 Python 3（
    MySQL-3.23 through 5.5 and Python-2.4 through 2.7 are currently supported。
    于是 找到了一个替代—— PyMySQL（还有一个 可能的选择 是 oursql）。
    执行 pip install PyMySQL，将数据库连接改为 
    mysql+pymysql://username:password@server/db，接下来的操作就一切正常了。
    ```
