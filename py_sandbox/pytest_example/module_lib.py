'''
Author: Kris Gonzalez
DateCreated: 190114
Objective: write tests that execute on a given set of code in order to test
    compatability and give an example of "continuous integration"

General Steps:
1. make a few random functions
2. in another file, write tests for those functions
3. run "pytest" and output results

How to Run:
>> pytest
'''

def pyt(arr):
    ''' return 2-norm of an array '''
    return sum([i**2 for i in arr])**0.5

def area_rect(x,y):
    ''' get area of a rectangle '''
    return x*y
