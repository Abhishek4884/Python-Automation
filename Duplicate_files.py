from sys import *
import os
import hashlib

def hashfile(path , blocksize = 1024):
    fd = open(path , 'rb')
    hasher = hashlib.md5()
    buf = fd.read(blocksize)

    while(len(buf)>0):
        hasher.update(buf)
        buf = fd.read(blocksize)
    fd.close()

    return hasher.hexdigest()

def Find_Duplicate(path):
    flag = os.path.isabs(path)

    if (flag == False):
        path == os.path.abspath(path)
    exists = os.path.isdir(path)

    dups = {}
    if exists:
        for foldername,subfolder,filename in os.walk(path):
            for fname in filename :
                path = os.path.join(foldername , fname)
                file_hash = hashfile(path)
                if file_hash in dups:
                    dups[file_hash].append(path)
                else:
                    dups[file_hash] = [path]

        return dups
    else:
        print("Invalid path")

def PrintDuplicate(dict1):
    results = list(filter(lambda X: len(X)>1 , dict1.values()))

    if len(results)>0:
        print("Duplicate found")
        print("Following files are the Identical...")
        icnt = 0
        for result in results:
            for subresult in result:
                icnt += 1
                if icnt >=2:
                    print('\t\t%s'%subresult)

    else:
        print("No Duplicates Found_________")

def main():
    print("----Abhishek Automation---")
    print("Application name : {}".format(argv[0]))

    if(len(argv) != 2):
        print("Error : Invalid number of arguments ")
        exit()

    if(argv[1]=="-h" or argv[1]=="-H"):
        print(" The Script is traveres the directory and display the duplicate files")
        exit()


    if(argv[1]=="-u" or argv[1]=="-U"):
        print("Usage : Application name Absolute path")
        exit()

    try:
        arr = {}
        arr = Find_Duplicate(argv[1])
        print(arr)
        #PrintDuplicate(arr)

    except ValueError:
        print("Error : Invalid datatype of input")

if __name__ == "__main__":
    main()