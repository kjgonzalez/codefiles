'''
datecreated: 191123
objective: use random forest classifier to ID flowers in iris dataset based on 4
    parameters. for more information see iris_nn.py.

NOTES:
* there's a lot of non-matrix operations to do, so will need to break things
    down in pieces
* seems like some use ordered dicts to generate random forests
* realized that binary data is a subset of discrete data, and discrete is a
    subset of continuous data, and have unified mask function

General Steps:
1. create simple, small binary dataset (e.g. heart disease from src)
2. create data boostrappig function / bagging function
3. create gini impurity calculator (generalized both for leaves and nodes)
4. create continuous data node?
4. generate a randomized decision tree?
5. generate random forest?
6. evaluate on a random forest?


Current Goals
STAT | DESCRIPTION
--------------------------------------------------
done | be able to get gini / entropy score for a given set of data / parameter
done | create node for binary data
done | create node for continuous data
done | create node for discrete data?
done | unify masking function for binary, discrete, and continuous data
done | create a single decision node
done | automatically determine best node to add (function)
???? | be able auto-generate a single decision node
???? | perhaps create tool that helps split everything, like in book
???? | create a single node decision tree automatically
???? | create decision node with children
???? | create a random forest
???? | ??
???? | ??
???? | ??
???? | ??

want to create a tree based on an format, such as:
treedef=dict()
treedef[0]=[[props],[children]] # root node
treedef[1]=[[props],[children]]


for partitioning help, want a function that:
    0. given a dataset in matrix form
    1. looks at each parameter
    2. determines if binary, discrete, or continuous
    3. check entropy across all parameters / thresholds
    4. print results (or return best option)



'''

selfdat=[ # taken from DataScienceFromScratch, p221
#Lv La Tw Ph dw
[2, 0, 0, 0, 0], # parameters: level / language / tweets / has phd / did well
[2, 0, 0, 1, 0], # 0/1/2 = junior / mid / senior
[1, 1, 0, 0, 1], # 0/1/2 = java / python / r
[0, 1, 0, 0, 1], # 0/1 = False / True
[0, 2, 1, 0, 1],
[0, 2, 1, 1, 0],
[1, 2, 1, 1, 1],
[2, 1, 0, 0, 0],
[2, 2, 1, 0, 1],
[0, 1, 1, 0, 1],
[2, 1, 1, 1, 1],
[1, 1, 0, 1, 1],
[1, 0, 1, 0, 1],
[0, 1, 0, 1, 0]
]

# first, work on getting a decision tree to work (with a single node)
import numpy as np
from klib import data as da
from klib import listContents as lc
dat=np.array(selfdat)
findsplit(dat)
exit()
class Node:
    _CONDS='bin disc cont multi'.split(' ') # binary, continuous, discrete / ranked data
    _METRICS='gini entropy'.split(' ')
    def __init__(self,param=0,cond='bin',thresh=0.5,metric='gini'):
        assert cond in self._CONDS,"invalid condition specified: "+cond
        assert metric in self._METRICS,"invalid condition specified: "+metric
        if(cond=='bin'):
            assert thresh==0.5,"Error, threshold specified when using binary classification"
        self.param=param # index, 0...n
        self.cond = cond # 0=binary, 1=threshold
        self._thresh = thresh # req if cond=thresh
        self.parent=None
        self.kids=[] # don't want to spell "children" out, or shorten it
        if(metric=='entropy'):
            self.metric=self.entropy
        else:
            self.metric=self.gini

    def getmask(self,input):
        ''' based on condition to check, get mask '''
        if(self.cond in self._CONDS[:3]): # using binary, discrete, or continuous
            return input[:,self.param]>self._thresh
        elif(self.cond==self._CONDS[3]):
            raise Exception('multichoice condition not implemented yet')
        else:
            raise Exception('invalid condition being used')

    def eval(self,input):
        ''' get mask and obtain separated result arrays and metrices (3-values) '''
        mask=self.getmask(input)
        res0=input[np.logical_not(mask)]
        res1=input[mask]
        resMetric=self.metric(res0,res1)
        # get gini score
        return res0,res1,resMetric

    def gini(self,res0,res1=None):
        ''' Get the gini impurity based on the output of an entire node (both
            binary results). can have any number of classes, which are
            determined when running. If only one result is given, then gini
            score of just that result is given (leaf?)
        '''
        summary0=lc(res0[:,-1],True) # get summary of classes in results
        nclasses = len(summary0)
        gini0=1-sum([(summary0[i,-1]/len(res0))**2 for i in range(nclasses)])
        if(type(res1)==type(None)):
            return gini0
        # otherwise, continue and return complete gini score
        summary1=lc(res1[:,-1],True) # get summary of classes in results
        nclasses = len(summary1)
        gini1=1-sum([(summary1[i,-1]/len(res1))**2 for i in range(nclasses)])
        s01=len(res0)+len(res1)
        giniN = (len(res0)/s01)*gini0+(len(res1)/s01)*gini1
        print('calculating gini')
        return giniN,gini0,gini1

    def entropy(self,res0,res1=None):
        ''' Another way to find how "pure" a list of classes are. based on
            example from Data Science from Scratch
        '''
        summary0=lc(res0[:,-1],True) # get summary of classes in results
        # get class probabilities
        pcls0=summary0[:,1]/summary0[:,1].sum()
        ent0=sum([-ip*np.log(ip) for ip in pcls0 if(ip>0)]) # per book, ignore '0'
        if(type(res1)==type(None)):
            return ent0
        # otherwise get weighted sum of combined entropy if have both results
        summary1=lc(res1[:,-1],True) # get summary of classes in results
        # get class probabilities
        pcls1=summary1[:,1]/summary1[:,1].sum()
        ent1=sum([-ip*np.log(ip) for ip in pcls1 if(ip>0)]) # per book, ignore '0'
        entN = ( ent0*len(res0) + ent1*len(res1) )/( len(res0) + len(res1) )
        print('calculating entropy')
        return entN, ent0, ent1

