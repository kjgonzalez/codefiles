'''
How to pickle data (any object). Note, if you want to use a forloop, must
    actually use a while loop that compares filesize to current byte location.
    Otherwise, need to use some kind of exception-based method.
exception-based forloop: https://stackoverflow.com/questions/18675863/load-data-from-python-pickle-file-in-a-loop
'''

import pickle # only works for python3. for py2, need to do other stuff
import numpy as np
import os

print('='*60)
print('example 1: pickle a single object')
a={letter:num for num,letter in enumerate(list('abcdef'))}
fname='delme.pkl'
with open(fname,'wb') as f:
    pickle.dump(a,f)

with open(fname,'rb') as f2:
    b=pickle.load(f2)

print('original:',a)
print('compare original and loaded:',a==b)
os.remove(fname)
print('file removed. done')
# ==============================================================================
print('='*60)
print('example 2: pickle multiple objects')
temp=[np.arange(i+1) for i in range(0,4)] # get multiple vectors to pickle
print('complete data:')
print(temp)
fname='example.pickle' # note, extension can pretty much be anything you want.
ftemp=open(fname,'wb')
for ivec in temp:
    print('dumping:',ivec)
    pickle.dump(ivec,ftemp)
ftemp.close()
print('done')
print('=','now, load file and display contents','='*10)

# next, read the file back in
ftemp=open(fname,'rb')
xx=[]
while ftemp.tell()<os.path.getsize('example.pickle'):
    xx.append(pickle.load(ftemp,encoding='bytes'))
    print('loaded: ',xx[-1])
ftemp.close()
print('complete data:')
print(xx)
os.remove(fname)
print('file removed. done')

# eof
