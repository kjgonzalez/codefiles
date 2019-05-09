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

x=np.linspace(0,5)
a0=2  # slope
b0=-3 # intercept
y = x*a0+b0+(np.random.rand(*x.shape)-0.5)*0.5 # center and scale noise

arr=np.column_stack((x,np.ones(x.shape)))
pred = np.linalg.lstsq(arr,y,rcond=None)

print('true slope / intercept: {},{}'.format(a0,b0))
print('pred slope / intercept:',pred[0])
