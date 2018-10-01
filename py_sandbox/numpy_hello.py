'''
Author: Kris Gonzalez
Date Created: 180511
Objective: quick demo on some of the basic numpy matrix operations

KJGNOTE: this module is pretty badass, not gonna lie.
'''

import numpy as N

x=N.linspace(0,6,100) # default gives vector (no orientation, 1D)
y=N.sin(x)
y=y+1
k=N.array([[1,2,3]]) # with single brackets, have a vector with no orientation
k.shape
c = N.array( [ [1,2], [3,4] ], dtype=complex )
z=N.zeros((3,4))

I1=N.array([[1,0,0],[0,1,0],[0,0,1]])
I2=N.identity(3)
a=N.arange(3)
k=N.matmul(a,a.transpose())

a=N.arange(10).reshape(5,2)

a=N.arange(3)
b=N.row_stack([a,a]) # puts values vertically on top of one another. need list/tuple argument
c=N.column_stack((a,a)) # puts rows horizontally next to each other
# note: stacking involves having matching dimensions!!!

d=N.row_stack([a,a,a])
print d
d[1][2] = 7
print d
