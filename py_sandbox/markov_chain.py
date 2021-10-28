'''
learn a little bit about markov chains


'''

import numpy as np
import argparse

mat = np.array([ # state transition matrix
    [2,6,2],
    [1,6,3],
    [2,7,1]
])/10
states = "sleep,run,icecream".split(',')

class MarkovSimple:
    def __init__(self,transitionmatrix:np.ndarray,statenames:list,initialstate=-1):
        ''' initialize markov chain. if no initial state given, one chosen at random'''
        self.m = transitionmatrix
        self.s = statenames
        r,c = self.m.shape
        assert r == c, "state transition matrix isn't square"
        assert r == len(self.s), "number of states doesn't match matrix"
        irow:np.ndarray = None
        for irow in self.m:
            assert np.isclose(irow.sum(),1.0),"row doesn't add up to 1: {}".format(irow)
        if(initialstate == -1):
            initialstate = np.random.choice(len(self.s))
        self.curr_state = initialstate
        self.hist = [self.curr_state]
        print('initial state:',self.s[self.curr_state])

    def next(self):
        ''' based on current state, go to next state'''
        irow = self.m[self.curr_state]
        self.curr_state = np.random.choice(len(self.s),p=irow)
        self.hist.append(self.curr_state)
        print('new state:',self.s[self.curr_state])


if(__name__ == '__main__'):
    # test out weather markov chain, using probabilities (not dice)
    mat = np.array([
        [0.7,0,0,0,0.09,0.075,0.09,0.045],
        [0,0.7,0,0,0.09,0.075,0.09,0.045],
        [0,0,0.7,0,0.09,0.075,0.09,0.045],
        [0,0,0,0.7,0.09,0.075,0.09,0.045],
        [0.075,0.075,0.075,0.075,0.21,0.175,0.21,0.105],
        [0.075,0.075,0.075,0.075,0.21,0.175,0.21,0.105],
        [0.075,0.075,0.075,0.075,0.21,0.175,0.21,0.105],
        [0.075,0.075,0.075,0.075,0.21,0.175,0.21,0.105],
    ])
    states = 'cool & foggy,clear & cool,clear & warm,cloudy & warm,clear & dry,rain showers,rain,storm'.split(',')
    am = MarkovSimple(mat, states)
    for i in range(10):
        am.next()

# eof



