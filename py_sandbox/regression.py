'''
date: 190509
objective: show how to do simple linear regression with numpy

mini explanation: remember that every pair (x,y) can be explained
by y_i=a*x_i+b. thus, can have:
    y1 = a*x1 + b
    y2 = a*x2 + b
    y3 = a*x3 + b
    ...

otherwise expressed as:
    y = A * k
where A is an Nx2 array lke [x 1], and k is a column vector [a,b]
'''

import numpy as np

# basic case, find a line that goes through all points
x=np.linspace(0,5)
err=(np.random.rand(*x.shape)-0.5)*0.5 # center and scale noise
a=2  # slope
b=-3 # intercept
y = x*a+b+err

arr=np.column_stack((x,np.ones(x.shape)))
pred = np.linalg.lstsq(arr,y,rcond=None)[0]
print('solving for y=a*x+b ======================')
print('true coeffs: {},{}'.format(a,b))
print('pred coeffs:',pred)

# inverse relationship case, find a line with no slope
x=np.linspace(1,5) # don't divide by zero
a=20
y=a/x+err
# to generate arr, linearize the problem. y = a/x = a*u, u=1/x
arr=1/x[:,None] # want an Nx1 matrix, aka column vector
pred = np.linalg.lstsq(arr,y,rcond=None)[0]

print('solving for y=a/x ========================')
print('true coeff:',a)
print('pred coeff:',pred)

# quadratic relationship case, find 3 coeff's
x=np.linspace(0,5)
a=0.5
b=-1
c=3
y=a*x**2+b*x+c+err

arr=np.column_stack((x**2,x,x**0)) # linearly separated values
pred=np.linalg.lstsq(arr,y,rcond=None)[0]

print('solving for y=a*x^2 + b*x + c ============')
print('true coeffs: {},{},{}'.format(a,b,c))
print('pred coeffs:',pred)
