'''
datecreated: 190930
objective: want to use opencv to make some kind of animated plotting tool.
KJG190930: using cv2 is MUCH MUCH faster, will use this instead of matplotlib
KJG190930: at this point, will use tkinter to try and control the rectangle
KJG191001: tkinter now functional, with multi-key input. now capable of having
    high-quality graphing window along with manual input control

applications:
    * animated plot
    * live updating
    * user / computer controlled animation
    * computer controlled demo

THINGS TO IMPLEMENT
status | description
done   | plot fast-updating (60Hz+) plot area
done   | have a rotating rectangle
done   | use polygons instead of "rect", in custom function
done   | be able to control item with keyboard (one key)


'''

import threading # handling two different sequences at once (getting frames, displaying them)
import tkinter as tk # keyboard control
import cv2
import time
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
    ''' general steps:
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
    cv2.polylines(img,[pts2],True,RED)

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
class Global:
    def __init__(self):
        self.var=0
gvar = Global()

class KBControl_r0:
    def __init__(self):
        ''' user note: tkinter should only be used in main thread and has issues
            working with threading module. do not put this class in separate
            thread
        src: https://stackoverflow.com/questions/45799121/runtimeerror-calling-tcl-from-different-appartment-tkinter-and-threading
        '''
        self.R = tk.Tk()
        self.F = tk.Frame(self.R, width=100, height=100)
        self.F.bind('a',self.leftKey)
        self.F.bind('d',self.rightKey)
        self.F.bind('q',self.quit)
        self.F.focus_set()
        self.F.pack()
        self.var_dir=tk.IntVar()

    def getstatus(self):
        print('value:',self.var_dir.get()) # may simplify later

    def leftKey(self,event):
        self.var_dir.set(0)
        gvar.var = 0


    def rightKey(self,event):
        self.var_dir.set(1)
        gvar.var = 1

    def quit(self,event):
        self.R.quit()
    def run(self):
        self.R.mainloop()

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
    def __init__(self):
        self.xc=IMW/2
        self.yc=IMH/2
        self.w=50
        self.h=100
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
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

timer = Timer()

dw = DisplayWindow()
kbc = KBControl_r1()
#
thread_dw=threading.Thread(target=dw.run,daemon=True) # kill this window if tkinter closes
thread_dw.start()
#
#
# # print('ready to exit')
kbc.run() # tkinter thing, should be final thing to run
