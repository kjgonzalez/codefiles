'''
want to implement a basic kmeans clustering algo, based on what was written in wikipedia
  https://en.wikipedia.org/wiki/K-means_clustering
'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time


class Kset:
    def __init__(self,initial_xy):
        self.pts=[initial_xy]
        self.mean:np.ndarray=None
        self.sig_previous:np.ndarray=None
    def updatemean(self):
        self.mean = np.mean(self.pts,axis=0)

    @property
    def signature(self):
        return np.linalg.norm(self.pts,axis=1) # not the best solution, but will use for now

def converged(list_of_ksets):
    for ik in list_of_ksets:
        sigold = ik.sig_previous
        signew = ik.signature
        if(len(sigold)!=len(signew)): return False
        elif(not (sigold == signew).all()): return False
    return True

def cluster_kmeans(list_xy,k=2,maxit=100,withplot=False):
    '''
    list_xy: points to cluster into groups
    k: number of expected clusters
    maxit: maximum number of iterations
    '''
    dat = np.column_stack((np.array(list_xy),[-1]*len(list_xy)))
    done=False
    while(not done):
        np.random.shuffle(dat) # shuffle, even if already shuffled
        pt0=dat[0,:2]
        pt1=dat[1,:2]
        if(np.linalg.norm(pt1-pt0)<0.3):
            done=True

    ksets=[]
    for i in range(k):
        dat[i,2]=i # set which group it's assigned to

    ptr = k
    iloop=0
    if(withplot):
        f, p = plt.subplots()
    while(iloop<maxit):
        '''
        update means
        calculate set of next marker
        check if converged
        '''
        oldsig = dat[:,2].copy()
        means = []
        for i in range(k):
            isub = dat[dat[:,2]==i]
            imean = isub.mean(0)[:2]
            means.append(imean)
        ipt = dat[ptr,:2]
        diffs = np.array(means)-ipt
        dists = np.linalg.norm(diffs,axis=1)
        ind_min = dists.argmin()
        dat[ptr,2] = ind_min

        newsig = dat[:,2]
        if((oldsig==newsig).all() and iloop>len(dat)+k-1):
            return dat

        if(withplot):
            f.clf()
            p = f.add_subplot()
            p.plot(*dat[ptr,:2],'rx')
            for i in range(-1,k):
                sub = dat[dat[:,2]==i]
                p.plot(sub[:,0],sub[:,1],'.')

            #plt.show()

        ptr = ptr+1 if(ptr<len(list_xy)-1) else 0 # loop back around
        iloop+=1
        # go to next while
    return None

if(__name__=='__main__'):
    nhalf = 10
    pts = []
    for i in range(nhalf):
        x = 1+np.random.rand()-0.5
        y = 2+np.random.rand()-0.5
        pts.append([x,y,1])
    for i in range(nhalf):
        x = 2+np.random.rand()-0.5
        y = 1+np.random.rand()-0.5
        pts.append([x,y,2])
    pts = pd.DataFrame(pts,columns='x y label'.split(' '))
    res = cluster_kmeans(pts['x y'.split(' ')].to_numpy(),2,withplot=True)
    p:plt.Axes=None
    f,p = plt.subplots()
    p.grid()
    p.set_xlim([0,3])
    p.set_ylim([0,3])
    p.plot(pts.x[:nhalf],pts.y[:nhalf],'.')
    p.plot(pts.x[nhalf:],pts.y[nhalf:],'.')
    plt.show()







# eof
