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
    val3=pad(bin(val2)[2:],23,'0')
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
    def __init__(self,ntotal=10000,ntrain=8500):
        ''' when object initialized, create dataset and train/test split '''
        idx=np.arange(ntotal)
        np.random.shuffle(idx) # note: shuffles in-place 
        set_train_idx=idx[:ntrain]
        set_test_idx =idx[ntrain:]
        
        x=np.linspace(-4,4,ntotal) # by design, dataset range is [-4,4]
        y=x*x*x-x
        ds_total=np.column_stack((x,y)) # [Nx2] set of inputs/answers
        
        dsTotal=dec2bin_arr(ds_total) # convert to binary

        # scale binary values to float range [0.01,0.99]
        dsTotal_bin2=[[list(scale(i[0],(0,1))),list(scale(i[1],(0,1)))] \
                for i in dsTotal]

        self._idx_train=set_train_idx
        self._idx_test =set_test_idx
        self._ds_total_raw=np.array(ds_total,object)
        self._ds_total=np.array(dsTotal_bin2,object)
    def get_training(self):
        ''' 
        Return preprocessed training dataset. dataset must have only 
            training values from total dataset, converted to binary array, and 
            rescaled. refer to array as such: ds_train[INDEX][INPUT,OUTPUT]  
        '''
        return self._ds_total[self._idx_train]
    def get_testing(self):
        ''' Return preprocessed testing dataset. dataset contains only testing
            values from total dataset. converted to binary and rescaled. refer
            to array as such: ds_test[INDEX][INPUT,OUTPUT]
        '''
        return self._ds_total[self._idx_test]
    def get_train_dec(self,idx):
        ''' given specific index, return values from given index as decimal 
            values. 
        '''
        return self._ds_total_raw[self._idx_train[idx]]
    def get_test_dec(self,idx):
        return self._ds_total_raw[self._idx_test[idx]]
    
    def to_decimal(self,bin_arr,thresh=0.5):
        ''' given an array of binary values (automatically thresholded), return
            the decimal value of that array. default thresholding value = 0.5
        INPUTS:
            * bin_arr: binary array (scaled or not)
            * thresh: threshold value for removing scaling, default=0.5
        '''
        return bin2dec(threshold(bin_arr))

if(__name__=='__main__'):
    # show example of above functions
    a=-np.pi
    print('orig:',a)
    b=dec2bin(a)
    print('bin :',b)
    print('len :',len(b))
    c=bin2dec(b)
    print('dec2:',c)
    d=scale(b)
    print('scaled:',d)
    e=threshold(d)
    print('descaled:',e)

    dsgen=DatasetGenerator(ntotal=100,ntrain=70)
    print('No. training entries:',len(dsgen.get_training()))
    print('No. testing entries:',len(dsgen.get_testing()))

    rec=dsgen.get_training()[3]
    print('single entry example:\n',rec,len(rec[0]),len(rec[1]))
    print('example in decimal:',dsgen.get_train_dec(3))
    print('single entry conversion:',dsgen.to_decimal(dsgen.get_training()[3][0]))

    rec=dsgen.get_training()[3]
    print('len of input/output:',len(rec[0]),len(rec[1]))

    # want to make sure always have same length for input values, output values.
    lengths=[len(i[0]) for i in dsgen.get_training()]
    lengths_out=[len(i[1]) for i in dsgen.get_training()]
    print('mean length of input:',np.mean(lengths))
    print('mean length of output:',np.mean(lengths_out))

''' 
so, to recap: dataset is generated ([x,y]), then converted to binary arrays,
    then scaled. it is then split into train / test and put into network, and 
    the given result is then thresholded (descaled) and converted (recovered) 
    back into decimal form.
'''



# eof

