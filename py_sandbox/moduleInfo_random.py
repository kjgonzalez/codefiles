'''
Author: Kris Gonzalez
DateCreated: 190214
Objective: showcase "random" module and basics of using it. there are some
    basic, but important abilities that this module has.
'''

import random
import numpy as np

x=list(range(10))
print('initial list:',x)

# randomly choosing a number of elements from a list:
# note: elements must be a sequence or set in python3
k=3
print('regular: choosing',k,'random elements from set:',random.sample(x,k))
print('numpy:   choosing',k,'random elements from set:',np.random.choice(np.array(x),k))

print(
'''NOTE: when dealing with a 2D array (or higher), need to actually use
    shuffling, because np.random.choice does not pick k unique random values,
    only k random values. example: ''')
x2=np.array(np.random.rand(5,3)*10,int)
print(x2)

print('sampling k rows from array:')


# randomly choosing a single element from a list:
print('random single choice:',random.choice(x))

# shuffle elements of array (need function to avoid in-place)
print('with random:')
x=list(range(10))
print('original:',x)
x2=x[:]
random.shuffle(x2)
print('shuffled:',x2)

print()
print('with numpy:')
print(
'''note: np.random.shuffle only shuffles along first axis of multi-dim array,
    and happens in-place''')
xnp=np.arange(10)
def npshuffle(nparr):
    npa2=np.copy(nparr)
    np.random.shuffle(npa2)
    return npa2
print('original:',xnp)
xnp2=npshuffle(xnp)
print('shuffled:', xnp2)
