'''
some basic examples of how to use matplotlib, along with some perhaps intersting
    unique applications of the module.


'''

import numpy as np
import matplotlib.pyplot as plt
print('test')

''' first, will demonstrate simple plotting plots ========================== '''
if(False):
    x=np.linspace(0,6)
    y=np.sin(x)
    y2=np.cos(x)

    f,p=plt.subplots()
    p.plot(x,y,color=(1,0,0))
    plt.plot()

''' quick demonstration of histograms ====================================== '''

if(False):
    n=10000
    x=(np.random.rand(n)*np.random.rand(n))**0.5

    f,[p1,p2]=plt.subplots(1,2,figsize=[8,4])

    # first, show basic
    p1.hist(x)

    # next, show more advanced version
    bins = [0,0.3,0.5,1]
    p2.hist(x,bins,edgecolor='black',linewidth=1)
    p2.set_axisbelow(True)
    p2.grid()

''' bar chart ============================================================== '''

if(False):
    f,p=plt.subplots()
    # help(p.bar)
    x=[1,2,3,4,5]
    y=np.random.rand(5)
    # x=['[{},{})'.format(i,i+10) for i in range(0,80,10)]
    p.bar(x,y)

    ''' customization while using "f,p" ======================================== '''

    f,p = plt.subplots()
    x=np.random.rand(5)
    y=np.random.rand(5)
    scale=7 # general size
    ratio=2 # how wide, such as 4:3 = 1.33
    f,p=plt.subplots(1,2,figsize=(scale*ratio,scale))
    p[0].plot(x,y)
    p[0].set_title('title')
    p[0].set_xlim([0,1])
    p[0].set_ylim([0,1])
    p[0].set_xlabel('xlabel')
    p[0].set_ylabel('ylabel')
    p[0].grid()
    p[0].set_aspect('equal')

''' using a colormap '''
if(False):
    from matplotlib import cm

    f,p=plt.subplots()
    viridis = cm.get_cmap('viridis', 5)
    x=np.linspace(0,6)
    for i in range(5):
        p.plot(x,np.sin(x)+i,color=viridis.colors[i])
    # plt.show()

''' creating own colormap '''
if(True):
    x=np.linspace(0,6)
    from matplotlib.colors import ListedColormap, LinearSegmentedColormap
    cdict = {'red':   [[0.0,  0.0, 0.0],
                       [1.0,  1.0, 1.0],
                       [1.0,  1.0, 1.0]],
             'green': [[0.0,  0.0, 0.0],
                       [0.25, 0.0, 0.0],
                       [0.75, 1.0, 1.0],
                       [1.0,  1.0, 1.0]],
             'blue':  [[0.0,  0.0, 0.0],
                       [0.5,  0.0, 0.0],
                       [1.0,  1.0, 1.0]]}


    newcmp = LinearSegmentedColormap('testCmap', segmentdata=cdict, N=256)
    rgba = newcmp(np.linspace(0, 1, 5))
    f,p = plt.subplots()
    # import ipdb; ipdb.set_trace()
    for i in range(5):
        p.plot(x,np.sin(x)+i,color=rgba[i])
plt.show()
# plt.show()
