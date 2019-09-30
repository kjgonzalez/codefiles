'''
datecreated: 190930
objective: want to use opencv to make some kind of animated plotting tool.
note: using cv2 is MUCH MUCH faster, will use this instead of matplotlib
applications:
    * animated plot
    * live updating
    * user / computer controlled animation

alright, idea:
1. have a object move around in a circle constantly, perpetually
2. show item, updating position
3. also be able to plot static items like walls, etc


steps:
1. have a window with shapes
2. have those shapes move around
3. have those shapes move with tkinter control
4. have those shapes move with computer control

THINGS TO IMPLEMENT
status | want
done   | plot fast-updating (60Hz+) plot area
???    | have a rotating rectangle
???    | use polygons instead of "rect", in custom function
???    | overlay simple image on top of background (deal with alpha)
???    | have item follow a path
???    | be able to control item with keyboard
???    |


'''

# import matplotlib.pyplot as plt
# import matplotlib.animation as ani
import cv2
import time
import numpy as np
RED = (0,0,255) # for use with opencv (BGR)
BLU = (255,0,0)
GRN = (0,255,0)
WHT = (255,255,255)
BLK = (0,0,0)
CVFONT = cv2.FONT_HERSHEY_SIMPLEX
def qs(img,title='CLOSE WITH KEYBOARD'):
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

t0=time.time()

class Timer:
    def __init__(self):
        self.t0=time.time() # start time
    def now(self):
        ''' return time since start of program '''
        return time.time()-self.t0
timer = Timer()
NOW=timer.now

class Kcirc:
    def __init__(self,centerRC,radius,freq=1):
        ''' note: freq in Hz '''
        self.r = centerRC[0]
        self.c = centerRC[1]
        self.radius = radius
        self.freq = 2*np.pi*freq
    def update(self):
        self.r += np.sin(NOW()*self.freq)*self.radius
        self.c += np.cos(NOW()*self.freq)*self.radius
    def get(self):
        self.update()
        return (self.r.astype(int),self.c.astype(int))

center = Kcirc((400,300),1)

while(True):
    # calculate center
    # rest of stuff
    t1=time.time()-t0
    t0=time.time()
    bkgd = np.ones((600,800,3))*255
    # noise = np.random.rand(600,800,3) # remember: (r,c) dimensions
    cv2.putText(bkgd,str(round(t1,3)),(50,30),CVFONT,1,BLU)
    cv2.putText(bkgd,str(round(NOW(),3)),(50,60),CVFONT,1,BLU)
    # temp=center.get()
    # print(temp)
    cv2.circle(bkgd,center.get(),10,BLU)
    cv2.circle(bkgd,(400,300),10,RED)

    # alright, try drawing a rectangle with polygon




    # pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
    pts = pts.reshape((-1,1,2)) # critical for drawing a polygon
    cv2.polylines(bkgd,[pts],True,RED)



    cv2.imshow('frame',bkgd)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
