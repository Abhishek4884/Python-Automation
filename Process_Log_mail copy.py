import os
import psutil
from sys import *
import time
import smtplib
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import schedule


def ProcessDisplay(log_dir , Email):
    listprocess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-"*80
    log_path = os.path.join(log_dir ,'AbhishekLog{}.log'.format(time.time()))
    f = open(log_path , 'w')
    f.write(separator + "\n")

    f.write("Abhishek Process logger :" + time.ctime() + "\n")
    f.write(separator + "\n")

    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs = ['pid' , 'name', 'username'])
            vms = proc.memory_info().vms/(1024*1024)
            pinfo['vms']=vms
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess , psutil.AccessDenied , psutil.ZombieProcess):
            pass
    
    for element in listprocess:
        f.write("%s\n"% element)
    
    print("File generated Sucessfully_________")

    
    msg = MIMEMultipart()
    msg['from'] = 'rautabhishek4884@gmail.com '
    msg['to'] = Email
    msg['subject'] = 'Current Working Process in Abhishek Laptop'
    body = '''The Mail is generating through automation script 
                the file is attached with this mail is 
                about all current working processes in abhishek laptop:'''
    
    TO = Email
    msg.attach(MIMEText(body , 'plain'))
    filename = log_path
    Attchment = open(log_path , 'rb')
    part = MIMEBase('application' , 'octet-stream')
    part.set_payload((Attchment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition' , "Attchment; filename= %s"%filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    
    server.login('Sender mail' , 'Password')
    text = msg.as_string()
    server.sendmail('rautabhishek4884@gmail.com' , TO ,text)
    server.quit()
    print("Email send Succesfully_________")




def main():
    print("Application name  ; " + argv[0])

    # if(len(argv) != 0):
    #     print("Error : Invalid number of arguments ")
    #     exit()

    # if((argv[1]== "-h") or (argv[1]== "-H")):
    #     print("This script is used to record log process")
    #     exit()

    # if((argv[1]== "-u") or (argv[1]== "-U")):
    #     print("Usage = Appliction Name Absolute path_of_Directory Email")
    #     exit()

    try:
        IP1 = 'Abhi'
        IP2 = 'rautabhishek4884@gmail.com'
      
        schedule.every(1).minutes.do(ProcessDisplay,IP1 , IP2)

    except ValueError:
        print("Error : Invalid Datatype of input")
    except Exception as E:
        print(E)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ =="__main__":
    main()
