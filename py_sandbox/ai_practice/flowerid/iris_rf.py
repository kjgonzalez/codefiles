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
* bootstrapping: randomly selecting samples of a dataset, including multiples of a single one
* bagging: "bootstrap aggregation"
* KJG191217: main question is HOW EXACTLY does a non-optimal tree for RF get
    made? will refer to CART algorithm and use Elements of Statistical Learning
    book
* KJG191217: select m=sqrt(n) variables out of the n available at each step
* KJG191217: "grow tree until minimum node size 'n_min' is reached"... this
    simply means a maximum number of allowable nodes, based on pg 308: "The
    preferred strategy is to grow a large tree T0, stopping the splitting
    process only when some minimum node size (say 5) is reached. Then this
    large tree is pruned using cost-complexity pruning, which we now describe."

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
done | make custom counting function, based on number of classes given
done | create decision node with children
done | make tree node with all functions:
done | tree=DecisionTree(dict_format,nclasses)
done | tree.train(data) # take output from training one node, give it to children, etc
done | tree.query(idat) # if result is integer, go to node. if list, give result
done | create a single decision tree automatically (optimal)
done | bootstrap a dataset
done | create a single decision tree automatically (randomized)
done | create a random forest
done | make current rf implementation compatible with how iris data is loaded

for partitioning help, want a function that:
    0. given a dataset in matrix form
    1. looks at each parameter
    2. determines if binary, discrete, or continuous
    3. check entropy across all parameters / thresholds
    4. print results (or return best option)

