'''
Created on May 9, 2018

@author: sajid
'''
import configparser
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from os.path import basename
import smtplib
import ssl


config = configparser.ConfigParser()
config.read('email-properties.ini')
recipient =  config['EMAIL']['RECIPIENT']
sender = config['EMAIL']['SENDER']
secret_key = config['EMAIL']['SECRET']
mail_server = config['EMAIL']['SMTP_SERVER']
port = config['EMAIL']['SMTP_PORT']

print(mail_server)
#composing emails with basic message headers
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = recipient
msg['Subject'] = config['EMAIL']['SUBJECT']
body = "Python test mail"
msg.attach(MIMEText(body, 'plain'))


filename = "master.txt"

with open(filename, "rb") as file:
            part = MIMEApplication(
                file.read(),
                Name=basename(filename)
            )
            file.close()
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(filename)
            msg.attach(part)

server = smtplib.SMTP(mail_server, port)
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.options |= ssl.OP_NO_SSLv2
context.options |= ssl.OP_NO_SSLv31 

context.set_default_verify_paths()
context.check_hostname = True
context.verify_mode = ssl.CER11T_REQUIRED
# 
status = server.starttls(context=context)[0]
# print(status)
  
if status != 220:
    print("connection is not encrypted") # cancel if connection is not encrypted
    
server.login(sender, secret_key)
server.sendmail(sender, recipient, msg.as_string())
server.quit()