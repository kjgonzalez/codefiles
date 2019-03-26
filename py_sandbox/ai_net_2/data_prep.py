'''
author: Kris Gonzalez
Objective: create a basic, simple network to predict the value of x^3-x between
    -4 and 4. will keep using self-made network, but would like to move to 
    pytorch soon / at some point.

'''
import numpy as np
from klib import scale


# first, need to generate some data and convert it into something readable by network.

x=np.linspace(-4,4)
y=x**3-x

# want to have a function that can transform a value into some binary-like representation... e.g. '-3.817' = (+/-) (integer part) (decimal part)

def toBin(val):
    ''' return custom binary representation of value between -4 & 4 '''
    assert val<=4.0 and val>=-4.0, "value out of range:"+str(val)
    arr=[]
    # pos/negative
    if(val<0):
        arr.append(1)
    else:
        arr.append(0)
    # integer part
    # val2 .... 
    # multiply by 1k, to int, abs, get list of booleans






# eof

