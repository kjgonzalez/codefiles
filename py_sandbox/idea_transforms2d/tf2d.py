'''
try applying rotation and translation to 2d pose, given knowing who parent is, etc.

need way to move a pose between different parents. 

world -> parent
parent -> world
pid=None === world, always pose(1,1,0deg)

need singleton to track all items?
use hidden world pose?
need to check at each pose creation for all items

p0_inw = pose(0,0,45,0,None)    # pose0 in world
p1_in0 = pose(0,0,45,1,p0_inw)  # pose1 in pose0

## option1 
p2_inw = pose(3,4,0,2,None)     # pose2 in world
p2_in1 = p1_in0.toLocal(p2_inw) # pose2 in pose1


## option2
p2 = pose(3,4,0,2,None)  # pose2 in world
p2.toWorld()             # in-place operation, returns self
p2.toLocal(p1_in0)       # in-place operation, returns self


# going with option 2

'''
from __future__ import annotations
import numpy as np
pi=np.pi
sind = lambda xdeg:np.sin(xdeg*pi/180)
cosd = lambda xdeg:np.cos(xdeg*pi/180)
sin = np.sin
cos = np.cos

class pose2d:
    def __init__(self,x,y,a,uid=0,par:pose2d=None,deg=True):
        self.x=x
        self.y=y
        self.a=a if(deg) else a*180/pi
        self.uid=uid # unique id
        self.par=par # link to parent
    def __repr__(self):
        pid = -1 if(self.par is None) else self.par.uid
        return f"p({self.x:0.3f},{self.y:0.3f},{self.a:0.3f}deg,{self.uid}/{pid})"
    @property
    def tf(self):
        c=cosd(self.a);s=sind(self.a)
        return np.reshape([  c,s,-self.x,  -s,c,-self.y,  0,0,1  ],(3,-1))

    def toWorld(self,inplace=True):
        '''
            if inplace, return self. else, return new item. for each parent, 
        get own coordinate in that reference frame until in world.
        '''
        ip = np.array([[self.x,self.y,1]]).T
        ia = self.a
        parent=self.par
        while(parent is not None):
            ip = np.linalg.inv(parent.tf)@ip
            ia = ia+parent.a
            parent=parent.par
        if(inplace):
            self.x=ip[0,0]
            self.y=ip[1,0]
            self.a=ia
            self.par=None
            return self
        else: return pose2d(ip[0,0],ip[1,0],ia,self.uid)
    def toLocal(self,des:pose2d,inplace=True):
        ''' from world, convert to desired pose's local frame '''
        p0=self.toWorld(inplace=False)
        ip = np.array([[p0.x,p0.y,1]]).T
        ia = p0.a
        chain = [des]
        parent=des.par
        while(parent is not None):
            chain.insert(0,parent)
            parent = parent.par
        for ipose in chain:
            ip = ipose.tf@ip
            ia = ia-ipose.a
        return pose2d(ip[0,0],ip[1,0],ia,self.uid,des)

if(__name__ == '__main__'):
    print('---- translation ----')
    p0 = pose2d(1,1,0,0)
    p1 = pose2d(1,1,0,1,p0)
    p2 = pose2d(1,1,0,2,p1)
    print("p2_1:",p2)
    print("p2_w:",p2.toWorld())

    print('---- rotation ----')
    p0=pose2d(0,0,45,0)
    p1=pose2d(0,0,45,1,p0)
    p2=pose2d(1,-1,-90,2,p1)
    p2b=p2.toWorld()
    print("p2_1:",p2)
    print("p2_w:",p2.toWorld())

    print('--- both ----')
    p0 = pose2d(1,0,45,0)
    p1 = pose2d(1,0,-45,1,p0)
    p2 = pose2d(1,1,20,2,p1)
    print("p2_1:",p2)
    #print("pred: p(5,4,0deg)")
    print("p2_w:",p2.toWorld())

    print('---- world2local ----')
    p0 = pose2d(1,1,0,0)
    p1 = pose2d(0,0,45,1,p0)
    p2 = pose2d(2,2,30,2)
    print("p2_w:",p2)
    print("p2_1:",p2.toLocal(p1))


# eof

