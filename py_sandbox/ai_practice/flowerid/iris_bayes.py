'''
datecreated: 191119
objective: use naive bayes classifier to ID flowers in iris dataset based on 4
    parameters. for more information see iris_nn.py. as a note, there are
    three main kinds of naive bayes (NB) classifiers (esp used in scikit-learn):
    - Gaussian NB
    - binary (Bernoulli) NB
    - multinomial NB

General Steps:
1. dataloading                  - done
2. class initialization         - done
3. querying / performance check - done

NOTES:
* The classifier below will be a gaussian naive bayes classifier (able to deal
    with continuous data)
* 150 samples, 20% data split (30 test samples)
* data in cm, params (4) are: sepL, sepW, petL, petW
* classes (3) are: setosa, versicolor, virginica (0,1,2)
* KJG191119: have noted that variance is calculated as population (n) and not
    sample (n-1), and may try the sample later if needed.
* KJG191119: have achieved performance of 0.933

'''

# INITIALIZATION ===============================================================

import numpy as np
from klib import data as da
import argparse, time, os, sys

# KJG200112: at this point, going to use a bit of scikit for metrics
from sklearn.metrics import confusion_matrix as cm

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
    def __init__(self,train_data):
        '''
        General Steps:
        1. get dataset - done
        2. identify how many parameters "i" there are - done
        3. identify how many classes "j" there are - done
        4. split dataset for each class, and get parameter means & variances - done
        5. for each class, each parameter, fill out avg and var arrays - done
        6. get P(iclass), and fill out pcl array - done
        '''

        # first, determine how many parameters & classes there are
        self.nprm = len(train_data[0][0])
        self.ncls = len(train_data[0][1])

        # get pcls ( P(iclass) ) for all classes & separate data per class
        self.pcls=[0]*self.ncls
        self.avg = np.zeros((4,3))
        self.var = np.zeros((4,3))
        clsarr=[[] for i in range(self.ncls)] # temporary arrays to generate per-class mean/variance
        for idat in train_data:
            # create temporary pcls sums
            loc=np.argmax(idat[1])
            self.pcls[loc]+=1
            clsarr[loc]+=[idat[0]]
        # get means / variances for each class (column by column)
        for iclass in range(self.ncls):
            temp=np.array(clsarr[iclass])
            self.avg[:,iclass] = temp.mean(0)
            self.var[:,iclass] = temp.var(0)
        # get P(iclass)
        self.pcls = np.array(self.pcls)/sum(self.pcls) # works fine

    def gpdf(self,x,mu,variance):
        ''' given a sample, mu, and variance, return gaussian probability
            density function.
        '''
        # quick check, make sure x is accepted as numpy array:
        xx=np.array(x)
        return (2*np.pi*variance)**(-1/2)*np.exp((xx-mu)**2 / (-2*variance))

    def query(self,inputs):
        ''' test network on a single input '''
        x=np.array(inputs)
        # create probability table P(x_i|c_j)
        p=np.zeros((self.nprm,self.ncls)) # P(x_i|c_j) (via gauss pdf)
        for iprm in range(self.nprm):
            for jcls in range(self.ncls):
                p[iprm,jcls]=self.gpdf(x[iprm],self.avg[iprm,jcls],self.var[iprm,jcls])
        # get probability products
        p_x=p.prod(0) # P(x|c_j)

        # get per-class prediction
        sum_p_x_cls=sum([p_x[jcls]*self.pcls[jcls] for jcls in range(self.ncls)])
        pvals=np.zeros(self.ncls)
        for iclass in range(self.ncls):
            pvals[iclass] = p_x[iclass]*self.pcls[iclass] / sum_p_x_cls
        return pvals

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

    # print('overall:')
    # print(ds_train)
    # TRAINING PHASE ===========================================================
    print('initializing network...')

    gnb=GaussianNaiveBayes(ds_train)
    # print('average:\n',gnb.avg.round(4))
    # print('variance:\n',gnb.var.round(6))
    # print('pcls:\n',gnb.pcls.round(4))

    # TESTING PHASE ============================================================
    # print('P | A')
    scorecard=[]
    ytrue = []
    ypred = []
    for idat in ds_test:
        answer=np.argmax(idat[1])
        pred=np.argmax(gnb.query(idat[0]))
        ytrue.append(answer)
        ypred.append(pred)

        # print(answer,'|',pred)
        scorecard+=[1] if(answer==pred) else [0]
    # print(scorecard)
    print('performance:',sum(scorecard)/len(scorecard))

    CM = cm(ytrue,ypred) # confusion matrix
    print('results of confusion matrix:\n',CM)
# eof
