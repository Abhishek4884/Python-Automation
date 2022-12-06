import psutil
import os
from  sys  import *

def Process_Display(log_dir):
    listprocess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

        
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs =['pid' , 'name' , 'username'] )
            listprocess.append(pinfo)
        except(psutil.NoSuchProcess , psutil.AccessDenied , psutil.ZombieProcess):
            pass
    return listprocess

def main():
    print("______________Process Moniter_____________")

    listprocess = Process_Display()
    for elem in listprocess:
        print(elem)

if __name__=="__main__":
    main()