'''
datecreated: 190930
objective: want to use matplotlib to make some kind of animated plotting tool.

conclusion: using matplotlib is not very good. will try opencv
applications:
    * animated plot
    * live updating
    * user / computer controlled animation

alright, idea:
1. have a ball move around in a circle constantly, perpetually
2. matplot lib to show item, updating position
3. also be able to plot static items

'''

import matplotlib.pyplot as plt
import matplotlib.animation as ani
import time
import numpy as np
#
# class Car:
#     def __init__(self,initcoord):
#         self.x = initcoord[0]
#         self.y = initcoord[1]
#     def update(self,coord):
#         ''' give new coordinates for the car to be '''
#
#
#
# def anim()

# car = Car([1,1])

fig = plt.figure()
p = fig.add_subplot(1,1,1)


class Elapsed:
    def __init__(self):
        self.t0=time.time()
    def now(self):
        return time.time()-self.t0
timer=Elapsed()
now=timer.now
t=0

x=0
y=0

def animate(*kargs):
    x=np.cos([now(),now()-0.1])
    y=np.sin([now(),now()-0.1])

    p.clear()
    p.plot(x,y,'k-')
    p.set_xlim(-3,3)
    p.set_ylim(-3,3)


ani = ani.FuncAnimation(fig, animate, interval=100)
plt.show()
