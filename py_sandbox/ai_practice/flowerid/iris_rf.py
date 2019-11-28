'''
datecreated: 191123
objective: use random forest classifier to ID flowers in iris dataset based on 4
    parameters. for more information see iris_nn.py.

NOTES:
* there's a lot of non-matrix operations to do, so will need to break things
    down in pieces
* seems like some use ordered dicts to generate random forests
General Steps:
1. create simple, small binary dataset (e.g. heart disease from src)
2. create data boostrapping function / bagging function
3. create gini impurity calculator (generalized both for leaves and nodes)
4. create continuous data node?
4. generate a randomized decision tree?
5. generate random forest?
6. evaluate on a random forest?


Current Goals
Stat | Descrip
wait | create a random forest
wait | create a single decision tree automatically
wait | create a single decision node
wait | create decision node with child
wait | automatically determine best node to add
???? | ??
???? | ??
???? | ??
???? | ??
???? | ??
???? | ??


'''
# 0/1/2 = junior / mid / senior
# 0/1/2 = java / python / r
# 0/1 = False / True
# parameters: level / language / tweets / has phd / did well
selfdat=[ # taken from DataScienceFromScratch, p221
#Lv La Tw Ph dw
[2, 0, 0, 0, 0],
[2, 0, 0, 1, 0],
[1, 1, 0, 0, 1],
[0, 1, 0, 0, 1],
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

class Node:
    _CONDS='bin thresh'.split(' ')
    _METRICS='gini entropy'.split(' ')
    def __init__(self,param=0,cond='bin',thresh=0.5,metric='gini'):
        assert cond in self._CONDS,"invalid condition specified: "+cond
        assert metric in self._METRICS,"invalid condition specified: "+metric
        self.param=param # index, 0...n
        self.cond = cond # 0=binary, 1=threshold
        self._thresh = thresh # req if cond=thresh
        self.parent=None
        self.kids=[]
        if(metric='entropy'):
            self.metric=self.entropy
        else:
            self.metric=self.gini

    def getmask(self,input):
        ''' based on condition to check, get mask '''
        if(cond=='bin'):
            return input[:,self.param]==True # assume cond=0
        if(cond=='thresh'):
            return input[:,self.param]>self._thresh

    def eval(self,input):

        mask=input[:,self.param]==True # assume cond=0
        res0=input[np.logical_not(mask)]
        res1=input[mask]
        gini=self.gini(res0,res1)
        # get gini score
        return res0,res1,gini

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
        return giniN,gini0,gini1

    def entropy(self,res0,res1=None):
        ''' Another way to find how "pure" a list of classes are. based on
            example from Data Science from Scratch
        '''
        summary0=lc(res0[:-1],True) # get summary of classes in results
        # get class probabilities
        pcls0=summary0[:,1]/summary0[:,1].sum()
        ent0=sum([-ip*np.log(ip) for ip in pcls0 if(ip>0)]) # per book, ignore '0'
        if(type(res1)==type(None)):
            return ent0
        # otherwise get weighted sum of combined entropy if have both results
        summary1=lc(res1[:-1],True) # get summary of classes in results
        # get class probabilities
        pcls1=summary1[:,1]/summary1[:,1].sum()
        ent1=sum([-ip*np.log(ip) for ip in pcls1 if(ip>0)]) # per book, ignore '0'
        entN = ( ent0*len(res0) + ent1*len(res1) )/( len(res0) + len(res1) )
        return entN, ent0, ent1
# perhaps create a tool that helps us split everything

def getgini(data,p):
    temp=Node(param=p)
    return temp.eval(data)[2]

def getentropy(data,p):
    temp=Node(param=p)
    return temp.
import ipdb; ipdb.set_trace()

'''
want to create a tree somehow
perhaps based on an instruction

n0:[n1:[],n2]

treedef=dict()
treedef[0]=[[props],[children]] # root node
treedef[1]=[[props],[children]]



'''
dat=np.array([i.strip().split(',') for i in open('delme.csv')],dtype=int)

n=Node(param=0,cond='bin')
res=n.eval(dat)
print('gini:\n',res[2])

m=Node(param=0,cond='thresh',thresh=0.5)
res=m.eval(dat)
print('gini:\n',res[2])



# eof
