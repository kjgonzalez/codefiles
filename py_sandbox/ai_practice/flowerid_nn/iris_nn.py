'''
date: 191113
objective: use neural network to identify flowers in iris dataset based on 4
    parameters (sepalL,sepalW,petalL,petalW) to identify species

general steps:
1. data loading / data prep - done
2. training                 - waiting
3. testing for accuracy     - waiting

NOTES:
* there are 150 samples, so will make a 20% datasplit (30 test samples)
* estimated architecture:
    - input layer: 4
    - hidden layer: 10/50/100 (?)
    - output layer: 3 (or 1 depending on style)
* min / max values (keeping rows in order):
    name | sepL | sepW | petL | petW
    min  | 4.3  | 2.0  | 1.0  | 0.1
    max  | 7.9  | 4.4  | 6.9  | 2.5
* by alphabetical order:
    setosa = 0
    versicolor = 1
    virginica = 2
* will simply min/max between 0/10cm instead of relative scaling

'''
# INITIALIZATION ===============================================================
import numpy as np
np.random.seed(0) # for now, control randomness seed
from klib import data as da
import argparse, time
import os, sys
sys.path.append(os.path.abspath('../../book_OwnNN'))
from knet_nn import NeuralNetwork

def npshuffle(nparr):
    # enable random shuffling of array without being in-place
    npa2=np.copy(nparr)
    np.random.shuffle(npa2)
    return npa2

# DATALOADING ==================================================================

print("loading data ...")
dataset=[]
for irow in open(da.irispath):
    iraw = irow.strip().split(',') # 1x5 data
    idat = (0.98/10)*(np.array(iraw[:-1],dtype=float))+0.01 # 0-10 to 0.01-0.99
    ival = iraw[-1]
    if('setosa' in ival): ival=0
    elif('versicolor' in ival): ival=1
    elif('virginica' in ival): ival=2
    else: raise Exception('error, species not recognized')
    ians = np.zeros(3)+0.01
    ians[ival] = 0.99
    dataset.append([idat,ians])
# at this point, have a 150x5 array of data
dataset=npshuffle(dataset) # shuffle data

print("data loaded")
ntrain = 120
ds_train=dataset[:ntrain]
ds_test =dataset[ntrain:]

print('training:')
for i in ds_train: print(i)
print('testing')
for i in ds_test: print(i)

# TRAINING PHASE ===============================================================
print('initializing network')
layers=[4,20,3]
LR=0.01 # this value is arbitrary, remember
nn=NeuralNetwork(layers,LR)

# presumably, training would happen here


# TESTING PHASE ================================================================
scorecard=[]
for idat in ds_test:
    answer=np.argmax(idat[1])
    pred=np.argmax(nn.query(idat[0]))
    print(answer,'|',pred)
    scorecard+=[1] if(answer==pred) else [0]
print(scorecard)
print('performance:',sum(scorecard)/len(scorecard))



if(__name__=='__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--random',default=False,action='store_true',help='Disable randomness control')
    # ideas: n epochs? split size?
    args=p.parse_args()
    print('done')





# eof
