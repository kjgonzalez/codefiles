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
    ''' Take decimal value and return custom binary array of value between -4 
        and 4. 
    '''
    assert val<=4.0 and val>=-4.0, "value out of range:"+str(val)
    arr=[]
    # pos/negative
    if(val<0):
        arr.append(1)
    else:
        arr.append(0)
    val2=abs(int(round(val*100000,0)))
    val3=pad(bin(val2)[2:],16,'0')
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



# eof

