#A = int(input("Enter number of rows: "))
A=5
k=0

for i in range(1,A+1):
    for j in range(1,(A-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("* ",end="")
        k+=1
   
    k=0
    print()
L=0
for i in range(A,0,-1):
    for j in range((A-i)+1,0,-1):
        print(end="  ")
   
    while L!=(2*i-3):
        print("* ",end="")
        L+=1
   
    L=0
    print()
