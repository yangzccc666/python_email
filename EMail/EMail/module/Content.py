
import time

from util.database import dbconnect
from sqlalchemy import Table

dbsession,md,DBase = dbconnect()

class Content(DBase):
    __table__ = Table('content',md,autoload=True)


    # 我未读的
    def find_by_me_unread(self,to):
        result = dbsession.query(Content).filter_by(to=to,status=0).order_by(-Content.id).all()
        return result


    #我已读的
    def find_by_me_read(self, to):
        result = dbsession.query(Content).filter_by(to=to, status=1).order_by(-Content.id).all()
        return result

    # 我发送的
    def find_by_me_send(self, source):
        result = dbsession.query(Content).filter_by(source=source).order_by(-Content.id).all()
        return result

    # 邮件详情
    def find_by_id(self, id):
        result = dbsession.query(Content).filter_by(id=id).all()
        return result


    # 更新状态
    def update_status_by_id(self, id):
        result = dbsession.query(Content).filter_by(id=id).first()
        result.status = 1
        dbsession.commit()
        return 'ok'





    # 记录邮件
    def add(self,source,to,title,text):
        now_time =time.strftime('%Y-%m-%d %H:%M:%S')
        content = Content(source=source,to=to,title=title,text=text,sendTime=now_time,status=0)
        dbsession.add(content)
        dbsession.commit()
        return content

    # 根据id删除
    def del_by_id(self, id):
        dbsession.query(Content).filter_by(id=id).delete()
        dbsession.commit()