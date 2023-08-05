'''
module for importing various items.

TODO: convert image to map for use in python
TODO: create agent that can navigate a map
TODO: have a class that solves paths based on config.
'''

import numpy as np
import matplotlib.pyplot as plt

def rgb2gray(rgb):
    return np.dot(rgb[...,:3],[0.2989, 0.5870, 0.1140])

class Map:
    '''
    0=wall/impassable, 1=valid
    TODO: detect whether there are places that can't be reached (multiple separate regions)
    '''
    def __init__(self,allow_diags=False):
        self.grid:np.ndarray = None
        self.loc_start:np.ndarray = None
        self.loc_end:np.ndarray = None
        self.ind_end = None
        self.path = None # list of points to find way through grid
        self.f,self.p = (None,None)
        self.adjlist = None
        self.allow_diags=allow_diags

    def readimg(self,path):
        ''' read an image and interpret as map. assume each pixel is a location '''
        self.grid = np.array(rgb2gray(plt.imread(path))).round().astype(int)
        self.adjacencyList() # create adjacency list once map is loaded

    def readarr(self,arr:np.ndarray):
        ''' read an array and interpret as map. assume each cell is a location '''
        self.grid = arr
        self.adjacencyList()
    def disp(self):
        ''' return figure and plot of map '''
        _f,_p = plt.subplots()
        _p.imshow(self.grid,cmap='gray')
        xlabels = np.arange(0, self.grid.shape[1] + 1)
        ylabels = np.arange(0, self.grid.shape[0] + 1)
        xticks = xlabels - 0.5
        yticks = ylabels - 0.5
        xlims = [xticks.min(), xticks.max()]
        ylims = [yticks.max(), yticks.min()]
        _p.set_xlim(xlims)
        _p.set_ylim(ylims)
        _p.set_xticks(xticks)
        _p.set_yticks(yticks)
        _p.set_xticklabels(list(xlabels[:-1]) + [" "])
        _p.set_yticklabels(list(ylabels[:-1]) + [" "])
        _p.grid(which='both')



        if(self.loc_start is not None):
            _p.plot(*self.loc_start[::-1], 'ro')
        if(self.loc_end is not None):
            _p.plot(*self.loc_end[::-1], 'rx')
        if(self.path is not None):
            coords = np.array([self.ind2rc(i) for i in self.path])
            _p.plot(coords[:,1],coords[:,0],'g-')
        return _f,_p

    def setStart(self,startpoint:np.ndarray):
        ''' make sure point is valid ground, then convert to index, and save '''
        assert self.grid[startpoint[0],startpoint[1]] != 0, "invalid point"
        self.loc_start = startpoint
    def setEnd(self,endpoint:np.ndarray):
        assert self.grid[endpoint[0],endpoint[1]] != 0, "invalid point"
        self.loc_end = endpoint
        self.ind_end = self.rc2ind(endpoint)
    def selectPoint(self):
        ''' Select a point, perhaps randomly, maybe on edges specifically '''
        pts = self.validpoints()
        ind = int(np.random.choice(range(pts.shape[0]),1))
        return pts[ind]

    def valid_directions(self,loc_rc):
        '''
        Return list of valid coordinates that can be reached from current location (coordinate
            [r,c])
        '''
        def val(ir,ic):
            ''' sub function: return whether particular spot traversible '''
            h,w = self.grid.shape
            if(ir < 0 or ir >= h or ic < 0 or ic > w): return 0
            return self.grid[ir,ic]
        assert val(*loc_rc) != 0,"invalid starting location"
        r,c = loc_rc
        valids = []
        if(val(r-1,c) != 0):valids.append(np.array([r-1,c])) # N
        if(val(r,c+1) != 0):valids.append(np.array([r,c+1])) # E
        if(val(r+1,c) != 0):valids.append(np.array([r+1,c])) # S
        if(val(r,c-1) != 0):valids.append(np.array([r,c-1])) # W

        if(self.allow_diags):
            if(val(r-1,c) != 0):valids.append(np.array([r-1,c]))  # NE
            if(val(r,c+1) != 0):valids.append(np.array([r,c+1]))  # SE
            if(val(r+1,c) != 0):valids.append(np.array([r+1,c]))  # SW
            if(val(r,c-1) != 0):valids.append(np.array([r,c-1]))  # NW
        return valids

    def rc2ind(self,rc_loc):
        return int(rc_loc[0]*self.grid.shape[1]+rc_loc[1]) # irow*width+icol
    def ind2rc(self,ind):
        w = self.grid.shape[1] # width of grid
        return np.array([ind // w, ind % w])

    def adjacencyList(self):
        ''' return adjacency list of map'''
        adjList = dict()
        w = self.grid.shape[1] # ncols
        for i, irow in enumerate(self.grid):
            for j, jcol in enumerate(irow):
                if (self.grid[i, j] != 0):
                    # adjacent, reachable spot relative to current spot
                    cellNo = self.rc2ind([i,j])
                    dirs = self.valid_directions([i,j])
                    adjList[cellNo] = [self.rc2ind(i) for i in dirs]
        self.adjlist = adjList
        return adjList
    def validpoints(self):
        ''' return list of valid places to occupy (where grid==1) '''
        pts = np.column_stack((np.where(self.grid == 1)))
        return pts

    def solve(self,method='dfs'):
        assert self.rc2ind(self.loc_start) != self.rc2ind(self.loc_end),\
            "same start / end locations:{}, {}".format(self.loc_start,self.loc_end)
        if(method == 'dfs'):
            self.path = self.dfs()[1]
        # TODO: add astar
        else:
            raise Exception("incorrect method given")

    def astar(self):
        # todo: add astar
        pass

    def dfs(self,_curr=None,_path=None):
        '''
        Depth-first search. runs recursively. note: need to simplify this code and understand
            better.
            INPUT: (none)
            OUTPUT:
                * status, if solved
                * path, if solved
        '''
        status = False
        if (_path is None):
            _path = []
            self.adjacencyList()
        if(_curr is None):
            _curr = self.rc2ind(self.loc_start)

        _path.append(_curr)
        if (_curr == self.ind_end):
            return True, _path
        else:
            for ioption in self.adjlist[_curr]:
                if (ioption not in _path):
                    status, _path = self.dfs(ioption, _path)
                    if (status):
                        return status, _path
                    elif (len(_path) > 0):
                        _path.pop(-1)  # remove incorrect paths
        return status, _path

    def bfs(self,_curr=None,_goal=None,):
        '''
        Breath-first search. given adjacency list, check for valid cells until find path
        INPUT: (none)
        OUTPUT:
            * status, if solved
            * path, if solved
        # todo: move this to independent function, agent
        '''
        # if()
        pass


class Map2:
    '''
    parse an image file to generate node graph. for each node, return next available node.
    '''
    def __init__(self,allow_diags=False):
        self.grid:np.ndarray = None
        self.loc_start:np.ndarray = None
        self.loc_end:np.ndarray = None
        self.ind_end = None
        self.path = None # list of points to find way through grid
        self.f,self.p = (None,None)
        self.adjlist = None
        self.allow_diags=allow_diags

    def readimg(self,path):
        '''
        Read an image and interpret as map. assume each pixel is a location
        1=passable,0=unpassable
        '''
        self.grid = np.array(rgb2gray(plt.imread(path))).round().astype(int)
        return self

    def readarr(self,arr:np.ndarray):
        '''
        Read an array and interpret as map. assume each cell is a location.
        1 = passable, 0 = not passable
        '''
        self.grid = arr
        return self

    def disp(self,start=None,end=None,pathlist=None):
        ''' return figure and plot of map '''
        _f,_p = plt.subplots()
        _p.imshow(self.grid,cmap='gray')
        xlabels = np.arange(0, self.grid.shape[1] + 1)
        ylabels = np.arange(0, self.grid.shape[0] + 1)
        xticks = xlabels - 0.5
        yticks = ylabels - 0.5
        xlims = [xticks.min(), xticks.max()]
        ylims = [yticks.max(), yticks.min()]
        _p.set_xlim(xlims)
        _p.set_ylim(ylims)
        _p.set_xticks(xticks)
        _p.set_yticks(yticks)
        _p.set_xticklabels(list(xlabels[:-1]) + [" "])
        _p.set_yticklabels(list(ylabels[:-1]) + [" "])
        _p.grid(which='both')

        if(start is not None): _p.plot(*start[::-1], 'ro')
        if(end is not None):   _p.plot(*end[::-1], 'rx')
        if(pathlist is not None):
            coords=np.array(pathlist)
            _p.plot(coords[:,1],coords[:,0],'g-')
        return _f,_p

    def adjacent(self, loc_rc):
        '''
        Return list of valid coordinates that can be reached from current location ([r,c])
        '''
        def val(ir,ic):
            ''' sub function: return whether particular spot traversible '''
            h,w = self.grid.shape
            if(ir < 0 or ir >= h or ic < 0 or ic > w): return 0
            return self.grid[ir,ic]
        assert val(*loc_rc) != 0,"invalid starting location"
        r,c = loc_rc
        valids = []
        if(val(r-1,c) != 0):valids.append(np.array([r-1,c])) # N
        if(val(r,c+1) != 0):valids.append(np.array([r,c+1])) # E
        if(val(r+1,c) != 0):valids.append(np.array([r+1,c])) # S
        if(val(r,c-1) != 0):valids.append(np.array([r,c-1])) # W

        if(self.allow_diags):
            if(val(r-1,c) != 0):valids.append(np.array([r-1,c]))  # NE
            if(val(r,c+1) != 0):valids.append(np.array([r,c+1]))  # SE
            if(val(r+1,c) != 0):valids.append(np.array([r+1,c]))  # SW
            if(val(r,c-1) != 0):valids.append(np.array([r,c-1]))  # NW
        return valids

    def validpoints(self):
        ''' return list of valid places to occupy (where grid==1) '''
        return np.column_stack((np.where(self.grid == 1)))


def depth_first_search(mapgraph:Map2,start:np.ndarray,goal:np.ndarray):
    '''
    Depth-first search. runs recursively. note: need to simplify this code and understand
        better.
        INPUT: (none)
        OUTPUT:
            * path, if solved
    '''

    def dfs(ipt, _path=None):
        ''' if current node not solution, check next available option. if invalid, return None '''
        if _path is None: _path = []
        res=False
        if(_path is None): _path = []
        _path.append(ipt)
        if(tuple(ipt) == tuple(goal)):
            return True, _path
        # otherwise, try next available options
        for iopt in mapgraph.adjacent(ipt):
            if(tuple(iopt) not in _path):
                res,_path = dfs(tuple(iopt),_path)
                if(res): return res, _path
                elif(len(_path)>0):
                    _path.pop(-1) # drop incorrect paths
        return res, _path

    result,pathout=dfs(tuple(start))
    if(result): return pathout
    else: return []


def dijkstra_search(mapgraph,start,goal):
    '''
    find path to reach goal after creating graph
    1. create graph to determine each one
    '''
    pass

def astar_search(mapgraph,start,goal):
    ''' use a-star search to find a path '''
    pass




if(__name__ == '__main__'):

    m = Map2().readimg('maze2r1.png')
    pt_start = np.array([1,1])
    # pt_end = np.array([5,15]) # unreachable node
    pt_end = np.array([23,23]) # unreachable node

    path = depth_first_search(m,pt_start,pt_end)
    if(len(path)==0): path=None

    f,p = m.disp(pt_start,pt_end,path) # (r,c) notation
    plt.show()





