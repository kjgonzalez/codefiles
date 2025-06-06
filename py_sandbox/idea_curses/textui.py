'''
goal: make easiest possible curses example that is also extendable. 

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

---
k250606: how bout letting the cursor go effectivelly anywhere except top row, 
  and then tracking where the user types or presses ENTER?


'''

import sys,os
import curses
KEY_ENTER = 10
nums=list(range(48,58))
alphas=list(range(65,123))

def constrain(val,vmin,vmax): return min(max(vmin,val),vmax)


class Color:
    def __init__(self):
        curses.start_color()
        curses.init_pair(7,curses.COLOR_WHITE,curses.COLOR_BLACK)
        curses.init_pair(1,curses.COLOR_RED,curses.COLOR_BLACK)
        curses.init_pair(2,curses.COLOR_GREEN,curses.COLOR_BLACK)
        curses.init_pair(3,curses.COLOR_BLUE,curses.COLOR_BLACK)
        curses.init_pair(4,curses.COLOR_YELLOW,curses.COLOR_BLACK)
        curses.init_pair(5,curses.COLOR_CYAN,curses.COLOR_BLACK)
        curses.init_pair(6,curses.COLOR_MAGENTA,curses.COLOR_BLACK)
    @property
    def WHT(self): return curses.color_pair(7)
    @property
    def RED(self): return curses.color_pair(1)
    @property
    def GRN(self): return curses.color_pair(2)
    @property
    def BLU(self): return curses.color_pair(3)
    @property
    def YEL(self): return curses.color_pair(4)
    @property
    def CYN(self): return curses.color_pair(5)
    @property
    def MAG(self): return curses.color_pair(6)




class Cursor:
    # todo: allow not having any limits?
    def __init__(self):
        self.r,self.c=0,0
        self.rlim=(0,1)
        self.clim=(0,1)
    def init(self,limsrow:tuple,limscol:tuple):
        ''' can only initialize after TUI has scr object '''
        self.setLimits(limsrow,limscol)
        self.r = limsrow[0]
        self.c = limscol[0]
    def setLimits(self,limsrow:tuple,limscol:tuple):
        assert len(limsrow)==2,"row limits need two values"
        assert limsrow[0]<limsrow[1],"row limit error"
        assert len(limscol)==2,"col limits need two values"
        assert limscol[0]<limscol[1],"col limit error"
        self.rlim=limsrow
        self.clim=limscol
    @property
    def loc(self): return self.r,self.c
    def mvu(self): self.r = constrain(self.r-1,*self.rlim) # visual up
    def mvd(self): self.r = constrain(self.r+1,*self.rlim) # visual down
    def mvl(self): self.c = constrain(self.c-1,*self.clim)
    def mvr(self): self.c = constrain(self.c+1,*self.clim)

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


class twidget:
    def __init__(self,row,col):
        self.r=row
        self.c=col



class TUI:
    def __init__(self,title='Name',quitkey='\\'): 
        ''' basics to get the class going '''
        self.scr = None
        self._lastkey=0
        self.quitkey=quitkey
        self._titlestr=title
        self._title_cur=True
        self._title_prs=True
        self._title_lim=False
        #self.optionbar = '- Options ----------'
        self.curmin=1 # minimum cursor location (highest point)
        #self.cl=CursorLocation(1,0,self.curmin,self.curmin)
        self.cl=Cursor()
    def pprint(self,text,row=10):
        self.scr.addstr(row,0,text)

    def configTitleBar(self,title="TUI Title",quitkey='\\',cursorloc=True,
                       lastpress=True,limits=False):
        self._titlestr=title
        self.quitkey=quitkey
        self._title_cur=cursorloc
        self._title_prs=lastpress
        self._title_lim=limits

    def _getTitle(self):
        return f"{self._titlestr} | " + \
               f"quit:\"{self.quitkey}\" " + \
               (f"| rlim{self.cl.rlim},clim{self.cl.clim}" if(self._title_lim) else "") + \
               (f"| loc{self.cursorLoc}" if(self._title_cur) else "") + \
               (f"| last:{self.lastKey}" if(self._title_prs) else "")
    @property
    def screenDims(self):
        ht,wd=self.scr.getmaxyx()
        return (ht-1,wd-1)
    @property
    def cursorLoc(self):
        return self.cl.loc
    @property
    def lastKey(self):
        return self._lastkey
    def main(self,stdscr):
        # main setup ---------
        self.scr = stdscr
        cmin = self.curmin
        cmax = cmin+1
        stdscr.clear() # start w/ blank canvas
        self.cl.init(*zip((1,0),self.screenDims))
        #stdscr.refresh()
        addstr=stdscr.addstr
        pp = self.pprint
        clr = Color()
        # main loop ------------------
        while (self._lastkey != ord(self.quitkey)):
            # redraw 
            addstr(0,0,self._getTitle()) # should be start of interfacea
            addstr(1,1,"text",clr.WHT)
            addstr(2,1,"text",clr.RED)
            addstr(3,1,"text",clr.GRN)
            addstr(4,1,"text",clr.BLU)
            addstr(5,1,"text",clr.YEL)
            addstr(6,1,"text",clr.CYN)
            addstr(7,1,"text",clr.MAG)
            stdscr.move(*self.cl.loc)
            # input get/process
            self._lastkey = stdscr.getch() #wait for input
            stdscr.clear()
            if(self._lastkey==ord(self.quitkey)): pass
            elif(self._lastkey==curses.KEY_DOWN): self.cl.mvd()
            elif(self._lastkey==curses.KEY_UP):   self.cl.mvu()
            elif(self._lastkey==curses.KEY_LEFT): self.cl.mvl()
            elif(self._lastkey==curses.KEY_RIGHT):self.cl.mvr()

    def run(self):
        # actually run class and get results
        curses.wrapper(self.main)


if __name__ == "__main__":
    #print('hello')
    tui=TUI()
    tui.configTitleBar("My TUI",quitkey='q')
    #tui.addElem(
    tui.run()

