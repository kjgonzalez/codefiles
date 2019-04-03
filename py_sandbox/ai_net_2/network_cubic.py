'''
author: kris gonzalez
objective: bring together two custom modules to train and test on a set on a 
    well known set of data: the input/output of function y=x^3-x. in all 
    honesty, the most difficult part of this entire process has been to prep
    the data correctly, ensuring that the network is able to read from it.
'''


# initializations ==============================================================
import numpy as np
import time
import os
from knet2 import NeuralNetwork
from data_prep import DatasetGenerator


# setup data to be manipulated =================================================
dsgen=DatasetGenerator(ntotal=10000,ntrain=7000)
print(dir(dsgen))
dstrain=dsgen.get_training()
dstest=dsgen.get_testing()
rec=dstrain[0]
print('training set length:',len(dstrain))
print('first item example:',rec[0],dsgen.to_decimal(rec[0]))
print('verification:',dsgen.get_train_dec(0)[0])

# setup network for training ===================================================
nn=NeuralNetwork(24,200,24,0.01)
#print(dir(nn))

## first attempt, just train once.
#idat=dstrain[0]
#print(*idat)
#itrain=list(idat[0])
#ians=list(idat[1])
#nn.train_one(itrain,ians)

# next attempt, train a full epoch
t0=time.time()
for idat in dstrain:
    itrain=list(idat[0])
    ians=list(idat[1])
    nn.train_one(itrain,ians)

print('training complete:',time.time()-t0)
print('training count:',len(dstrain))

print('success')



# eof

