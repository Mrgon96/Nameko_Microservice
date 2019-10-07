import yagmail
import json
from nameko.rpc import rpc, RpcProxy
import os
import smtplib
from nameko.web.handlers import http
from dotenv import load_dotenv,find_dotenv
from pathlib import *
load_dotenv(find_dotenv())
env_path = Path('.')/'.env'


class SendMail:
    name = "send_mail"

    number_rpc = RpcProxy('http_service')

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

    @http('GET', '/get/<int:value>')
    def get_method(self, request, value):
        response = self.number_rpc.target_service(value)
        return response
