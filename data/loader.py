'''
load dataset as needed

initial effort: create corrected dataset

NOTE:
  * try to only use stdlib, numpy, and maybe pandas modules

'''
import numpy as np
import os.path as osp

def load_iris():
    '''
    Return dictionary of info 
      data
      target
      labels

    '''
    path = osp.join(osp.dirname(__file__),'iris.csv')
    raw = np.array([i.strip().split(',') for i in open(path)],dtype=float)
    d = dict()
    d['data'] = raw[:,:4]
    d['target']=raw[:,4].astype(int)
    d['labels-target']='Iris-setosa Iris-versicolor Iris-virginica'.split(' ')
    d['labels-data']='len1 len2 len3 len4'.split(' ') # todo: fixme
    return d

if(__name__ == '__main__'):
    print(load_iris())
    

#eof

