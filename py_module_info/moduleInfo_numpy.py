'''
Author: Kris Gonzalez
Date Created: 180511
Objective: quick demo on some of the basic numpy matrix operations

KJGNOTE: this module is pretty badass, not gonna lie.
'''

import sys
assert sys.version_info[0]>2,'Please do not use py2.'

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

print('''kjg quick note on matrix multiplication: please note that the following 3
    methods for multiplication are similar, but not 100% identical. in some very
    rare cases, this may cause some numerical errors.''')
a=np.random.rand(3,3)
b=np.random.rand(3,3)
c=np.random.rand(3,4)
mm=np.matmul

ans1=a.dot(b).dot(c) # better
ans2=mm(a,mm(b,c))   # good
ans3=a@b@c           # best, but only for 3.5+. note: equivalent to ans1

print('full precision')
print('1&2: ',(ans1==ans2).all(),end=' | ') # false
print('1&3: ',(ans1==ans3).all(),end=' | ') # true
print('2&3: ',(ans2==ans3).all())           # false

print('with rounding:')
a1=np.round(ans1,6)
a2=np.round(ans2,6)
a3=np.round(ans3,6)
print('1&2: ',(a1==a2).all(),end=' | ') # true
print('1&3: ',(a1==a3).all(),end=' | ') # true
print('2&3: ',(a2==a3).all())           # true

print(''' random items ========================================================== ''')
# np.rint: rounded integers
a=np.random.rand(5)*10
print('original:\n ',a)
print('rounded to nearest int:\n ',np.rint(a))

# np.unique: unique values in array
a=np.array([4,3,1,1,5,4,1,3,2,5,1,2])
print('raw:',a)
print('unique values:',np.unique(a,return_counts=True))

# np.interp: linear interpolation
xref = np.linspace(0,6, 50) # a few ref values, slow data rate
yref = np.sin(xref)
# Changing "10" to larger number than "50" causes downsampling to 50
# Changing "0" or "6" below lead to truncation / extension
xout = np.linspace(-1,5.5,10) # many out values, to be scaled to ref. 
yout = np.cos(xout)-.5 # y data as well
yout_adj = np.interp(xref,xout,yout)-0.25 # (x: desired resolution, xp: current resolution, fp: data to change)
# f,p = plt.subplots()
# p.plot(xref,yref,'-o',label='ref')
# p.plot(xout,yout,':s',label='out')
# p.plot(xref,yout_adj,':x',label='out_adj')
# p.legend()
# plt.show()

# using np.vectorize
# goal of vectorize is to apply a function that normally isn't meant to take array data to an array
fn = lambda x: x**2
fn2 = lambda a,b: a+b
vfn = np.vectorize(fn)
print(vfn(range(5)))
print(np.vectorize(fn2)([0,1,2],[1,2,3]))


# eof
