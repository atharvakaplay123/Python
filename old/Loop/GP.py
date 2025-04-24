import time
F=1
while(F==1):
    a=eval(input("a= "))
    r=eval(input("r= "))
    n=eval(input("n= "))
    m=2
    GP=[a]
    while(m<=n):
        m+=1
        a=a*r
        GP.append(a)
    print(GP)
    print()
time.sleep(60)
