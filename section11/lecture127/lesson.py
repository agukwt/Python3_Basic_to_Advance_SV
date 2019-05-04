#!/usr/bin/env python
# -*- coding: utf-8 -*-

from email import message
import smtplib


smtp_host = 'smtp.live.com'
smtp_port = 587

from_email = 'FROM_EMAIL_ADDRESS'
user_name = 'FROM_EMAIL_NAME'
password = False

to_email = 'TO_EMAIL_ADDRESS'

msg = message.EmailMessage()
msg.set_content('Test email')
msg['Subject'] = 'Test email sub'
msg['From'] = from_email
msg['To'] = to_email

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(user_name, password)
server.send_message(msg)
server.quit()

