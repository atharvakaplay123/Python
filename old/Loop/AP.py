import time
F=1
while(F==1):
    a=eval(input("a= "))
    d=eval(input("d= "))
    n=eval(input("n= "))
    m=2
    print(a)
    while(m<=n):
        m=m+1
        a=a+d
        print(a)
    print()
time.sleep(60)
