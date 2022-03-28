'''
date: 191113
objective: use neural network to identify flowers in iris dataset based on 4
    parameters (sepalL,sepalW,petalL,petalW) to identify species

general steps:
1. data loading / data prep - done
2. training                 - done
3. testing for accuracy     - done


NOTES:
* what if scale from 0.5-8.0 instead of 0-10?
* KJG191118: several combinations achieve 0.933 accuracy, including:
    - [4,4,3] @ 1000 epochs
    - [4,1000,3] @ 4000 epochs
    - [4,3,3] @ 1000
* there are 150 samples, so will make a 20% datasplit (30 test samples)
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
from klib import data as da
import argparse, time
import os, sys
sys.path.append(os.path.abspath('../book_OwnNN'))
from knet_nn import NeuralNetwork

def npshuffle(nparr):
    # enable random shuffling of array without being in-place
    npa2=np.copy(nparr)
    np.random.shuffle(npa2)
    return npa2

if(__name__=='__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--random',default=False,action='store_true',help='Enable randomness')
    p.add_argument('--epochs',default=1000,type=int,help='number of epochs to train')
    p.add_argument('--lr',type=float,default=0.1,help='Learning rate')
    p.add_argument('--layers',type=str,default='4-4-3',help='nn layer composition')
    # ideas: n epochs? split size?
    args=p.parse_args()

    if(not args.random):
        np.random.seed(0) # for now, control randomness seed
        print('seed controlled')
    nepochs = args.epochs

    layers=[int(i) for i in args.layers.split('-')]
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

    # TRAINING PHASE ===========================================================
    print('initializing network...')
    LR=0.1 # this value is arbitrary, remember
    nn=NeuralNetwork(layers,LR)
    print('nepochs:',nepochs,'|  layers:',layers)
    # presumably, training would happen here
    nn.train_full(ds_train,nepochs)

    # TESTING PHASE ============================================================
    scorecard=[]
    ypred=[]
    ytrue=[]
    for idat in ds_test:
        answer=np.argmax(idat[1])
        pred=np.argmax(nn.query(idat[0]))
        ytrue.append(answer)
        ypred.append(pred)
        # print(answer,'|',pred)
        scorecard+=[1] if(answer==pred) else [0]
    # print(scorecard)
    print('accuracy:',sum(scorecard)/len(scorecard))

    # KJG200112: at this point, going to use a bit of scikit for metrics
    from sklearn.metrics import confusion_matrix as cm
    CM = cm(ytrue,ypred) # confusion matrix
    print('results of confusion matrix:\n',CM)
# eof