def findthresholds(data):
    ''' find thresholds, and assume that data is a vector '''
    temp=data[np.argsort(data)]
    inds=np.where(temp[1:]-temp[:-1])[0]
    threshs=[temp[i:i+2].mean() for i in inds]
    return threshs

def findsplit(data):
    ''' Given an input array (assume last parameter is ground truth), determine
        type of parameter, check entropy for each combination, and return
        results.
    '''
    assert data.dtype =='O',"Dataset not loaded as dtype=object, param types might be ambiguous"
    nparams = len(data[0])-1
    print('nparams:',nparams)
    # determine nature of each parameter
    ptype=[] # 0=binary,1=discrete,2=continuous
    for i in range(nparams):
        if(type(data[:,i].max())==float):
            # non-integer: continuous data
            ptype.append(2)
        elif(data[:,i].max()>1):
            # int, larger than 1: discrete
            ptype.append(1)
        else:
            ptype.append(0)
    print('ptypes:',ptype)

    alias=dict()
    alias[0]='bin'
    alias[1]='disc'
    alias[2]='cont'
    # check each parameter's thresholds and report all combos
    print('note: using entropy score')
    arr=[]
    for iparam in range(nparams):
        if(ptype[iparam]==0):
            # just check 0.5 threshold and go on to next
            thresh=0.5
            inode = Node(iparam,alias[ptype[iparam]],thresh=thresh,metric='entropy')
            score=round(inode.eval(data)[2][0],3)
            arr.append([iparam,thresh,score])
            # print('p:{} | t:{} | s:{}'.format(iparam,thresh,score))
        elif(ptype[iparam]==1):
            # need to determine thresholds
            threshs=findthresholds(data[:,iparam])
            for ithresh in threshs:
                inode = Node(iparam,alias[ptype[iparam]],thresh=ithresh,metric='entropy')
                score=round(inode.eval(data)[2][0],3)
                arr.append([iparam,ithresh,score])
                # print('p:{} | t:{} | s:{}'.format(iparam,ithresh,score))
    print('results:')
    for irow in arr:print('p:{} | t:{} | s:{}'.format(*irow))
# need to create function that determines splits for a set of data

dat2=dat[dat[:,0]==0]


findsplit(dat2)
exit()

print('gini based metrics:')
a=Node(param=2) # binary data, gini
print('bin',a.eval(dat)[2])
b=Node(param=2,cond='disc')
print('dis',a.eval(dat)[2])
c=Node(param=2,cond='cont')
print('con',a.eval(dat)[2])




# eof
