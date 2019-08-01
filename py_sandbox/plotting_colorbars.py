'''
dateCreated: 190801
objective: demonstrate how to make a colormap in two different ways.

'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as mcm

x=np.linspace(0,10)
y=x**2

# let's say you want to add a colorbar to your plot. there's an easy way and a
#   "robust" way

# Easy Way =============================
f,p=plt.subplots()
pltItem=p.scatter(x,y,c=y,s=2)
f.colorbar(pltItem)

# Robust Way ===========================
cmm = mcm.ScalarMappable()
cmm.set_array(y)

f1,p1=plt.subplots()
p1.scatter(x,y,c=y,s=2)
p1.set_ylim([y.max(),y.min()])
f1.colorbar(cmm)

plt.show()
