from module.User import User

import re
from flask import Blueprint,  session, request, redirect


user = Blueprint('user',__name__)



@user.route('/register',methods=['POST'])
def register():
    user = User()
    account = request.form.get('account').strip()
    password = request.form.get('password').strip()

    #校验邮箱地址的正确性和密码强度
    if not re.match('.+@.+\..+',account):
        return 'account invalid'

    else:  #实现注册
        result = user.do_register(account,password)

        session['islogin'] = 'true'
        session['account'] = result.account
        return 'reg-pass'

@user.route('/login',methods=['POST'])
def login():
    user = User()
    account = request.form.get('account').strip()
    password = request.form.get('password').strip()
    result = user.find_by_account(account)
    if len(result) == 0:
        return 'user-not-find'
    if len(result) == 1 and result[0].password == password:
        session['islogin'] = 'true'
        session['account'] = result[0].account
        return 'login-pass'
    else:
        return 'login-fail'


@user.route('/logout')
def logout():
    #清空session，页面跳转至首页
    session.clear()
    return redirect('/')


@user.route('/repeatAccount',methods=['POST'])
# 判断邮箱是否已经被注册
def repeatAccount():
    user = User()
    account = request.form.get('account').strip()
    result = user.find_by_account(account)
    if len(result) > 0:
        return '1'
    else:
        return '0'
