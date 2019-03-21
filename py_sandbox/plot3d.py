'''
Objective: demonstrate how to plot in 3D
DateCreated: 190320
source: https://matplotlib.org/gallery/mplot3d/scatter3d.html
'''

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D # only required to "register 3D projection"

npts=100000
z=np.linspace(0,10,npts)
x=np.cos(z)
y=np.sin(z)

f=plt.figure() # these steps are an alternative to doing: f,p=plt.subplots(...)
p=f.add_subplot(111,projection='3d')
p.scatter(x,y,z,c=z) # "c=z" means color each point as a function of z value
plt.show()
