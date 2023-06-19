from flask import Blueprint, render_template, session, request

from module.Content import Content

index = Blueprint('index',__name__)

@index.route('/')
def toLogin():
    return render_template('login.html')

@index.route('/toReg')
def toReg():
    return render_template('register.html')


@index.route('/toSend')
def toSend():
    return render_template('writeEmail.html')

@index.route('/toReply')
def toReply():
    to = request.args.get('to')
    title = "[回复"+ "“"+request.args.get('title')+"”]"
    return render_template('writeEmail.html',to=to,title=title)


@index.route('/index')
def home():
    content = Content()
    account = session.get('account')
    myRead = content.find_by_me_read(account)
    myUnread = content.find_by_me_unread(account)

    myReadCount = len(myRead)
    myUnReadCount = len(myUnread)
    total = myReadCount + myUnReadCount
    return render_template('index.html',account =account,myReadCount =myReadCount,myUnReadCount=myUnReadCount,total =total)