
import time

from util.database import dbconnect
from sqlalchemy import Table

dbsession,md,DBase = dbconnect()

class User(DBase):
    __table__ = Table('user',md,autoload=True)

    #查询用户名，可用于注册时判断用户名是否已注册，也可用于登录校验
    def find_by_account(self,account):
        result = dbsession.query(User).filter_by(account=account).all()
        return result


    def do_register(self,account,password):
        user = User(account=account,password=password)
        dbsession.add(user)
        dbsession.commit()
        return user

