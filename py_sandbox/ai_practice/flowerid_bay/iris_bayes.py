'''
datecreated: 191119
objective: use naive bayes classifier to ID flowers in iris dataset based on 4
    parameters. for more information see iris_nn.py. as a note, there are
    three main kinds of naive bayes (NB) classifiers (esp used in scikit-learn):
    - gaussian NB
    - binary (Bernoulli) NB
    - multinomial NB

General Steps:
1. dataloading                  - inProgress
2. class initialization         - waiting
3. querying / performance check - waiting

NOTES:
* The classifier below will be a gaussian naive bayes classifier (able to deal
    with continuous data)
* 150 samples, 20% data split (30 test samples)
* data in cm, params (4) are: sepL, sepW, petL, petW
* classes (3) are: setosa, versicolor, virginica (0,1,2)
'''

# INITIALIZATION ===============================================================

import numpy as np
from klib import data as da
import argparse, time, os, sys

def npshuffle(nparr):
    # enable random shuffling of array without being in-place
    npa2=np.copy(nparr)
    np.random.shuffle(npa2)
    return npa2


if(__name__=='__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--random',default=False,action='store_true',help='Enable randomness')
    args=p.parse_args()
    print('hello world')

    if(not args.random):
        np.random.seed(0) # for now, control randomness seed
        print('seed controlled')

    # DATALOADING ==============================================================
    print("loading data...")
    dataset=[]
    for irow in open(da.irispath):
        iraw = irow.strip().split(',') # 1x5 data
        dmin= 0.0# domain minimum
        dmax= 10.0# domain maximum
        idat = (0.98/(dmax-dmin))*(np.array(iraw[:-1],dtype=float)-dmin)+0.01 # 0-10 to 0.01-0.99
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

    ntrain = 120
    ds_train=dataset[:ntrain]
    ds_test =dataset[ntrain:]

# eof
