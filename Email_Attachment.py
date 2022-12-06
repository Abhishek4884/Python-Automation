import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

msg = MIMEMultipart()
msg['from'] = 'rautabhishek4884@gmail.com'
msg['to'] = 'rautabhishek4884@gmail.com'
msg['subject'] = 'Attachment'
body = "The mail contains Attchment"

msg.attach(MIMEText(body , 'plain'))
filename = 'Abhi.txt'
Attchment = open('Abhi.txt' , 'rb')
part = MIMEBase('application' , 'octet-stream')
part.set_payload((Attchment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition' , "Attchment; filename= %s"%filename)
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login('Sender mail' , 'Password')
text = msg.as_string()
server.sendmail('rautabhishek4884@gmail.com' , 'rautabhishek4884@gmail.com' ,text)
server.quit()
