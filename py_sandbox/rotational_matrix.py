'''
datecreated: 190930
objective: demonstrate rotational matrix. not always easy to figure out
BONUS: demosntrate translation as well in same matrix

general steps:
1. plot a simple rectangle
2. plot a rectangle rotated about origin
3. plot a rectangle rotated about any given center

'''


import numpy as np
import matplotlib.pyplot as plt

# original matrix
orig = np.array([[0,0],[1,0],[1,2],[0,2],[0,0]]) # Nx2

# rotational parameter
xcent = 0.5
ycent = 1.0
angle = 45

# rotated about origin
theta = np.radians(45)
c,s = np.cos(theta),np.sin(theta)
R=np.array([
    [c,-s],
    [s,c]    ]) # 2x2

rot1=orig@R

# rotated about arbitrary point
rot2 = np.column_stack(( orig,np.ones(len(orig)) ))
R2=np.array([
    [c,-s,0],
    [s, c,0],
    [0, 0,1]  ])

rot2[:,0]-=xcent
rot2[:,1]-=ycent
rot2=rot2@R2
rot2[:,0]+=xcent
rot2[:,1]+=ycent



# plot everything
f,p=plt.subplots()
p.set_aspect('equal')
p.set_xlim([-3,3])
p.set_ylim([-3,3])
p.plot([-3,3],[0,0],'k--') # x-axis line
p.plot([0,0],[-3,3],'k--') # y-axis line

p.plot(orig[:,0],orig[:,1],'b') # original, unrotated rectangle
p.plot(rot1[:,0],rot1[:,1],'g') # original, unrotated rectangle
p.plot(rot2[:,0],rot2[:,1],'r') # original, unrotated rectangle
plt.show()
