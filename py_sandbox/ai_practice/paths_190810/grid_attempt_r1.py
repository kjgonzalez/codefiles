'''
datecreated: 190811
objective: work on creating a depth-first search and breadth-first search
    example here, then transferring back to a python script. using jupyter
    notebook because of it's rapid prototyping capability
'''

''' INITIALIZATIONS ======================================================== '''
import numpy as np
import matplotlib.pyplot as plt

# setup functions
def plotgrid(gridarr,fsize=4):
    ''' ensure that plot comes out nicely formatted '''
    nrows,ncols = gridarr.shape
    f,p=plt.subplots(figsize=[fsize]*2)
    p.imshow(gridarr,cmap='gray')
    xticks=np.arange(0,ncols+1)-0.5
    yticks=np.arange(0,nrows+1)-0.5
    xlims=[xticks.min(),xticks.max()]
    ylims=[yticks.min(),yticks.max()]
    p.set_xticks(xticks,minor=True)
    p.set_yticks(yticks,minor=True)
    p.grid(b=True,which='minor')
    return f,p

def canGoInDir(arr,coord,direction):
    '''
    create a map that says whether a point can go in a given direction.
        alternative to making a tree in the typical sense.
        only works with orthogonal directions (no diagonals coded here)
    '''
    row,col=coord
    if(direction==0):
        # check if can go 'up'
        if(row==0): return False # at top row
        elif(arr[row-1,col]==0): return False # occupied
        else: return True
    elif(direction==1):
        # check if can go 'right'
        if(col==arr.shape[1]-1): return False # at right-most column
        elif(arr[row,col+1]==0): return False # occupied
        else: return True
    elif(direction==2):
        # check if can go 'down'
        if(row==arr.shape[0]-1): return False # at bottom row
        elif(arr[row+1,col]==0): return False # occupied
        else: return True
    elif(direction==3):
        # check if can go 'left'
        if(col==0): return False # at left-most column
        elif(arr[row,col-1]==0): return False # occupied
        else: return True
    else: print('error: not a valid direction')

def coord2cellnum(coord,gridwidth):
    ''' assume coordinate is (row,col) '''
    return coord[0]*gridwidth+coord[1]
def cellnum2coord(num,gridwidth):
    i=1
    while(i*gridwidth<=num):i+=1
    i-=1
    return [i,num-i*gridwidth]
def makeAdjList(arr):
    ''' create adjacency list '''
    adjList = dict()
    w=arr.shape[1]
    for i,irow in enumerate(arr):
        for j,jcol in enumerate(irow):
            if(arr[i,j]!=0):
                # not empty
                ilist = []
                if(canGoInDir(arr,[i,j],0)): ilist.append((i-1)*w+j) # can go up
                if(canGoInDir(arr,[i,j],1)): ilist.append(i*w+(j+1)) # right
                if(canGoInDir(arr,[i,j],2)): ilist.append((i+1)*w+j) # down
                if(canGoInDir(arr,[i,j],3)): ilist.append(i*w+(j-1)) # left
                cellNo = int(i*arr.shape[1]+j)
                adjList[cellNo] = ilist
    return adjList
def path2coords(pathlist,gridwidth):
    w=gridwidth;coords = []
    for ipoint in pathlist:
        coords.append( cellnum2coord(ipoint,w) )
    return coords

# grid 4 (dungeon problem grid)
grid = np.ones((5,7))
grid[0,3]=0
grid[1,1]=0
grid[1,5]=0
grid[2,1]=0
grid[3,2]=0
grid[3,3]=0
grid[4,0]=0
grid[4,2]=0
grid[4,5]=0
loc_start=[0,0]
loc_end  =[4,3] # row/col format
print('map created')

w=grid.shape[1]
st = coord2cellnum(loc_start,w)
en = coord2cellnum(loc_end,w)
print('start / end locations created')
adj=makeAdjList(grid)
print('adjacency list created')


''' BREADTH-FRIST SEARCH =================================================== '''
def bfs(_adjlist,options,goal,history=None,oldoptions=None):
    ''' simple attempt at bfs. added "history" to properly keep track of where things have been
    INPUTS:
        * _adjlist: adjacency list. list of new available paths, given current location
        * options: starting location. internally, list of current options
        * goal: end point to reach.
        * history: internal variable. remembers all visited notes, prevents infinite loops
        * oldoptions: internal variable. key to remembering previous path taken
    '''
    if(type(options)!=list):
        # first iteration
        history=[options] # prevent infinite loops
        options=[options] # aka current location
    else:
        history+=options
    newoptions=[]
    prevoptions=[]
    for i,ioption in enumerate(options): # for each currently known option...
        if(ioption==goal):
            print('solved!')
            print('prev loc:',oldoptions[i])
            return [ioption] # return solution
        # while generating new paths, remember old ones
        for inew in _adjlist[ioption]:
            if(inew not in history):
                newoptions.append(inew)
                prevoptions.append(ioption)
    if(len(newoptions)>0):
        # can continue
        path = bfs(_adjlist,newoptions,goal,history.copy(),prevoptions.copy())
        # if a solution is found, path represents correct item in newoptions
        # finding the index of that option leads to the right previous option
        iloc=newoptions.index(path[0])
        path.insert(0,prevoptions[iloc])
        return path
    else:
        print('no solution found')
        return None

# solve and plot everything
path = bfs(adj,st,en)
print('path:',path)

coords=np.array(path2coords(path,grid.shape[1]))
f,p=plotgrid(grid,8)
p.plot(*loc_start[::-1],'ro')
p.plot(*loc_end[::-1],'rx')
p.plot(coords[:,1],coords[:,0],'g-')
plt.show() # necessary when running as a script and not in notebook

''' DEPTH-FIRST SEARCH ===================================================== '''
def dfs(_adjlist,curr,goal,_path=None):
    ''' depth-first search. runs recursively. note: need to simplify this code and understand better. '''
    status=False
    if(_path==None):
        _path = []
    _path.append(curr)
    if(curr==goal):
        return True,_path
    else:
        for ioption in _adjlist[curr]:
            if(ioption not in _path):
                status,_path = dfs(_adjlist,ioption,goal,_path)
                if(status==True):
                    return status,_path
                elif(len(_path)>0):
                    _path.pop(-1) # remove incorrect paths
    return status,_path


# solve and plot everything
path = dfs(adj,st,en)[1]
print('path:',path)

coords=np.array(path2coords(path,grid.shape[1]))
f,p=plotgrid(grid,8)
p.plot(*loc_start[::-1],'ro')
p.plot(*loc_end[::-1],'rx')
p.plot(coords[:,1],coords[:,0],'g-')
plt.show() # necessary when running as a script and not in notebook
