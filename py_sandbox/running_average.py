'''
author: Kris Gonzalez
datecreated: 180716
objective: quick demo of how a running average can be programmed for path\
    planning node.
'''


import time
import numpy as np
import random


comm_avg=np.linspace(0,0,10)
class RunningAvg(object):
    ''' make a class of a running object, so don't need to keep track of
        global variables and so on. will assume that order of latest items
        is not relevant to user

        FUTURE IMPLEMENTATION: getLastValues(), where user can get last several
        values added in chronological order
    '''
    def __init__(self,size=10,initialvalue=0):
        import numpy as np
        self.np = np
        self.data = self.np.linspace(0,0,10)
        self.iwrite = 0 # write value to this spot, then increment

    def getAvg(self):
        ''' get average of all values in array'''
        return self.np.mean(self.data)
    def addValue(self,NewValue):
        ''' add a new value to array, let object handle where it is written.
        '''
        self.data[self.iwrite] = NewValue
        # increment iwrite, or reset to zero
        self.iwrite=self.iwrite+1
        if(self.iwrite==10):
            self.iwrite = 0
# class RunningAvg

ra = RunningAvg()
print ra.data

while True:
    time.sleep(.1)
    newval = random.random()
    ra.addValue(newval)
    print ra.data
    print ra.getAvg()
