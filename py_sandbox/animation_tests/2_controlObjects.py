'''
datecreated: 191017
objective: control individual objects in the screen

status | descrip
wait   | be able to show one object
????   | control that one object (fwd, bwd, Lturn, Rturn)
????   | show more than one object
????   | control more than one object (one at a time, use drop-down)
????   | spawn new objects?
????   | ?
????   | ?

want to make design roughly like below. emulates a car, with headlights, and arrow pointing direction.

-/\----/\-
|        |
|   /\   |
|        |
|        |
----------

'''

import threading # handling two different sequences at once (getting frames, displaying them)
import tkinter as tk # keyboard control
import cv2, time, argparse
import numpy as np
RED = (0,0,255) # for use with opencv (BGR)
BLU = (255,0,0)
GRN = (0,255,0)
WHT = (255,255,255)
BLK = (0,0,0)
CVFONT = cv2.FONT_HERSHEY_SIMPLEX
IMW=400
IMH=300

def qs(img,title='CLOSE WITH KEYBOARD'):
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def rect2(img, center,dims,angle, color,*kargs):
    ''' Draw a typical rectangle, but at any given angle.
    INPUTS:
    * img: image to draw rectangle on
    * center: center of rectangle, given as (x,y) or (col,row)
    * dims: dimensions of rectangle, given as (w,h)
    * angle: scalar angle of rectangle, given in degrees
    * color: color of rectangle border, given as BGR tuple
    OUTPUT:
    * (None), draws on img

    general steps:
    1. take in parameters
    2. rotate rectangle centered at origin
    3. translate to given spot.

     '''
    xc,yc=center
    w,h=dims
    theta = np.radians(angle)
    c,s=np.cos(theta),np.sin(theta)
    R=np.array([
        [c,-s,0],
        [s,c,0],
        [0,0,1]]) # 3x3
    pts=np.array([
        [-w,h,1],
        [w,h,1],
        [w,-h,1],
        [-w,-h,1],
        [-w,h,1]   ])/2

    # rotate points
    pts2=pts@R
    pts2[:,0]+=xc
    pts2[:,1]+=yc
    pts2=pts2[:,:2].reshape((-1,1,2)).astype(int)
    cv2.polylines(img,[pts2],True,color)

class Timer:
    def __init__(self):
        self.t0=time.time() # start time
        self._lap = time.time()
    def now(self):
        ''' return time since start of program '''
        return time.time()-self.t0
    def lap(self):
        ''' get lap time and reset timer '''
        elapsed = time.time() - self._lap
        self._lap = time.time()
        return elapsed
    def nowLap(self):
        return time.time() - self._lap
class Global:
    def __init__(self):
        self.var=0
gvar = Global()

class KBControl_r1:
    def __init__(self):
        self.R = tk.Tk()
        self.V = tk.StringVar()
        self.V.set('0')        # initial value
        self.a_label = tk.Label(self.R,textvariable = self.V ).pack() # create label object
        self.history = []            # create empty list
        self.v_dir = ''
        self.F = tk.Frame(self.R, width=200, height=200)    #create self.F in main window
        self.F.bind("<KeyPress>", self.keydown)    # bind "keydown" fn to keyPRESS
        self.F.bind("<KeyRelease>", self.keyup)    # bind "keyup" fn to keyRELEASE
        self.F.bind('q',self.quit)
        self.F.pack()            # activate self.F
        self.F.focus_set()        # set self.F in focus

    def keyup(self,e):
        # print e.char        # when a key is un-pressed, print to screen
        if  e.char in self.history :
            self.history.pop(self.history.index(e.char)) #remove it from the list
            # NOTE: LIST IS NOW UPDATED
            self.v_dir = self.direction(self.history)
            gvar.var = self.v_dir
            self.V.set(self.v_dir)    # convert current state of history into string
            # here, would send the updated command to the serial port.

    def keydown(self,e):
        print('pressed')
        if not e.char in self.history :    # if key isn't alrdy in list...
            self.history.append(e.char)    # add key to END(!) of list
            # NOTE: LIST IS NOW UPDATED
            self.v_dir = self.direction(self.history)
            gvar.var = self.v_dir
            self.V.set(self.v_dir)        # convert current state of list into string
            # here, would send updated command to the serial port

    def direction(self,e):
        ''' Take in list of currently pressed keys, return direction. General
            steps:
            1. receive list
            2. check if list has more than two elements
            3. check which two elements active
            4. return direction
            NOTE: keypad:
            1 2 3
            4 5 6
            7 8 9
              0        '''
        if(len(e)==1):
            # only one button pressed
            if('w' in e):
                return '2'                # NORTH
            elif('a' in e):
                return '4'                # WEST
            elif('s' in e):
                return '8'                # SOUTH
            elif('d' in e):
                return '6'                # EAST
            else:
                return '0'
        elif(len(e)==2):
            if('w' in e and 'a' in e):
                return '1'                # NWEST
            elif('w' in e and 'd' in e):
                return '3'                # NEAST
            elif('s' in e and 'a' in e):
                return '7'                # SWEST
            elif('s' in e and 'd' in e):
                return '9'                # SEAST
            else:
                return '0'
        else:
            return '0'

    def quit(self,e):
        self.R.quit()
    def run(self):
        self.R.mainloop()            # activate whole program



class DisplayWindow:
    ''' should be capable of putting everything into a thread '''
    def __init__(self,freq=60,save=False):
        self.xc=IMW/2
        self.yc=IMH/2
        self.w=50
        self.h=100
        self.save=save
        self.freq=freq # synchronize actual framerate and video framerate
        if(save):
            fourcc = cv2.VideoWriter_fourcc(*'XVID')
            self.out = cv2.VideoWriter('output.avi',fourcc,self.freq, (IMW,IMH))

    def writeout(self,frame):
        if(not self.save):
            return None
        # if self.save is True, continue
        self.out.write(frame)
        return None

    def run(self):
        while(True):
            lap = timer.lap()
            bkgd = np.ones((IMH,IMW,3))*255 # follows image format
            cv2.putText(bkgd,str(round(lap,3)),(50,30),CVFONT,1,BLU)
            cv2.putText(bkgd,str(round(timer.now(),3)),(50,60),CVFONT,1,BLU)
            cv2.putText(bkgd,str(gvar.var),(50,90),CVFONT,1,BLU)
            cv2.circle(bkgd,(int(IMW/2),int(IMH/2)),10,GRN)
            rect2(bkgd,(self.xc,self.yc),(self.w,self.h),timer.now()*180,RED)
            pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
            pts = pts.reshape((-1,1,2)) # critical for drawing a polygon
            cv2.imshow("press 'q' to exit",bkgd)
            if(self.save):
                self.out.write(bkgd.astype(np.uint8)) # needs to be uint8 for compatability
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            while(1/self.freq > timer.nowLap()):
                continue # synchronization pause
        if(self.save):
            self.out.release()

if(__name__=='__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--save',default=False,action='store_true',help='save to video file')
    args=p.parse_args()

    timer = Timer()

    dw = DisplayWindow(save=args.save)
    dw.run()
    # kbc = KBControl_r1()
    # #
    # thread_dw=threading.Thread(target=dw.run,daemon=True) # kill this window if tkinter closes
    # thread_dw.start()
    # #
    # #
    # # # print('ready to exit')
    # kbc.run() # tkinter thing, should be final thing to run
