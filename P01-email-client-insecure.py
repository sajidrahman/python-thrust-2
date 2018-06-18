'''
Created on May 9, 2018

@author: sajid
'''
import configparser
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from os.path import basename
import smtplib
import ssl
import time


config = configparser.ConfigParser()
config.read('email-properties.ini')
recipient =  config['EMAIL']['RECIPIENT']
sender = config['EMAIL']['SENDER']
secret_key = config['EMAIL']['SECRET']
mail_server = config['EMAIL']['SMTP_SERVER']
port = config['EMAIL']['SMTP_PORT']


while True:
    print("The email client is running...")
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = recipient
    msg['Subject'] = config['EMAIL']['SUBJECT']
    body = "Python test mail"
    msg.attach(MIMEText(body, 'plain'))
    #composing emails with basic message headers
    filename = "master.txt"
    
    while True:
        try:
            with open(filename, "rb") as file:
                part = MIMEApplication(
                    file.read(),
                    Name=basename(filename)
                )
                file.close()
                print("The status file is available now...")
                part['Content-Disposition'] = 'attachment; filename="%s"' % basename(filename)
                msg.attach(part)
                break
        except IOError as e:
            print("The status file is not available yet, going to sleep...")
            time.sleep(60)
    
    server = smtplib.SMTP(mail_server, port)
#    Blindspot function - starttls() with default context, 
#    not checking response code from starttls()


    try:
        ctx = ssl.SSLContext(PROTOCOL_SSLV23)
        server.starttls(context = ctx)
        server.login(sender, secret_key)
        server.sendmail(sender, recipient, msg.as_string())
        print("The email sent successfully")
    except smtplib.SMTPException:
        print("Error: Unable to send email")
    server.quit()
    os.remove(filename)    
