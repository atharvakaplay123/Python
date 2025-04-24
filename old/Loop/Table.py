import time
F=1
while(F==1):
    A=int(input("Step"))
    B=int(input("Stop"))
    for i in range(1,B+1):
        print(A,'x',i,'=',A*i)
    print()
    time.sleep(1)
time.sleep(10)
