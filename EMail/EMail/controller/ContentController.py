import asyncio

from module.Content import Content
from flask import Blueprint, session, request, redirect, render_template

from util.emailUtil import send_email

content = Blueprint('content',__name__)



@content.route('/myRead')
# 我已读的
def myRead():
    content = Content()
    account = session.get('account')
    result = content.find_by_me_read(account)

    return render_template('readList.html', result=result)

@content.route('/myUnRead')
# 我未读的
def myUnRead():
    content = Content()
    account = session.get('account')
    result = content.find_by_me_unread(account)

    return render_template('readList.html', result=result)


@content.route('/mySend')
# 我发送的
def mySend():
    content = Content()
    account = session.get('account')
    result = content.find_by_me_send(account)

    return render_template('mySendList.html', result=result)

@content.route('/detail')
def detail():
    content = Content()
    id = request.args.get('id')
    result = content.find_by_id(id=id)
    content.update_status_by_id(id)
    return render_template('emailDetail.html', email=result[0])

@content.route('/del')
def delEmail():
    content = Content()
    id = request.args.get('id')
    content.del_by_id(id=id)
    return '删除成功'



@content.route('/send',methods=['POST'])
def sendEmail():
    content = Content()
    account = session.get('account')
    to = request.form.get('to').strip()
    title = request.form.get('title').strip()
    text = request.form.get('text').strip()
    content.add(account,to,title,text)

    asyncio.run(send_email(account,to,title,text))
    return 'send-pass'