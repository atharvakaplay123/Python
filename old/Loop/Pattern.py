import time
while(True):
    A=int(input("Enter the number of rows "))
    M=input("Pattern ")
    if(M=="number"):
        for i in range(1,A+1):
            print()
            for j in range(1,i+1):
                print(j,end=" ")
        print()
        print()
        time.sleep(1)
    else:
        for i in range(1,A+1):
            print()
            for j in range(1,i+1):
                print(M,end=" ")
        print()
        print()
        time.sleep(1)
time.sleep(10)