'''

dat=[ # taken from DataScienceFromScratch, p221
#Lv La Tw Ph dw
[2, 0, 0, 0, 0], # parameters: level / language / tweets / has phd / did well
[2, 0, 0, 1, 0], # 0/1/2 = junior / mid / senior
[1, 1, 0, 0, 1], # 0/1/2 = java / python / R
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

import numpy as np
import argparse, time
from klib import data as da

# KJG200112: at this point, going to use a bit of scikit for metrics
from sklearn.metrics import confusion_matrix as cm

dat=np.array(dat,dtype=object) # using this type keeps ints as ints
# will now modify data to match how iris dataset is loaded, to see if the decision tree behaves properly

def npshuffle(nparr):
    # enable random shuffling of array without being in-place
    npa2=np.copy(nparr)
    np.random.shuffle(npa2)
    return npa2

def convertToDS(data):
    ''' take an input array with ians at final column and convert to local convention '''
    ds = []
    for irow in data:
        idat=irow[:-1]
        ians=np.zeros(2)+0.01
        ians[irow[-1]]=0.99
        ds.append([idat,ians])
    return ds
ds = convertToDS(dat)

def findthresholds(data):
    ''' find thresholds, and assume that data is a vector '''
    temp=data[np.argsort(data)]
    inds=np.where(temp[1:]-temp[:-1])[0]
    threshs=[temp[i:i+2].mean() for i in inds]
    return threshs

def getOptions(data,nclasses=2,desmetric=0,allmetrics=False,rounding=5):
    ''' Given an input array (assume last parameter is ground truth), determine
        type of parameter, check entropy for each combination, and return
        results.
    '''
    assert data.dtype =='O',"Dataset not loaded as dtype=object, param types might be ambiguous"
    nparams = len(data[0])-1
    arr=[]
    for iparam in range(nparams):
        # for now, will not worry about continuous data and massive number of splits there can be...
        threshs=findthresholds(data[:,iparam])
        for ithresh in threshs:
            inode = Node(iparam,thresh=ithresh,met=desmetric,nclasses=nclasses)
            if(allmetrics):
                # all metrics (yes,no,overall)
                score=[i.round(rounding) for i in inode.check(data)[2]]
                arr.append([int(iparam),ithresh,*score])
            else:
                # single metric (overall)
                score=round(inode.check(data)[2][2], rounding)
                arr.append([int(iparam),ithresh,score])
    return np.array(arr,dtype=object)

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

def gini(res0,res1=None,nclasses=2):
    ''' Get the gini impurity based on the output of an entire node (both
        binary results). can have any number of classes, which are
        determined when running. If only one result is given, then gini
        score of just that result is given (leaf?)
    '''
    count0=countClasses(res0[:,-1],nclasses)
    gini0=1-sum( (count0/count0.sum())**2 )
    if(type(res1)==type(None)):
        return gini0
    # otherwise, continue and return complete gini score
    count1=countClasses(res1[:,-1],nclasses)
    gini1=1-sum( (count1/count1.sum())**2 )
    sum01=len(res0)+len(res1)
    giniN = (len(res0)/sum01)*gini0+(len(res1)/sum01)*gini1
    return gini0,gini1,giniN

def entropy(res0,res1=None,nclasses=2):
    ''' Another way to find how "pure" a list of classes are. based on
        example from Data Science from Scratch
    '''
    s0=countClasses(res0[:,-1],nclasses)
    pcls0=s0/s0.sum()
    ent0=sum([-ip*np.log(ip) for ip in pcls0 if(ip>0)]) # per book, ignore '0'
    if(type(res1)==type(None)):
        return ent0
    # otherwise get weighted sum of combined entropy if have both results
    s1=countClasses(res1[:,-1],nclasses)
    pcls1=s1/s1.sum()
    ent1=sum([-ip*np.log(ip) for ip in pcls1 if(ip>0)]) # per book, ignore '0'
    entN = ( ent0*len(res0) + ent1*len(res1) )/( len(res0) + len(res1) )
    return ent0,ent1,entN

def getBootstrap(data):
    ''' return bootstrapped subset of data. two main rules: subset of
    data must be same length, and indices are allowed to be reused
    KJG191210: in the future, may return inds as well, to be able to
        track what indices are or aren't used.
    '''
    inds=np.random.choice(np.arange(len(data)),len(data))
    return data[inds]


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
        self.thresh = thresh # req if cond=thresh
        self._metric = met
        self.parent=None
        self.ncls = nclasses # will simply receive number of classes (such as from Tree object)
        self.yes_kid=None # index of child branch for "yes" (True) answer
        self.no_kid=None
        self.yes_ans=None # index of child branch for "no" (False) answer
        self.no_ans=None
        self.ID=None
        if(self._metric==self._METRICS[1]):
            self.metric=entropy
        else:
            self.metric=gini

    @property
    def children(self):
        return self.yes_kid,self.no_kid

    @property
    def info(self):
        ''' return quick summary about node '''
        L = 'ID param thresh parent yeskid nokid'.split(' ') # labels
        D = [self.ID,self.param,self.thresh,self.parent,self.yes_kid,self.no_kid] # data
        return {L[i]:D[i] for i in range(len(L))}

    def check(self,input,rounding=7):
        ''' get mask and obtain separated result arrays and metrices (3-values) '''
        mask=input[:,self.param]>self.thresh # bin/disc/cont all calculate mask same way
        res0=input[mask] # first check yes, then no...
        res1=input[np.logical_not(mask)]
        resMetric=self.metric(res0,res1,self.ncls)
        resMetric=[i.round(rounding) for i in resMetric]
        # get gini score
        return res0,res1,resMetric # KJG191210: won't return mask, working recursively

    def train(self,data,_nodes=None):
        ''' given a set of input data, decide what the outcome of a node would be
        variable _nodes only intended for use by DecisionTree class

        first, transform data from local convention to more usual array
        local convention: ds_train[0] = [input_array_normalized,ans_array]
            input_array = [0.01,0.43,0.99,...]
            ans_array   = [0.01,0.01,0.99] # 3-class example
        usual array:
            ds_train[0] = [*input_array,2]
        '''
        res0,res1=self.check(data)[:2]
        count0=countClasses(res0[:,-1],self.ncls)
        count1=countClasses(res1[:,-1],self.ncls)

        self.yes_ans= count0/count0.sum()
        self.no_ans = count1/count1.sum()

        if(type(_nodes)==type(None)):
            # no need to recursively train
            return res0,res1
        # otherwise, will then tell children to train as well
        if(self.yes_kid != None):
            _nodes[self.yes_kid].train(res0,_nodes)
        if(self.no_kid != None):
            _nodes[self.no_kid].train(res1,_nodes)

    def query(self,idat):
        ''' given a single sample, return what node thinks classification would be '''
        if(idat[self.param]>self.thresh):
            if(self.yes_kid==None):
                return self.yes_ans
            else:
                return self.yes_kid # should be an integer
        else:
            if(self.no_kid==None):
                return self.no_ans
            else:
                # should be an integer
                return self.no_kid

class DecisionTree:
    ''' a decision tree will hold the structure of each node (parents /
        children each has) and will contain all the nodes themselves as well.
        this object also traverses the "tree" to each final classification
    NOTE:
    * should have train function (take in data and save final scores at each leaf)
    * should have eval function (traverse tree)
    Typical Usage:
    tree = DecisionTree(struct,2) # struct=(premade dict of nodes)
    tree.train(ds) # "train" on a dataset
    tree.query(ds[0][0]) # test on sample data
    '''
    def __init__(self,numclasses,metric=0,maxnodes=100):
        self.node=dict()
        self.ncls = numclasses
        self.structure=None
        self.metric=metric # 0=gini, 1 = entropy
        self.maxnodes=maxnodes

    def generateManual(self,structure):
        ''' will create structure of tree based on given structure (dict) '''
        self.structure=structure
        # create reverse list to have parent listed for each node as well
        parent_list=[]
        parent_list.append([0,None])
        for ikey in structure.keys():
            for ival in structure[ikey][2]:
                if(ival!=None): parent_list.append([ival,ikey])
        parent_list=np.array(parent_list)
        parent_list=parent_list[np.argsort(parent_list[:,0])][:,1] # sort array, then keep only 2nd column and use by calling index
        for ind in structure.keys():
            param,thresh,kids=structure[ind]
            self.node[ind] = Node(param,thresh,met=self.metric,nclasses=self.ncls)
            # here, need to create connection to children
            self.node[ind].yes_kid=kids[0]
            self.node[ind].no_kid=kids[1]
            self.node[ind].parent=parent_list[ind]
            self.node[ind].ID=ind

    def addchild(self,parentNum,childNum,no_option):
        ''' connect parent and child nodes. if no_option=True, then will
            connect parent & "no" branch
        '''
        if(not no_option):
            # this is "yes" branch
            self.node[parentNum].yes_kid=childNum
        else:
            self.node[parentNum].no_kid =childNum
        self.node[childNum].parent=parentNum

    @property
    def nodeinfo(self):
        infos=[self.node[i].info for i in self.node.keys()]
        return infos

    def autogen(self,data,optimal=True):
        ''' Generate a tree given the data. can select if making an optimal tree
            or non-optimal as part of a random forest.
        '''
        # HERE, will transform data from local convention back to typical convention
        data2 = [list(data[i][0])+[np.argmax(data[i][1])] for i in range(len(data))]
        data2=np.array(data2,dtype=object)

        self.create_root(data2,optimal=optimal)
        # KJG191217: in order to balance which direction the tree grows in, will
        # randomly select left or right. workaround for depth-first instead of breadth-first
        if(np.random.randint(2)):
            self.tryAdd(0,data2,0,optimal=optimal)
            self.tryAdd(0,data2,1,optimal=optimal)
        else:
            self.tryAdd(0,data2,1,optimal=optimal)
            self.tryAdd(0,data2,0,optimal=optimal)
        # once everything is created, backfill the structure info
        struct=dict()
        for i in self.node.keys():
            temp=self.node[i]
            struct[i]=[temp.param,temp.thresh,[temp.yes_kid,temp.no_kid]]
        self.structure=struct

    def create_root(self,data,optimal=True):
        ''' for now, it might be easiest to separate the root and internal node
            creation subroutines.
        '''
        ops = getOptions(data,allmetrics=False,rounding=5,nclasses=self.ncls)
        # import ipdb; ipdb.set_trace()
        if(optimal):
            p,t,g = ops[np.argmin(ops[:,-1])] # return param,thresh, metric(s)

        else:
            ''' randomly select m variables to keep in list out of n choices '''
            # want: to return a "best split" from m variables out of the n available ones
            c=np.unique(ops[:,0])
            np.random.shuffle(c)
            d=c[:round(len(c)**0.5)] # choose m=sqrt(n) variables to create split
            mask=[i in d for i in ops[:,0]] # create filter
            ops2=ops[mask]
            p,t,g = ops2[np.argmin(ops2[:,-1])] # get best split from reduced choices
        self.node[0] = Node(p,t,nclasses=self.ncls)
        self.node[0].ID=0

    def tryAdd(self,r,data,direction,optimal=True):
        ''' recursive function for branches of root.
        INPUTS:
            * r = root / parent node index
            * data = data that goes into parent node
            * direction = which child of root node to attempt (0=yes,1=no)
        '''
        dat0,dat1,metric=self.node[r].check(data)
        dat=[dat0,dat1][direction]
        leaf_score=metric[direction]
        if(len(dat)<2):
            # not enough data to separate
            return None
        ops = getOptions(dat,allmetrics=False,rounding=5,nclasses=self.ncls)
        if(len(ops)<1):
            return None
        if(optimal):
            try:
                iparam,ithresh,iscore = ops[np.argmin(ops[:,-1])]
            except IndexError:
                import ipdb; ipdb.set_trace()
        else:
            # find sub-optimal split for random forest
            c=np.unique(ops[:,0])
            d=c[:round(len(c)**0.5)] # choose m=sqrt(n) variables to create split
            mask=[i in d for i in ops[:,0]] # create filter
            ops2=ops[mask]
            # XX for the moment, will leave this alone and not check if there are too few options
            iparam,ithresh,iscore = ops2[np.argmin(ops2[:,-1])] # get best split from reduced choices

        if(iscore>=leaf_score):
            return None # exit condition
        # otherwise, create new node
        nnode=len(self.node.keys())
        self.node[nnode]=Node(iparam,ithresh,nclasses=self.ncls)
        self.node[nnode].parent=r
        self.node[nnode].ID=nnode
        if(direction==0):
            self.node[r].yes_kid=nnode
        else: self.node[r].no_kid=nnode
        # now gotta deal with new node's potential children:

        # KJG191217: just like with create_root, randomly select direction
        if(np.random.randint(2)):
            if(len(self.node.keys())<self.maxnodes):
                self.tryAdd(nnode,dat,0)
            if(len(self.node.keys())<self.maxnodes):
                self.tryAdd(nnode,dat,1)
        else:
            if(len(self.node.keys())<self.maxnodes):
                self.tryAdd(nnode,dat,1)
            if(len(self.node.keys())<self.maxnodes):
                self.tryAdd(nnode,dat,0)

    def train(self,data):
        ''' will train recursively (depth first) by having any node that
        has children to tell its children to train on that data as well. this is
        done by the root node access to both the data as well as the dict of
        nodes, which all nodes will use as a guide during training. '''

        # HERE, will transform data from local convention back to typical convention
        data2 = [list(data[i][0])+[np.argmax(data[i][1])] for i in range(len(data))]
        data2=np.array(data2,dtype=object)

        self.node[0].train(data2,self.node)

    def query(self,idat):
        ''' traverse branches of tree based on given input data '''
        res=self.node[0].query(idat)
        # if a list, then has returned answer. if an integer, then has returned index to a child
        while(type(res)==int):
            res = self.node[res].query(idat)
        return res

class RandomForest:
    ''' create a random forest from a large number of RF-trees. use to classify
        some given data.
    '''
    def __init__(self,nclasses,metric=0,nTrees=101,maxnodes=5):
        self.nTrees=nTrees
        self.tree=[]
        self.nclasses=nclasses
        self.metric=metric
        self.maxnodes=maxnodes
    def genTrees(self,data):
        ''' for each tree:
            1. bootstrap the data
            2. create a non-optimal tree
            3.
        '''
        for i in range(self.nTrees):
            self.tree+=[DecisionTree(self.nclasses,metric=self.metric,maxnodes=self.maxnodes)]
            data_bootstrap=getBootstrap(data)
            self.tree[i].autogen(data_bootstrap,optimal=False)
            self.tree[i].train(data_bootstrap)
    def query(self,idat):
        res=[]
        for itree in self.tree:
            res.append(np.argmax(itree.query(idat)))
        res2=countClasses(res,self.nclasses)
        return res2/res2.sum()

# quick test to make sure things are working properly (including allmetrics)
def tests():
    assert (getOptions(dat)[:,-1]==getOptions(dat,allmetrics=True)[:,-1]).all() # getoptions not working
    # with sample dataset, as of KJG191210, this is what optimal, greedy decision tree looks like
    s=dict()
    s[0]=[2,0.5,[1,3]];         s[1]=[0,0.5,[None,2]]
    s[2]=[3,0.5,[None,None]];   s[3]=[0,1.5,[None,4]]
    s[4]=[0,0.5,[None,5]];      s[5]=[3,0.5,[None,None]]
    tree1=DecisionTree(2);       tree1.generateManual(s)
    tree1.train(ds)
    for idat in ds:
        assert np.argmax(tree1.query(idat[0]))==np.argmax(idat[1])
    tree2=DecisionTree(2)
    tree2.autogen(ds)
    tree2.train(ds)
    for idat in ds:
        assert np.argmax(tree2.query(idat[0]))==np.argmax(idat[1])
tests()

if(__name__=='__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--random',default=False,action='store_true',help='Enable randomness')
    p.add_argument('--epochs',default=1000,type=int,help='number of epochs to train')
    args=p.parse_args()

    if(not args.random):
        np.random.seed(0)
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

    # at this point, working with iris dataset. has 3 classes
    rf = RandomForest(nclasses=3,nTrees=60,maxnodes=9)
    rf.genTrees(ds_train)
    nNodes=[len(rf.tree[i].node.keys()) for i in range(len(rf.tree))]
    print('max and average number of nodes:',np.max(nNodes),np.mean(nNodes))
    scorecard=[]
    ytrue = []
    ypred = []
    for idat in ds_test:
        answer=np.argmax(idat[1]) # KJG191217: need to change this later
        pred = np.argmax(rf.query(idat[0]))
        ytrue.append(answer)
        ypred.append(pred)

        # print(pred,'|',answer)
        scorecard+=[1] if(answer==pred) else [0]
    print('performance:',sum(scorecard)/len(scorecard))

    CM = cm(ytrue,ypred) # confusion matrix
    print('results of confusion matrix:\n',CM)
    # eof
