'''
create a confusion matrix given some randomly generated data

NOTES:
* each row represents a class prediction
* each column represents a class ground truth
* sources:
    - https://machinelearningmastery.com/confusion-matrix-machine-learning/
    - confusion matrix, ElementsofStatisticalLearning,p301
    - https://en.wikipedia.org/wiki/Confusion_matrix

'''

import numpy as np
from sklearn.metrics import confusion_matrix as cm
np.random.seed(0)

def cm2(ypred,ytrue,nCls=None):
    ''' self-made confusion matrix calculation '''
    if(nCls==None):
        nCls=ytrue.max()+1
    arr=np.zeros((nCls,nCls))
    for i in range(len(ytrue)):
        arr[ypred[i],ytrue[i]]+=1
    return arr.astype(int)

# will use 3 classes
yp = np.random.randint(3,size=10) # create artificial predictions
yt = np.random.randint(3,size=10) # create artificial ground truth

print('prediction: ',yp)
print('groundtruth:',yt)
print()
print('results:')
print(cm(yt,yp))
print('\nself-made comparison:')
print(cm2(yt,yp,3))
