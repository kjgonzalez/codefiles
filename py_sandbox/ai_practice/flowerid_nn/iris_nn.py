'''
date: 191113
objective: use neural network to identify flowers in iris dataset based on 4
    parameters (sepalL,sepalW,petalL,petalW) to identify species

general steps:
1. data loading / data prep
2. training
3. testing for accuracy

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

* could either rescale min/max values to be maximum, or attempt to future-proof
    against possible larger or smaller values. will do latter. min/max scale
    will simply be set to 0 and 10 cm

'''

# initialization / dataloading =================================================

import numpy as np
from klib import data as da

lookup = dict()
lookup[0]='setosa'
lookup['setosa'] = 0
lookup[1] = 'versicolor'
lookup['versicolor'] = 1
lookup[2] = 'virginica'
lookup['virginica'] = 2


raw=[i.strip().split(',') for i in open(da.irispath)]

for i in range(len(raw)):
    # replace each species with a number instead
    if('setosa') in raw[i][-1]:
        raw[i][-1]=0
    elif('versicolor') in raw[i][-1]:
        raw[i][-1]=1
    elif('virginica') in raw[i][-1]:
        raw[i][-1]=2
    else:
        raise Exception ("error, species not recognized")
raw2=np.array(raw,dtype=float)

# create input data (complete set at the moment)
# note: dataset has shape: dataset[i] = [input,answer]

# create ground truths
