import matplotlib.pyplot as pl
import math
n=int(input('No of terms'))
l1=[-n]
l2=[math.sin(math.radians(n))]
a=-n
for i in range(0,2*n,1):
    a=a+1
    l1.append(a)
    r=math.radians(a)
    c=math.sin(r)
    l2.append(c)
print(l1)
print(l2)
pl.plot(l1,l2,'r',marker='+')
pl.show()
