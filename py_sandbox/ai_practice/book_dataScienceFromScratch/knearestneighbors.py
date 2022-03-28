'''
datecreated: 191002
objective: make own version of k-nearest neighbors (knn) classifier, from pg 169
    in book, using iris dataset

'''

import numpy as np
import matplotlib.pyplot as plt
from klib import listContents
# load dataset
dat=[]
fpath = '../../lib/data/iris.csv'
for irow in open(fpath):
    irow2=irow.strip().split(',')
    iline=[]
    iline.append(float(irow2[0]))
    iline.append(float(irow2[1]))
    iline.append(float(irow2[2]))
    iline.append(float(irow2[3]))
    iline.append(irow2[4].split('-')[-1]) # class name, without "Iris-"
    dat.append(iline)
dat=np.array(dat,dtype=object)
# data is loaded, now need to scramble rows and split
np.random.shuffle(dat)
ntotal=len(dat)
ntrain=int(0.7*ntotal)
ntest=ntotal-ntrain

ds_train=dat[:ntrain]
ds_test =dat[ntrain:]

# want: k-nearest neighbors classifier. need a distance metric.

class K_NearestNeighbor:
    def __init__(self,train_dataset,k):
        self.k=k
        from klib import listContents
        self.lc=listContents
        self.ds_train=train_dataset
    def dist(self,a,b):
        ''' given vectors a and b, return 2-norm '''
        return np.linalg.norm(np.array(a)-np.array(b)) # convert to np if not already

    def sort_closest(self,x,vectors):
        ''' given a specific vector and a list of other vectors, list other vectors
            by nearness (closest to farthest)
        '''
        order=np.argsort([self.dist(x,ivect) for ivect in vectors]) # get sorting order
        return order,vectors[order]

    def majority_vote(self,arr):
        ''' count most occuring value in list, try again if have a tie
        1. get list count
        2. check if max occurs more than once (if so, try again)
        3. return class of max
        '''
        counters=self.lc(arr,True)
        maxcount=np.max(counters[:,1])
        numOccur=len([1 for i in counters[:,1] if(maxcount==i)])
        if(numOccur==1):
            return counters[np.argmax(counters[:,1]),0]
        else:
            return self.majority_vote(arr[:-1])
    def eval_one(self,item):
        ord,vect=self.sort_closest(item[:-1],self.ds_train[:,:-1])
        neighbors=self.ds_train[ord][:self.k]
        estimate=self.majority_vote(neighbors[:,-1])
        return estimate
    def eval_set(self,test_dataset,show=False):
        ncorrect=0
        for item in test_dataset:
            ord,vect=self.sort_closest(item[:-1],self.ds_train[:,:-1])
            neighbors=self.ds_train[ord][:self.k]
            estimate=self.majority_vote(neighbors[:,-1])
            if(show):
                print('===================')
                print(item[-1],':',estimate)
            if(estimate==item[-1]):
                if(show):
                    print('correct')
                ncorrect+=1
            else:
                if(show):
                    print('wrong')
        return ncorrect,len(test_dataset)

knn = K_NearestNeighbor(ds_train,5) # have wrapped everything into a nice class


print('step 1, pick a random test item:')
item=ds_test[4]
print(item)
print('step 2, compare to all known data, choose k-nearest (5)')
ord,vect = knn.sort_closest(item[:-1],ds_train[:,:-1])
neighbors=ds_train[ord][:knn.k]
print(neighbors)
print('step 3, get majority vote of closest class')
estimate=knn.majority_vote(neighbors[:,-1])
print(estimate)
print('all in one step:',knn.eval_one(item))



print()
print('can do this for all test values, and get a score')
res=knn.eval_set(ds_test,False) # evaluate set, don't show all output

print('results: {}/{}, {}'.format(res[0],res[1],round(res[0]/res[1],2) ))
# eof
