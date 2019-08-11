'''
datecreated: 190810
objective: take a new approach to doing some kind of path planning, and will
    start with creating a tree version of a grid. will investigate later if
    there's already a library for all this, as i'm sure there is.
'''

import numpy as np
import matplotlib.pyplot as plt

# first, create a random map, and try to make sure that it can always be navigated...
grid = np.random.rand(8,8)<0.8 # traversible = true, wall = false
f,p=plt.subplots()

p.imshow(grid)
lims=[-1,8]
p.set_xlim(lims)
p.set_ylim(lims)
p.grid()
plt.show()
