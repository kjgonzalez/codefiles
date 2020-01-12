'''
use scikit-learn library to create a simple neural network. train it on iris
    dataset, see what performance is like.

KJG200112: will also use sklearn's version of iris dataset
KJG200112: to be as similar as possible to self-made nn, use:
* L2 error
* LR (learning rate) = 0.1
* maxiter (nepochs) = 1000
* architecture: 4-4-3 (tuple as: (4,)  )
* activation = sigmoid ('logistic')
* solver = 'sgd'
* !!!: not sure what 'alpha' is in MLPClassifier
* shuffle = False
*

'''

import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn import datasets
def npshuffle(nparr):
    # enable random shuffling of array without being in-place
    npa2=np.copy(nparr)
    np.random.shuffle(npa2)
    return npa2

np.random.seed(0)

sknn = MLPClassifier(hidden_layer_sizes=(4, ),
    activation='logistic', # changed
    solver='sgd', # changed
    batch_size='auto',
    learning_rate='constant',
    learning_rate_init=0.1,
    max_iter=1000, # changed (nepochs)
    shuffle=False, # changed
    nesterovs_momentum=True, # KJG200112: not sure if this should be False
    alpha=0.0001, # KJG200112: not sure what this corresponds to
    momentum=0.9, # KJG200112: not sure what this corresponds to
    )

iris = datasets.load_iris()

ds = iris['data']
labels = iris['target']

# randomly reorder all values in dataset for splitting into train/test
mask_shuffle = npshuffle(np.arange(len(ds)))
ds=ds[mask_shuffle]
labels=labels[mask_shuffle]



print(labels)






# eof
