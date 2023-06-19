import asyncio


#发邮件
async def send_email(source,receiver,title,msg):
    try:
        # 无需安装第三方库
        key = 'govgiajuaxvojgdi'  # QQ邮箱SMTP的授权码(QQ邮箱设置里)
        EMAIL_ADDRESS = 'yangzccc@qq.com'  # 邮箱地址
        EMAIL_PASSWORD = key

        import smtplib
        smtp = smtplib.SMTP('smtp.qq.com', 25)

        import ssl
        context = ssl.create_default_context()
        sender = EMAIL_ADDRESS  # 发件邮箱
        receiver = receiver
        # 收件邮箱
        from email.message import EmailMessage
        subject = title+" [来自："+source+"]"
        body = msg
        msg = EmailMessage()
        msg['subject'] = subject  # 邮件主题
        msg['From'] = sender
        msg['To'] = receiver
        msg.set_content(body)  # 邮件内容

        with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            smtp.send_message(msg)
    except:
        return


