'''
date: 200318
objective: quick overview on how to use tqdm
'''

from tqdm import tqdm,trange
from time import sleep
import time
import numpy as np

# most basic usage: wrap around an iterator
print('working...')
for i in tqdm(range(10)):
    sleep(0.1)
print('done')

# the above can also be accomplished with trange, which replaces tqdm(range(...),...)
for i in trange(3,desc='trange'):
    sleep(0.01)

# apparently nested progress bars are normal
for i in tqdm(range(2),desc='iloop'):
    for j in tqdm(range(2),desc='jloop'):
        for k in tqdm(range(2),desc='kloop'):
            sleep(0.1)

# NOT recommended to use "print" while in a tqdm loop, breaks up the behavior
# instead, use tqdm.write
for i in trange(5):
    # print('in iter',i)
    tqdm.write('in iter {}'.format(i))
    sleep(0.2)
