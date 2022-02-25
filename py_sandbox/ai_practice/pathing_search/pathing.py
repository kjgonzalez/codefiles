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
    def __init__(self):
        self.grid:np.ndarray = None
        self.loc_start:list=None
        self.loc_end:list = None
        self.f,self.p = (None,None)
    def readimg(self,path):
        ''' read an image and interpret as map. assume each pixel is a location '''
        self.grid = np.array(rgb2gray(plt.imread(path))).round().astype(int)
    def disp(self):
        ''' return figure and plot of map '''
        f,p = plt.subplots()
        p.imshow(self.grid)
        return f,p
    def selectStart(self):
        ''' select a starting location, perhaps randomly, maybe on edges specifically '''
        pass
    def selectEnd(self):
        ''' select a goal, perhaps randomly, maybe on edges specifically '''
        pass
    def adjacencyList(self):
        ''' return adjacency list of map'''


if(__name__ == '__main__'):
    m = Map()
    m.readimg('maze3.png')
    f,p = m.disp()
    plt.show()
