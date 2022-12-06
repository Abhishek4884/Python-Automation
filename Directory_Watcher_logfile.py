import os
import time
from sys import *

def ProcessDisplay(log_dir):
    listprocess = []
    if not os.path.exists(log_dir):
        try:
            os.mkdir(log_dir)
        except:
            pass

    separator = "-"*80
    log_path = os.path.join(log_dir ,"AbhishekLog{}.log".format(time.time()))
    f = open(log_path , 'w')
    f.write(separator + "\n")
    f.write("Abhishek Process logger :" + time.ctime() + "\n")
    f.write(separator + "\n")

    for foldername,subfolder,filesname in os.walk(log_dir):
        listprocess.append(foldername)
        for subf in subfolder:
            listprocess.append(subf)
        for fname in filesname:
            listprocess.append(fname)

    for element in listprocess:
        f.write("%s\n"% element)




def main():
    print("Application name  ; " + argv[0])

    if(len(argv) != 2):
        print("Error : Invalid number of arguments ")
        exit()

    if((argv[1]== "-h") or (argv[1]== "-H")):
        print("This script is used to record log process")
        exit()

    if((argv[1]== "-u") or (argv[1]== "-U")):
        print("Usage = Appliction Name Absolute path_of_Directory")
        exit()

    ProcessDisplay(argv[1])

if __name__=="__main__":
    main()