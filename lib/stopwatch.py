'''
purpose: start working on a simple lap timer to better record when a certain time is passing

note: it's clear that the previous implementation doesn't behave like what was seen in the conti stopwatch you made. the objective is to have specific functions: 
    1. lap
    2. per-category lapping
    3. reset
    4. clear
    5. difference
    6. average per-category
'''

import time
import numpy as np
from collections import OrderedDict as odict
sleep = time.sleep

class Laps():
    def __init__(self):
        self.tLatest = -1
        self.raw = dict()
        

    def start(self):
        # initialize timer
        self.tLatest = time.time()

    def lap(self,name=0):
        # given a key, check if key exists in dict, add if missing, then log current time.
        if(name in self.raw.keys()):
            self.raw[name].append(time.time()-self.tLatest)
        else:
            # name not in keys
            self.raw[name] = [time.time()-self.tLatest]
        self.tLatest = time.time()
    @property
    def data(self):
        return self.raw
    @property
    def average(self):
        x = dict()
        for ikey in self.raw.keys():
            x[ikey] = np.mean(self.raw[ikey])
        return x

if(__name__ == '__main__'):
    x = Laps()
    x.start()
    for i in range(5):
        sleep(0.1)
        x.lap()
        sleep(0.2)
        x.lap(1)
    
    print(x.data)
    print(x.average)
