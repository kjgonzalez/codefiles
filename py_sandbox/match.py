'''
simple function that helps match a value in an array to a given value. example 
    task is to compare a detection with several ground truth bounding boxes to
    generate highest iou pair.
kjg190529: have discovered even simpler way of finding best match. described below.
'''

import numpy as np

def find_best_match(value,array,function,objective='min'):
    ''' return index of value in array that best matches a given item, based on
            min / max value.
    '''
    results=[]
    for item in array:
        results.append(function(value,item))
    if(objective=='min'):
        return np.argmin(results)
    elif(objective=='max'):
        return np.argmax(results)

print('example 1 '+'-'*30)
# here, want to find index of value closest to a, 2.0
a=2.0
b=[0.0,1.0,3.5,2.1,2.5,3.0]
def f(a,b):
    return abs(a-b)
ind=find_best_match(a,b,f)
print('ind {}: {}'.format(ind,b[ind]))

# ==============================================================================
print('example 2 '+'-'*30)
# here, give index of value that produces highest result.
a=2.0
b=[0.0,1.0,3.5,2.1,2.5,3.0]
def f2(a,b):
    return a*b
ind=find_best_match(a,b,f2,objective='max')
print('ind {}: {}'.format(ind,b[ind]))

# ==============================================================================
print('example 3'+'-'*30)
# ok, try to do it in one line with argmin / argmax
a=2.0
b=[0.0,1.0,3.5,2.1,2.5,3.0]
def f3(ival):
    return a*ival
ind = np.argmax(list(map(f3,b)))
print('ind {}: {}'.format(ind,b[ind]))


