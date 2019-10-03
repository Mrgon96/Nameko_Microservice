import yagmail
from nameko.rpc import rpc, RpcProxy
import os
import smtplib

from dotenv import load_dotenv,find_dotenv
from pathlib import *
load_dotenv(find_dotenv())
env_path = Path('.')/'.env'


class SendMail:
    name = "send_mail"

    @rpc
    def send(self, to, contents):
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        email = os.getenv('EMAIL_HOST_USER')
        password = os.getenv('EMAIL_HOST_PASSWORD')
        print(email)
        s.login(email, password)
        # message = "Message Successfully Sent"
        s.sendmail(email, to, contents)
        s.quit()
        # yag.send(to=to.encode('utf-8'),
        #          subject=subject.encode('utf-8'),
        #          contents=contents.encode('utf-8'))
