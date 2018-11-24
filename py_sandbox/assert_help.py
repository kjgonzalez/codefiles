'''
objective: learn how to use assert statement in python

Main purpose of assert: find bugs quickly, and it should be used where the 
    problem can be clearly identified before something worse happens later


In particular, [assertions are] good for catching false assumptions that were made while writing the code, or abuse of an interface by another programmer.

source: https://wiki.python.org/moin/UsingAssertionsEffectively
'''

assert True # this should finish quietly and let the program continue running

try:
    assert False # this would cause an assertion error in the program
except AssertionError:
    print("false assertions cause program to exit")

# anything that can evaluate to a boolean and is part of debugging forms the 
#   basis for using assert.

#to print a message, just add:

import os
filename='gobbledygook.txt'
errmsg = lambda filename:"duh, file {} doesn't exist".format(filename)
try:
    assert os.path.exists(filename),errmsg(filename)
except:
    print("here, program would give a specific error and then exit, such as:")
    print(errmsg(filename)+'\n')

