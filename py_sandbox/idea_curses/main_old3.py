'''
goal: make easiest possible curses example that is also extendable. 

todo simplify
todo change order of operation (draw, input, update)
todo make widget class?

# what is typical order of operations?
  delete, draw (with reaction)
  wait for input
  if just display something, show on screen...



typical appearance: 

program name
- options --------
 > RETURN
 > btn1...
 > btn2...
 [X] radio1
 [ ] radio2
 entry1: ____
 entry2: ____
 > enter...
 # LBL info

------------------

(end)

# wait, don't specify as text... just specify like tkinter
frame = one view
in a frame goes each thing

need widget types:
    Root - handles everything as "TUI" (textual user interface)
    frame
    button
    label
    entry
    radio

each widget should have:
    initialization
    formatting / appearance
    draw fn
    get?
    draw location(top rc)
    draw height
    allowable cursor locations
    what to do when cursor inside area

make a frame, show it. make a button, let it change states. a state is a frame
change frames.

class TUI(Root):
    def __init__():
        super().__init__(title)
        frm0 = Frm()
        


self.frm0 = Frm() # container
self.addframe(self.frm0) # creates each visible frame. 
self.btn_hi = Btn(self.frm0,text='say hi',callback=self.blah)
self.lbl_stat = Lbl(self.frm0,text='hi')
self.ent_name = Ent(self.frm0,text='name:')
self.rdo_setting = Rdo(self.frm1,texts='one two three'.split(' '))



'''

import sys,os
import curses
KEY_ENTER = 10
nums=list(range(48,58))
alphas=list(range(65,123))

def constrain(val,vmin,vmax): return min(max(vmin,val),vmax)




class CursorLocation:
    def __init__(self,row,col,limL=None,limU=None):
        self.r=row
        self.c=col
        self.rL=limL
        self.rU=limU
    @property
    def loc(self): return self.r,self.c
    @loc.setter
    def loc(self,tuple_rc): self.r,self.c = tuple_rc
    @property
    def havelims(self):
        return self.rL is not None and self.rU is not None
    def __repr__(self): return f'({self.r},{self.c})'
    def dec1(self): 
        if(self.havelims): self.r = constrain(self.r-1,self.rL,self.rU)
        else: self.r-=1
        return self.loc
    def inc1(self): 
        if(self.havelims): self.r = constrain(self.r+1,self.rL,self.rU)
        else: self.r+=1
        return self.loc

class Widget:
    def __init__(self):
        pass

class Frm(Widget):
    def __init__(self,scr):
        self.wlist=[]
        self.wlocs=[0]
        self.clocs=[]
        self.scr=scr
    def draw(self):
        for iw in self.wlist:
            iw.draw()
    def addelem(self,widget):
        self.wlist.append(widget)
        self.wlocs.append(self.wlocs[-1]+widget.height) # height for next widget
        self.clocs+=widget.clocs # allowable locs
    @property
    def height(self):
        self.wlocs[-1]
class TUI:
    def __init__(self,title='Name',quitkey='\\'): 
        ''' basics to get the class going '''
        self.scr = None
        self.title = title
        self.quitkey=quitkey
        self.titlebar=f'{self.title} | quitkey: "{self.quitkey}"'
        self.optionbar = '- Options ----------'
        self.curmin=2 # minimum cursor location (highest point)
        self.cl=CursorLocation(self.curmin,0,self.curmin,self.curmin)
    def pprint(self,text,row=10):
        self.scr.addstr(row,0,text)
    def drawframe(self):
        ''' assume already cleared. draw each element. update allowable cursor locations '''

    def main(self,stdscr):
        # main setup ---------
        self.scr = stdscr
        k = 0 # result of keypress
        cmin = self.curmin
        cmax = cmin+1
        stdscr.clear() # start w/ blank canvas
        #stdscr.refresh()
        addstr=stdscr.addstr
        pp = self.pprint
        # main loop ------------------
        while (k != ord(self.quitkey)):
            # redraw 
            #H, W = stdscr.getmaxyx()
            addstr(0,0,self.titlebar) # should be start of interface
            addstr(1,0,'- options --')
            addstr(2,0,'> op1')
            addstr(3,0,'> op2')
            addstr(4,0,'------------') # should be end of interface
            stdscr.move(*self.cl.loc)
            self.cl.rU=cmax
            # scr.addstr(*self.loc,self.text)
            # get input
            k = stdscr.getch() #wait for input
            # process input
            stdscr.clear()
            if k == curses.KEY_DOWN: self.cl.inc1()
            elif k == curses.KEY_UP: self.cl.dec1() 

    def run(self):
        # actually run class and get results
        curses.wrapper(self.main)


if __name__ == "__main__":
    #print('hello')
    TUI().run()

