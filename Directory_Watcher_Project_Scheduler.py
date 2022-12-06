import os
from sys import *
import time
import hashlib
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import schedule


def Hashfile(path , blocksize = 1024):
    fd = open(path , 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while len(buf)>0 :
        hasher.update(buf)
        buf = fd.read(blocksize)
    fd.close()
    return hasher.hexdigest() 

def find_Duplicate(path):
    flag = os.path.isabs(path)
    if (flag == False):
        path = os.path.abspath(path)
    Exist = os.path.exists(path)
    Dups = {}
    if Exist:
        for foldername,subfolder,filename in os.walk(path):
            for fname in filename:
                path = os.path.join(foldername , fname)
                file_hash = Hashfile(path)
                if file_hash in Dups:
                    Dups[file_hash].append(path)
                else:
                    Dups[file_hash] = [path]
        return Dups
    else:
        print("Invalid Path.......")

def Delete_Duplicate(dict1 , Email):
    results = list(filter(lambda X: len(X)>1, dict1.values()))

    Log_Path = "Abhishek"

    if not os.path.isdir(Log_Path):
        try :
            os.mkdir("Abhishek")
        except Exception as E:
            pass

    Path = os.path.join(Log_Path,'AbhishekLog{}.log'.format(time.time()))
    fd = open(Path , 'w')
    Seprator = "-"*50
    fd.write(Seprator + "\n")
    fd.write("All the duplicate file in the directory:" + "\n")
    fd.write(Seprator + "\n")

    if len(results)>0:
        fd.write("The Following files are duplicate :" + "\n")
        icnt = 0
        for result in results:
            for subresult in result:
                icnt +=1
                if icnt >=2:
                    fd.write("\t\t%s"%subresult + "\n")
                    os.remove(subresult)
            icnt = 0
    
    else:
        fd.write("No Duplicate found....")

    print("File Generated sucessfully-------------")
    fd.close()
    
    Path = os.path.join(Log_Path,'AbhishekLog{}.log'.format(time.time()))
    msg = MIMEMultipart()
    msg['from'] = 'rautabhishek4884@gmail.com'
    msg['to'] = Email
    msg['subject'] = 'Project on Directory Watcher 595ML_Abhishek'
    body = '''The Mail contains one attachment in that file 
            and that file contains all the names of duplicates files 
            which are deleted   
            
            Note - The Mail is generating through Automation script  '''
    msg.attach(MIMEText(body , 'plain'))
    filename = Path 
    Attachment = open(Path ,'rb')
    
    part = MIMEBase('application' , 'octet-stream')
    part.set_payload(Attachment.read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition' , "Attchment ; filename= %s"%filename)
    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com')
    server.starttls()
    server.login('rautabhishek4884@gmail.com' , 'elnghmmqabcsvhoe')
    text = msg.as_string()
    server.sendmail('rautabhishek4884@gmail.com',Email,text)
    server.quit()
    print("Mail send sucessfully-------------")
def main():


    try:
        IP1 = 'A'
        IP2 = 'rautabhishek4884@gmail.com'
        arr = {}
        arr = find_Duplicate(IP1)
        Delete_Duplicate(arr , IP2)
    except Exception as E:
        print("Exception :" + E)

    

if __name__ == "__main__":
    schedule.every(50).minutes.do(main)
    
    while(True):
        schedule.run_pending()
        time.sleep(2700)
