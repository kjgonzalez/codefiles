'''
datecreated: 191119
objective: use naive bayes classifier to ID flowers in iris dataset based on 4
    parameters. for more information see iris_nn.py. as a note, there are
    three main kinds of naive bayes (NB) classifiers (esp used in scikit-learn):
    - gaussian NB
    - binary (Bernoulli) NB
    - multinomial NB

General Steps:
1. dataloading                  - done
2. class initialization         - inProgress
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

class GaussianNaiveBayes:
    ''' Gaussian Naive Bayes classifier. initially developed for use with iris
        dataset.

    In order to initialize this class, must have the dataset already prepared
        in the correct manner, similar to training for NeuralNetwork class:
        ds_train[i] = [data,answer] for each i in dataset
        data = array of m values, [0.01-0.99]
        answer = array of n values, [0.01 or 0.99], where
    '''
    def __init__(self,ds_train):
        '''
        General Steps:
        1. get dataset
        2. identify how many parameters "i" there are
        3. identify how many classes "j" there are
        4. split dataset for each class, and get parameter means & variances
        5. for each class, each parameter, fill out avg and var arrays
        6. get P(iclass), and fill out pcl array
        get dataset, separate for each class, get mean and variance, then place into appropriate locations
        '''
        pass

    def gpdf(self,x,mu,variance):
        ''' given a sample, mu, and variance, return gaussian probability
            density function
        '''
        pass

    @property
    def means(self):
        pass
        # return self.avg

    @property
    def variances(self):
        pass
        # return self.var

    def Pclass(self):
        pass
        # return self.pcl












if(__name__=='__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--random',default=False,action='store_true',help='Enable randomness')
    args=p.parse_args()

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

    print(ds_test)
# eof
