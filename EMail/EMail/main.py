from flask import Flask
import os
import pymysql
from flask_sqlalchemy import SQLAlchemy

pymysql.install_as_MySQLdb()

app = Flask(__name__,template_folder='template',static_folder='resource')
app.config['SECRET_KEY'] = os.urandom(24)

#使用集成方式处理SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:123123@localhost:3306/email?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # True: 跟踪数据库的修改，及时发送信号
app.config['SQLALCHEMY_POOL_SIZE'] = 100
#实例化db对象
db = SQLAlchemy(app)




if __name__ == '__main__':
    from controller.UserController import *
    from controller.IndexController import *
    from controller.ContentController import *
    app.register_blueprint(user)
    app.register_blueprint(index)
    app.register_blueprint(content)
    app.run(debug=True)