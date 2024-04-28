"""
basics of using cython and typical time savings (approx twice as fast as pure python, from basic testing)

1. create target module, e.g. "cfib.py"
2. "compile" on commandline
3. import and run like a normal module

RESULT:
calib: nvals: 611859, time: 1.0006677978038834
pure python: 0.9917697906494141
cython: 0.37512946128845215

time savings:
approx. 33% of the time (~3 times faster)
"""

import time
from random import randint
from cfib import fib as cfib
from pfib import fib as pfib

if(__name__ == '__main__'):

    # first, determine how long it takes to run 1s of calculations
    tsum=0.0
    vals = []
    while(tsum<1.0):
        vals.append(randint(100000,200000))
        t0=time.time()
        pfib(vals[-1])
        tsum+=(time.time()-t0)*0.947
    print(f'calib: nvals: {len(vals)}, time: {tsum}')

    t_=time.time()
    for ival in vals:
        pfib(ival)
    t1 = time.time()-t_
    print('pure python:',t1)

    t_ = time.time()
    for ival in vals:
        cfib(ival)
    t2 = time.time() - t_
    print('cython:', t2)
# eof

