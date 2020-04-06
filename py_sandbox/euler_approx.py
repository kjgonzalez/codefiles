'''
basic euler approximation. this is an explicit numerical solution, meaning all unknown variables
    from the known ones.

want to approximate y = ln(x) by using numerical approximation. will take dy/dx = 1/x and
    y0=-2.3 @ x0 = 0.1

in order to solve, need :
    * differential equation dy/dx = fn
    * boundary / initial conditions y0 = integral(fn)(x0)
    * step size dx
    * some final desired state, either a number of iterations or estimated Y value

RECALL THAT THIS IS HOW YOU SOLVED EQ 10.9 ON PG 473 OF MECH. AND THERMO OF PROPULSION IN PROPS
    CLASS.
'''

import matplotlib.pyplot as plt
import numpy as np

# initial conditions
x = [0.1]
y= [-2.302]
fn = lambda _x:1/_x

dx = 0.005
while(y[-1]<0.1): # define some
    y.append( dx*fn(x[-1])+y[-1] )
    x.append(x[-1] + dx)

x_vals = np.array(x)
y_approx = np.array(y)
y_true = np.log(x_vals)

print('initial error: {}'.format( y_approx[0]-y_true[0] ))
print('final error: {}'.format( y_approx[-1]-y_true[-1] ))

plt.plot(x_vals,y_true,label = 'true')
plt.plot(x_vals,y_approx,label = 'approx')
plt.show()
