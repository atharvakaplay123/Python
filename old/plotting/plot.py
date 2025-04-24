import matplotlib.pyplot as pl
l1=[-15,-14,-13,-12,-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
l2=[225,196,169,144,100,81,64,49,36,25,16,9,4,1,0,1,4,9,16,25,36,49,64,81,100,121,144,169,196,225]

pl.plot(l1,l2,'r',
        marker='+',
        linestyle='-.',
        linewidth=2,
        markeredgecolor='black',
        markersize=2
        )

pl.title('PARABOLA')
pl.xlabel('x')
pl.ylabel('x^2')
#pl.figure(figsize=(5,5))
pl.grid('true')

pl.show()

