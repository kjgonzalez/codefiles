'''
convenient place to store 2d transform stuff
'''
from __future__ import annotations
import numpy as np


class Pose:
    ''' convenient way to work on 2d transforms '''
    def __init__(self,x,y,a):
        self.x=x
        self.y=y
        self.a=a
        self._r=self.a*np.pi/180
    def __repr__(self): return f"({self.x:0.3f},{self.y:0.3f},{self.a}deg)"
    def _gettf(self,astf=False):
        s=np.sin(self._r)
        c=np.cos(self._r)
        x=self.x*(-1 if(astf) else 1)
        y=self.y*(-1 if(astf) else 1)
        return np.reshape([c,s,x,-s,c,y,0,0,1],(3,-1))

    def _astf(self):
        return 1
    def _asmat(self):

    def _mult(self,p:Pose):
        return 1

def getT(x,y,a,tf=False):
    c=np.cos(a*dr)
    s=np.sin(a*dr)
    x*=-1 if(tf) else 1
    y*=-1 if(tf) else 1
    return np.reshape([c,s,x,-s,c,y,0,0,1],(3,-1))


if(__name__ == '__main__'):
    print('starting')
    


# eof

