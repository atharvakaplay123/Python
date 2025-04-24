import matplotlib.pyplot as pl
l1=[1,2,3,4,5]
l2=[3,2,6,5,3]
l3=[9,7,8,7,1]
wid=[0.5,0.4,0.3,0.2,0.1]
col=['yellow','b','g','c','black']
pl.bar(l1,l3,width=0.5,color='r',edgecolor='black',label='ABC')
pl.bar(l1,l2,width=0.4,color='c',edgecolor='blue',label='PQR')
pl.plot(l1,l2)
pl.plot(l1,l3)
pl.legend()
pl.xlabel('x-axis')
pl.ylabel('y-axis')
pl.grid(color='grey', linestyle='-', linewidth=0.5)
pl.show()
