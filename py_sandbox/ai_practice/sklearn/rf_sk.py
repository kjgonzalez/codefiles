'''
use scikit-learn library to create a random forest classifier. train it on iris
    dataset, see what performance is like.

KJG200112: will also use sklearn's version of iris dataset
KJG200121: following example in documentation because of similarity

'''

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
from sklearn.metrics import confusion_matrix as cm
def npshuffle(nparr):
    # enable random shuffling of array without being in-place
    npa2=np.copy(nparr)
    np.random.shuffle(npa2)
    return npa2

np.random.seed(0)
print('seed controlled')

# load all data
iris = datasets.load_iris()
ds = iris['data']
labels = iris['target']
# randomly reorder all values in dataset for splitting into train/test
mask_shuffle = npshuffle(np.arange(len(ds)))
ntrain = 120
ds=ds[mask_shuffle]
labels=labels[mask_shuffle]
ds_train=ds[:ntrain]
ds_test=ds[ntrain:]
labels_train=labels[:ntrain]
labels_test=labels[ntrain:]

skrf = RandomForestClassifier(max_depth=2,random_state=0)
skrf.fit(ds_train,labels_train)


ypred = skrf.predict(ds_test)
ytrue = labels_test[:]

# as an example, show probabilities when predicting
print(skrf.predict_proba(ds_test[:10]).round(3))

# get some stats about results
ans = ypred==ytrue
print('accuracy:',ans.sum()/len(ans))

CM = cm(ytrue,ypred)
print('results of confusion matrix:\n',CM,sep='')

# eof
