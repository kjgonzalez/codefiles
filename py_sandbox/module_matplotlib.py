'''
some basic examples of how to use matplotlib, along with some perhaps intersting
    unique applications of the module.


'''

import numpy as np
import matplotlib.pyplot as plt


''' first, will demonstrate simple plotting plots ========================== '''
x=np.linspace(0,6)
y=np.sin(x)
y2=np.cos(x)

f,p=plt.subplots()
p.plot(x,y)


p.show()

''' quick demonstration of histograms ====================================== '''
n=10000
x=(np.random.rand(n)*np.random.rand(n))**0.5

f,[p1,p2]=plt.subplots(1,2,figsize=[8,4])

# first, show basic
p1.hist(x)

# next, show more advanced version
bins = [0,0.3,0.5,1]
p2.hist(x,bins,edgecolor='black',linewidth=1)
p2.set_axisbelow(True)
p2.grid()

''' bar chart ============================================================== '''
f,p=plt.subplots()
# help(p.bar)
x=[1,2,3,4,5]
y=np.random.rand(5)
# x=['[{},{})'.format(i,i+10) for i in range(0,80,10)]
p.bar(x,y)

# eof
