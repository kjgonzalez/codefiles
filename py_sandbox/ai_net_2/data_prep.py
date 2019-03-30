'''
author: Kris Gonzalez
objective: this module to be used for preparing data that is received by 
    network. Overall objective is to create a basic, simple network to predict 
    the value of x^3-x between -4 and 4. will keep using self-made network, but
    would like to move to pytorch soon / at some point.

ASSUMPTIONS: 
    * working to predict function y=x**3-x, given values between -4 and 4
    * network will take in float value that has been converted to bin array
'''
import numpy as np
from klib import scale, pad

def dec2bin(val):
    ''' Take decimal value and return custom binary array of value between -64 
        and 64. 
    '''
    assert val<=64.0 and val>=-64.0, "value out of range:"+str(val)
    arr=[]
    # pos/negative
    if(val<0):
        arr.append(1)
    else:
        arr.append(0)
    # magnitude of value
    val2=abs(int(round(val*100000,0)))
    val3=pad(bin(val2)[2:],17,'0')
    arr+=[int(i) for i in val3]
    return arr

def bin2dec(bin_arr):
    ''' Take custom binary number array form and convert to decimal number '''
    arr=bin_arr.copy()
    if(arr[0]==0):
        sign=1
    else:
        sign=-1
    arr.reverse()
    val=sum([ival*2**i for i,ival in enumerate(arr[:-1])])
    return val*sign/100000.0

def threshold(arr,thresh=0.5):
    ''' Take in an array of values between [0,1] and set to either 0 or 1, 
        depending on if larger than threshold value. 
    INPUT:
        * arr: array of float values [0,1]
        * thresh: constant between [0,1], default=0.5
    OUTPUT:
        * arr2: array of integer values [0,1]
    '''
    return [0 if(ival<thresh) else 1 for ival in arr]

def dec2bin_arr(arr):
    ''' convert entire decimal array to binary arrays '''
    return [[dec2bin(i[0]),dec2bin(i[1])] for i in arr]

def bin2dec_arr(arr):
    ''' convert entire array of binary arrays to numpy decimal array '''
    return np.array([[bin2dec(i[0]),bin2dec(i[1])] for i in arr])

class DatasetGenerator:
    ''' class that can auto-generate train and test datasets, already in scaled 
    binary array form. when initialized, dataset is created. can then give the 
    train and test datasets as needed.
    '''
    def __init__(self):
        ntotal=5
        ntrain=3
        idx=np.arange(ntotal)
        np.random.shuffle(idx) # note: shuffles in-place 
        set_train_idx=idx[:ntrain]
        set_test_idx =idx[ntrain:]
        # at this point, have created list of train/test indices
        
        x=np.linspace(-4,4,ntotal) # by design, dataset range is [-4,4]
        y=x**3-x
        ds_total=np.column_stack((x,y)) # [Nx2] set of inputs/answers
        self.idx_train=set_train_idx
        self.idx_test =set_test_idx
        self.ds_total_orig=ds_total
    def get_training(self):
        ''' 
        Return preprocessed training dataset. dataset must have only 
            training values from total dataset, converted to binary array, and 
            rescaled. refer to array as such: ds_train[INDEX][INPUT,OUTPUT]  
        '''
        pass

if(__name__=='__main__'):
    # show example of above functions
    a=-np.pi
    print('orig:',a)
    b=dec2bin(a)
    print('bin :',b)
    c=bin2dec(b)
    print('dec2:',c)
    d=scale(b)
    print('scaled:',d)
    e=threshold(d)
    print('descaled:',e)


    # ntotal=10000
    # ntrain= 8500
    ntotal=5 # debugging
    ntrain=3

    idx=np.arange(ntotal)
    np.random.shuffle(idx) # note: shuffles in-place 
    set_train_idx=idx[:ntrain]
    set_test_idx =idx[ntrain:]

    x=np.linspace(-4,4,ntotal)
    y=x*x*x-x
    ds_total=np.column_stack((x,y)) # [Nx2] set of inputs/answers
    ds_train=ds_total[set_train_idx,:]
    ds_test =ds_total[set_test_idx, :]
    
    print('original:\n',ds_total)

    dsTotal=dec2bin_arr(ds_total)
    print('converted:\n',dsTotal[0])

    dsTot2=[[scale(i[0],(0,1)),scale(i[1],(0,1))] for i in dsTotal]
    #dsTot2=[]
    #for i in dsTotal:
    #    print('first:',i[0])
    #    print('second:',i[1])
    #    print('1-s:',scale(i[0],xlim=(0,1)))
    ## forloop
    #exit()
    print('scaled:\n',dsTot2[0])

    dsTot3=[[threshold(i[0]),threshold(i[1])] for i in dsTot2]
    print('descaled:\n',dsTot3[0])

    #dsrec=[[bin2dec(i[0]),bin2dec(i[1])] for i in dsTotal]
    dsrec=bin2dec_arr(dsTot3)
    print('recovered:\n',dsrec)

''' 
so, to recap: dataset is generated ([x,y]), then converted to binary arrays,
    then scaled. it is then split into train / test and put into network, and 
    the given result is then thresholded (descaled) and converted (recovered) 
    back into decimal form.
'''



# eof

