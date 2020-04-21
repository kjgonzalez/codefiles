'''
date: 200318
objective: quick overview on how to use tqdm
'''

from tqdm import tqdm as _tqdm,trange as _trange
from time import sleep

# recommended changes to tqdm behavior for compatability in pycharm
tprint = _tqdm.write
def tqdm(*args,**kwargs):
    kwargs['ascii']=True
    return _tqdm(*args,**kwargs)

def trange(*args,**kwargs):
    kwargs['ascii']=True
    return _trange(*args,**kwargs)


# try nested bars again
for i in trange(3,desc='recfile'):
    for j in trange(3,desc='detections',leave=False):
        sleep(2)

# most basic usage: wrap around an iterator
print('working...')
list()
for i in tqdm(range(10)):
    sleep(0.1)
print('done')


# the above can also be accomplished with trange, which replaces tqdm(range(...),...)
for i in trange(3,desc='trange'):
    sleep(0.01)
print()


# apparently nested progress bars are normal
for i in tqdm(range(3),desc='iloop'):
    for j in tqdm(range(3),desc='jloop'):
        for k in tqdm(range(3),desc='kloop',leave=False):
            sleep(0.25)
print()

# NOT recommended to use "print" while in a tqdm loop, breaks up the behavior
# instead, use tqdm.write
for i in trange(5):
    # print('in iter',i)
    tprint('in iter {}'.format(i))
    sleep(0.2)

