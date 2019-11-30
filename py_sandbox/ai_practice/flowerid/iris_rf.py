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
done | get rid of condition argument, not needed
done | single-node decision tree, capable of train and eval
wait | make custom counting function, based on number of classes given
wait | make tree node, with given functionality:
        * tree=DecisionTree(dict_format,nclasses)
        * tree.train(data) # take output from training one node, give it to children, etc
        * tree.query(idat) # if result is integer, go to node. if list, give result
???? | be able auto-generate a single decision node
???? | perhaps create tool that helps split everything, like in book
???? | create a single node decision tree automatically
???? | create decision node with children
???? | create a random forest
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
dat=np.array(selfdat,dtype=object) # using this type keeps ints as ints
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

    # check each parameter's thresholds and report all combos
    # print('note: using entropy score')
    arr=[]
    desmetric=1 # 0=gini, 1 = entropy
    for iparam in range(nparams):
        # for now, will not worry about continuous data and massive number of splits there can be...
        threshs=findthresholds(data[:,iparam])
        for ithresh in threshs:
            inode = Node(iparam,thresh=ithresh,met=desmetric)
            score=round(inode.check(data)[2][0],3)
            arr.append([iparam,ithresh,score])
    return np.array(arr)

def countClasses(data,nclasses):
    ''' given some data and set of classes, count each class out
    ASSUMPTIONS:
        * classes range from 0 to n
        * data is a 1-D array of integers
    '''
    s=np.zeros(nclasses)
    for i in data:
        s[i]+=1
    return s

class Node:
    '''
    INITIALIZATION INPUTS:
    * param: parameter index (0,1,2,...). default=0
    * thresh: threshold to test condition default=0
    * metric: metric to identify best separation of values. 0=gini, 1=entropy.
        default=0
    '''
    _METRICS=[0,1] # gini, entropy
    def __init__(self,param=0,thresh=0.5,nclasses=2,met=0):
        assert met in self._METRICS,"invalid metric specified: "+met
        self.param=param # index, 0...n
        self._thresh = thresh # req if cond=thresh
        self._metric = met
        self.parent=None
        self.ncls = nclasses # will simply receive number of classes (such as from Tree object)
        self.yes_kid=None # index of child branch for "yes" (True) answer
        self.no_kid=None
        self.yes_ans=None # index of child branch for "no" (False) answer
        self.no_ans=None
        if(self._metric==self._METRICS[1]):
            self.metric=self.entropy
        else:
            self.metric=self.gini

    def check(self,input):
        ''' get mask and obtain separated result arrays and metrices (3-values) '''
        mask=input[:,self.param]>self._thresh # bin/disc/cont all calculate mask same way
        res0=input[mask] # first check yes, then no...
        res1=input[np.logical_not(mask)]
        resMetric=self.metric(res0,res1)
        # get gini score
        return res0,res1,resMetric

    def train(self,data):
        ''' given a set of input data, decide what the outcome of a node would be '''
        res0,res1=self.check(data)[:2]
        summary0=lc(res0[:,-1],True)
        summary0=summary0[np.argsort(summary0[:,0])] # have to ensure lc function is sorted properly
        count0=summary0[:,-1]
        summary1=lc(res1[:,-1],True)
        summary1=summary1[np.argsort(summary1[:,0])]
        count1=summary1[:,-1]

        self.yes_ans=count0/count0.sum()
        self.no_ans =count1/count1.sum()
        return res0,res1

    def query(self,idat):
        ''' given a single sample, return what node thinks classification would be '''
        if(idat[self.param]>self._thresh):
            if(self.yes_kid==None):
                return self.yes_ans
            else:
                return self.yes_kid # should be an integer
        else:
            if(self.no_kid==None):
                return self.no_ans
            else:
                return self.no_kid # should be an integer

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
        return entN, ent0, ent1

class DecisionTree:
    ''' a decision tree will hold the structure of each node (parents /
        children each has) and will contain all the nodes themselves as well.
        this object also traverses the "tree" to each final classification
    NOTE:
    * should have train function (take in data and save final scores at each leaf)
    * should have eval function (traverse tree)
    '''
    def __init__(self):
        pass

node=Node(0,1.5)
node.train(dat)
print(node.query(dat[0]))
print(node.query(dat[2]))
import ipdb; ipdb.set_trace()

exit()
# will instead create trees based on what children they have, not what parents
nodes = dict()
# nodes[index] = [param,thresh,[yes_child,no_child]]
nodes[0]=[0,0.5,[1,2]] # root node usually has children
nodes[1]=[2,0.5,[None,None]] # node either has 0, 1, or 2 children
nodes[2]=[0,1.5,[None,3]] #
nodes[3]=[3,0.5,[None,None]] # for now, will use double none to denote no children
# assumption: if child is None, then use metric to determine solution


tree=dict()
for i in nodes.keys():    #def __init__(self,param=0,cond=0,thresh=0.5,metric=0):
    tree[i]=Node(*nodes[i][:2])
    # tree[i].


# eof
