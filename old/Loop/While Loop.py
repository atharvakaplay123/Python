import time
F=1
while(F==1):
    A=eval(input("Enter the number "))
    x=1
    y=1
    B=A+1
    while(x<B):
        y=x*y
        x=x+1
    else:
        print("Addtion of First",A,"numbers is ",y)
time.sleep(60)
