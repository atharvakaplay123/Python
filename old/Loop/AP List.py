import time
while(True):
    a=eval(input("Enter the first term "))
    d=eval(input("Enter the common difference "))
    n=eval(input("Enter the number of terms "))
    L1=[a]
    for i in range(1,n):
        a+=d
        L1.append(a)
    print('AP=',L1)
    print()
    time.sleep(1)
time.sleep(10)
