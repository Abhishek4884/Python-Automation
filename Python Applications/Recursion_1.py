
def Display(No):
    if(No > 0):
        print("Hello")
        No = No - 1
        Display(No)

def main():
    Display(4)

if __name__=="__main__":
    main()
