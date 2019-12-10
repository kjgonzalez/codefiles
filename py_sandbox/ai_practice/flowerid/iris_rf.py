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
* bagging: "bootstrap aggregation",
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
???? | create a single decision tree automatically (randomized)
???? | bootstrap a dataset
???? | create a random forest
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

# first, work on getting a decision tree to work (with a single node)
import numpy as np
from klib import data as da
from klib import listContents as lc
dat=np.array(selfdat,dtype=object) # using this type keeps ints as ints
# will now modify data to match how iris dataset is loaded, to see if the decision tree behaves properly

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

def getOptions(data,desmetric=0,allmetrics=False,rounding=5):
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
            inode = Node(iparam,thresh=ithresh,met=desmetric)
            if(allmetrics):
                # all metrics (yes,no,overall)
                score=[i.round(rounding) for i in inode.check(data)[2]]
                arr.append([int(iparam),ithresh,*score])
            else:
                # single metric (overall)
                score=round(inode.check(data)[2][2], rounding)
                arr.append([int(iparam),ithresh,score])
    return np.array(arr,dtype=object)

def best_split(data,desmetric=0,allmetrics=False,rounding=5):
    ''' in given data, return best option for splitting (p,t,metric) '''
    options = getOptions(data,allmetrics=allmetrics,rounding=rounding)
    return options[np.argmin(options[:,-1])] # return param,thresh, metric(s)

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

def maskmerge(mask1,mask2):
    ''' be able to use mask of standardized size across all nodes and be able to
    assume mask1 is the super-mask '''
    m3=[]
    j=0
    for i in range(len(mask1)):
        if(mask1[i]):
            m3.append(mask2[j])
            j+=1
        else:
            m3.append(mask1[i])
    return np.array(m3)

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

        self.yes_ans=count0/count0.sum()
        self.no_ans =count1/count1.sum()

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
                return self.no_kid # should be an integer

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
    def __init__(self,numclasses,metric=0):
        self.node=dict()
        self.ncls = numclasses
        self.structure=None
        self.metric=metric # 0=gini, 1 = entropy
        self.maxnodes=1000

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
            self.node[ind] = Node(param,thresh,self.ncls,met=self.metric)
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

        '''


    def train(self,data):
        ''' will train recursively (depth first) by having any node that
        has children to tell its children to train on that data as well. this is
        done by the root node access to both the data as well as the dict of
        nodes, which all nodes will use as a guide during training. '''
        # KJG191130: for now, won't use "local convention", takes too much effort to convert between
        # need to change data back to slightly more typical array
        # inp = []
        # for idat in data:
        #     inp.append( np.append( idat[0],np.argmax(idat[1]) ) )
        # inp=np.array(inp)

        self.node[0].train(data,self.node)

    def query(self,idat):
        ''' traverse branches of tree based on given input data '''
        res=self.node[0].query(idat)
        # if a list, then has returned answer. if an integer, then has returned index to a child
        while(type(res)==int):
            res = self.node[res].query(idat)
        return res

# quick test to make sure things are working properly (including allmetrics)
assert (getOptions(dat)[:,-1]==getOptions(dat,allmetrics=True)[:,-1]).all() # getoptions not working
assert getOptions(dat)[:,-1].min()==best_split(dat,allmetrics=True)[-1] # best_split not working
# with sample dataset, as of KJG191210, this is what optimal, greedy decision tree looks like
s=dict()
s[0]=[2,0.5,[1,3]];         s[1]=[0,0.5,[None,2]]
s[2]=[3,0.5,[None,None]];   s[3]=[0,1.5,[None,4]]
s[4]=[0,0.5,[None,5]];      s[5]=[3,0.5,[None,None]]
tree=DecisionTree(2);       tree.generateManual(s)
tree.train(dat)
for idat in dat:
    assert np.argmax(tree.query(idat[:-1]))==idat[-1]

if(__name__=='__main__'):

    # will instead create trees based on what children they have, not which parents
    # struct[index] = [param,thresh,[yes_child,no_child]]
    tree.autogen(dat)

    # eof
