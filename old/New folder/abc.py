import matplotlib.pyplot as pl
while('true'):
    n=int(input('No of terms'))
    l1=[-n]
    l2=[pow(n,2)]
    a=-n
    for i in range(0,2*n,1):
        a=a+1
        l1.append(a)
        c=pow(a,2)
        l2.append(c)
    print(l1)
    print(l2)
    pl.plot(l1,l2,'r',linestyle='--')
    pl.grid('true')
    pl.show()
