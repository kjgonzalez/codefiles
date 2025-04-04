'''
some basic examples of how to use matplotlib, along with some perhaps intersting
    unique applications of the module.


'''

import numpy as np
import matplotlib.pyplot as plt

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
    p[0].set_aspect('equal') # aspect ratio

''' using a colormap ======================================================= '''
if(False):
    from matplotlib import cm

    f,p=plt.subplots()
    viridis = cm.get_cmap('viridis', 5)
    x=np.linspace(0,6)
    for i in range(5):
        p.plot(x,np.sin(x)+i,color=viridis.colors[i])
    # plt.show()

''' creating own colormap ================================================== '''
if(False):
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

''' color invidiual points like a colormap ================================= '''
if(False):
    x = np.linspace(0,6)
    y = np.sin(x)
    plt.scatter(x,y,c=y)

''' creating a broken axis ================================================= '''
if(False):
    # src: https://matplotlib.org/3.1.0/gallery/subplots_axes_and_figures/broken_axis.html
    pts = np.array([
        0.015, 0.166, 0.133, 0.159, 0.041, 0.024, 0.195, 0.039, 0.161, 0.018,
        0.143, 0.056, 0.125, 0.096, 0.094, 0.051, 0.043, 0.021, 0.138, 0.075,
        0.109, 0.195, 0.050, 0.074, 0.079, 0.155, 0.020, 0.010, 0.061, 0.008])

    # Now let's make two outlier points which are far away from everything.
    pts[[3, 14]] += .8

    # If we were to simply plot pts, we'd lose most of the interesting
    # details due to the outliers. So let's 'break' or 'cut-out' the y-axis
    # into two portions - use the top (ax) for the outliers, and the bottom
    # (ax2) for the details of the majority of our data
    f, (ax, ax2) = plt.subplots(2, 1, sharex=True)

    # plot the same data on both axes
    ax.plot(pts)
    ax2.plot(pts)

    # zoom-in / limit the view to different portions of the data
    ax.set_ylim(.78, 1.)  # outliers only
    ax2.set_ylim(0, .22)  # most of the data

    # hide the spines between ax and ax2
    ax.spines['bottom'].set_visible(False)
    ax2.spines['top'].set_visible(False)
    ax.xaxis.tick_top()
    ax.tick_params(labeltop=False)  # don't put tick labels at the top
    ax2.xaxis.tick_bottom()

    # This looks pretty good, and was fairly painless, but you can get that
    # cut-out diagonal lines look with just a bit more work. The important
    # thing to know here is that in axes coordinates, which are always
    # between 0-1, spine endpoints are at these locations (0,0), (0,1),
    # (1,0), and (1,1).  Thus, we just need to put the diagonals in the
    # appropriate corners of each of our axes, and so long as we use the
    # right transform and disable clipping.

    d = .015  # how big to make the diagonal lines in axes coordinates
    # arguments to pass to plot, just so we don't keep repeating them
    kwargs = dict(transform=ax.transAxes, color='k', clip_on=False)
    ax.plot((-d, +d), (-d, +d), **kwargs)        # top-left diagonal
    ax.plot((1 - d, 1 + d), (-d, +d), **kwargs)  # top-right diagonal

    kwargs.update(transform=ax2.transAxes)  # switch to the bottom axes
    ax2.plot((-d, +d), (1 - d, 1 + d), **kwargs)  # bottom-left diagonal
    ax2.plot((1 - d, 1 + d), (1 - d, 1 + d), **kwargs)  # bottom-right diagonal

''' importing / manipulating images ======================================== '''
if(False):
    fpath = '../data/baby.jpg'
    def rgb2gray(rgb):
        return np.dot(rgb[...,:3],[0.2989, 0.5870, 0.1140])
    im = plt.imread(fpath)
    f,p = plt.subplots(2)
    p[0].imshow(im)
    p[1].imshow(rgb2gray(im))

''' blitting =============================================================== '''
if(False):
    def run_blitting():
        from matplotlib.backend_bases import KeyEvent
        from random import random
        flag_blitting_done = False  # note: bad practice, but convenient for small example

        def cbQuit(evkey: KeyEvent):
            print('pressed:', evkey.key)
            global flag_blitting_done
            flag_blitting_done = True
        print('Default quit: "q"')
        #x = np.linspace(-2*np.pi,0, 100)
        #x = np.linspace(-99,0,100)
        x = list(range(-99,1,1))
        buff = RingBuffer()

        # prepare graph for blitting
        fig, ax = plt.subplots()
        fig.canvas.mpl_connect('key_press_event',cbQuit)
        (ln,) = ax.plot(x,buff.latest(), animated=True)
        ax.set_ylim([0,1])
        ax.grid()
        plt.show(block=False)
        plt.pause(0.1)
        bg = fig.canvas.copy_from_bbox(fig.bbox)
        # add curves that will be drawn
        ax.draw_artist(ln)
        fig.canvas.blit(fig.bbox)

        while(not flag_blitting_done):
            fig.canvas.restore_region(bg)
            buff.update(random())
            ln.set_ydata(buff.latest())
            ax.draw_artist(ln)
            fig.canvas.blit(fig.bbox)
            fig.canvas.flush_events()
        print('blitting complete')
    run_blitting()


# plot your results ============================================
plt.show()
