'''
author: kris gonzalez
objective: bring together two custom modules to train and test on a set on a 
    well known set of data: the input/output of function y=x^3-x. in all 
    honesty, the most difficult part of this entire process has been to prep
    the data correctly, ensuring that the network is able to read from it.

CONCLUSIONS:
so, there are clearly ways to improve the results, but will not spend more 
    effort to actually implement them. some of the obvious changes that should
    be implemented:
    * use proper float notation for numbers
    * perhaps modify network so that it can take actual numbers?
    * better control the conversion / formatting of numbers
'''


# initializations ==============================================================
import numpy as np
import time
import os
from knet2 import NeuralNetwork
from data_prep import DatasetGenerator


# setup data to be manipulated =================================================
print('loading dataset...')
t0=time.time()
dsgen=DatasetGenerator(ntotal=20000,ntrain=19000)
print('loaded.',time.time()-t0)

dstrain=dsgen.get_training()
dstest=dsgen.get_testing()
rec=dstrain[0]

# setup network for training ===================================================
print('loading network... ')
nn=NeuralNetwork(24,200,24,0.01)
print('loaded.')

# next attempt, train a full epoch
print('training network... ')
t0=time.time()
#for idat in dstrain:
#    #itrain=list(idat[0])
#    #ians=list(idat[1])
#    nn.train_one(*idat)
nEpochs=4
nn.train_full(dstrain,nEpochs)

print('complete:',time.time()-t0)
print('training count:',len(dstrain))
print('num Epochs:',nEpochs)

# at this point, try querying the network to see if it knows the answer

# first, query single value
idat=dstest[0]
bf2d=dsgen.to_decimal
print('querying network')
print('true::',dsgen.get_test_dec(0))
truedec=dsgen.get_test_dec(0)[1]

ans=nn.query(idat[0])
#print('ans:',ans.T) # transpose so it's horizontal
ansdec=bf2d(ans)
print('estimated:',ansdec)
print('error:',(ansdec-truedec)/truedec)
print('complete')

# now query the entire test dataset, and get a score
# score = average([abspcterr(iest,itru) for ...])
bf2d=dsgen.to_decimal
scores=[]
t0=time.time()
print('starting scoring...')
for idat in dstest:
    ians=bf2d(nn.query(idat[0]))
    itru=bf2d(idat[1])
    if(itru!=0.0):
        ierr=abs((ians-itru)/itru)
    else:
        ierr=abs((ians-itru)/(itru+0.01))
    #print(itru,ians,ierr)
    scores.append(ierr)
print('scoring complete',time.time()-t0)
print('test set:',len(dstest))
print('average error:',np.mean(scores))

# eof

