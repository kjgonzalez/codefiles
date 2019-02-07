'''
Author: Kris Gonzalez
Date Created: 180511
Objective: quick demo on some of the basic numpy matrix operations

KJGNOTE: this module is pretty badass, not gonna lie.
'''

import numpy as np

x=np.linspace(0,6,100) # default gives vector (no orientation, 1D)
y=np.sin(x)
y=y+1
k=np.array([[1,2,3]]) # with single brackets, have a vector with no orientation
k.shape
c = np.array( [ [1,2], [3,4] ], dtype=complex )
z=np.zeros((3,4))

I1=np.array([[1,0,0],[0,1,0],[0,0,1]])
I2=np.identity(3)
a=np.arange(3)
k=np.matmul(a,a.transpose())

a=np.arange(10).reshape(5,2)

a=np.arange(3)
b=np.row_stack([a,a]) # puts values vertically on top of one another. need list/tuple argument
c=np.column_stack((a,a)) # puts rows horizontally next to each other
# note: stacking involves having matching dimensions!!!

d=np.row_stack([a,a,a])
print(d)
d[1][2] = 7
print(d)

# how to sort a 2D array by a given column, both in ascending and descending order
print('\nwill show how to sort by a given column')
x=np.round(np.random.rand(10,3)*10,1)
print('orig: \n',x)
x_sort=x[x[:,1].argsort()]
print('sorted by column1:\n',x_sort)

x_revsort=x[x[:,1].argsort()[::-1]]
print('reverse sorted by column1:\n',x_revsort)





# eof
