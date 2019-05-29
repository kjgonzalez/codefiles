'''
simple function that helps match a value in an array to a given value. example
    task is to compare a detection with several ground truth bounding boxes to
    generate highest iou pair.
kjg190529: have discovered even simpler way of finding best match. described below.

kjg190529_2: will augment current function to return actual best value as well.
'''

import numpy as np

def find_best_match(value,array,function,objective='min'):
    ''' given a value, array, and function, find best match that maximizes or
        minimizes result from each index in array. return index and result that
        meets criteria.
    INPUTS:
        * value: single object, to be compared with other items
        * array: list of objects, to compare to 'value'
        * function: comparison function for value and each object in array
        * objective: criteria to meet. 'min','max'. default: 'min'
    OUTPUTS:
        * result: best output that matches criteria
        * index: index of best output in array
    '''
    results=[]
    for item in array:
        results.append(function(value,item))
    if(objective=='min'):
        index = np.argmin(results)
    elif(objective=='max'):
        index = np.argmax(results)
    return function(value,array[index]),index

# ==============================================================================
print('example 1 '+'-'*30)
# here, want to find index of value closest to a, 2.0
a=2.0
b=[0.0,1.0,3.5,2.1,2.5,3.0]
def f(a,b):
    return abs(a-b)
res,ind=find_best_match(a,b,f)
print('ind {} | arr {} | res {}'.format(ind,b[ind],res))

# ==============================================================================
print('example 2 '+'-'*30)
# here, give index of value that produces highest result.
a=2.0
b=[0.0,1.0,3.5,2.1,2.5,3.0]
def f2(a,b):
    return a*b
res,ind=find_best_match(a,b,f2,objective='max')
print('ind {} | arr {} | res {}'.format(ind,b[ind],res))

# ==============================================================================
print('example 3'+'-'*30)
# ok, try to do it in one line with argmin / argmax.
# kjg190529: nto that helpful now that want 2 values returned
a=2.0
b=[0.0,1.0,3.5,2.1,2.5,3.0]
def f3(ival):
    return a*ival
ind = np.argmax(list(map(f3,b)))
print('ind {} | arr {} | res {}'.format(ind,b[ind],f3(b[ind])))
