'''
basic information on multiprocessing module

note: normally, data should not be passed between processes, but when need to, can use "Queue"
    class, also from multiprocessing module.
for more info overall: https://docs.python.org/3/library/multiprocessing.html

example output:
  done: 13500000
  done: 13500000
  done: 13500000
  done: 13500000
  no multi, duration: 11.655511140823364
  done: 13500000
  done: 13500000
  done: 13500000
  done: 13500000
  multi, duration: 3.259234666824341
'''

import multiprocessing as mp
import time
from math import ceil

def longop(maxval=300):
    # takes about 3 seconds to execute
    a = 0
    for i in range(maxval):
        for j in range(maxval):
            for k in range(maxval):
                a +=(i+j+k)%2
    print('done:',a)

def no_multi():
    for i in range(4):
        longop()

def multi():
    ncores = mp.cpu_count()
    nloops = ceil(4/ncores)

    for iloop in range(nloops): # avoid creating more processes than cores, saturating computation
        procs = []
        for icore in range(ncores):
            ip = mp.Process(target=longop)
            ip.start()
            procs.append(ip)
        for iproc in procs:
            iproc.join()


if(__name__ == '__main__'):
    t0 = time.time()
    no_multi()
    print('no multi, duration:',time.time()-t0)

    t0=time.time()
    multi()
    print('multi, duration:',time.time()-t0)


# eof

