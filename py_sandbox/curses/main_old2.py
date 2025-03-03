import sys,os
import curses
KEY_ENTER = 10
def constrain(val,vmin,vmax): return min(max(vmin,val),vmax)

class Widget:
    def __init__(self,text,loc_rc,wtype='lbl',callback=None):
        self.text=text
        self.loc=loc_rc
        self.sel_rc=None
        assert wtype in 'btn lbl ent'.split(' '),f"invalid type: {wtype}"
        self.type=wtype
        self.cb=callback
        if(wtype=='btn'):
            self.text='> '+text
            self.sel_rc=loc_rc
        if(wtype=='ent'):
            r = loc_rc[0]
            c = loc_rc[1]+1+len(text)
            self.sel_rc = r,c
    def set(self,newtext):
        self.text=newtext
    def draw(self,scr):
        scr.addstr(*self.loc,self.text)
    

class Curse_Boiler:
    def __init__(self): 
        ''' basics to get the class going '''
        self.scr = None
        self.quitkey='\\'
        self.title = 'Program Name'
        self.cmin=2
        self.xoff=2 # basic offset of all options
        self.loc=(self.cmin,self.xoff)
        pp=self.pprint
        self.states={
                0:[
                    ['test1',lambda:pp('hi1')],
                    ['test2',lambda:pp('hi2')],
                    ['test3',lambda:pp('hi3')],
                    ['ch_1',lambda:self.setst(1)]
                  ],
                1:[['testz',lambda:pp('hiZ')]]
                    }
        self.sinds=[0]
    def pprint(self,text,row=10):
        self.scr.addstr(row,self.xoff,text)

    def prest(self):
        if(len(self.sinds)>1):
            self.sinds.pop(-1)
        self.loc=(self.cmin,self.xoff)
    def setst(self,state): 
        self.sinds.append(state)
        self.loc=(self.cmin,self.xoff)
        self.pprint(f'change state: {state}')
    def main(self,stdscr):
        # main setup ---------
        self.scr = stdscr
        k = 0
        cmin = self.cmin
        cursor_y = cmin
        stdscr.clear() # start w/ blank canvas
        stdscr.refresh()
        addstr=stdscr.addstr
        #addop = self.addop
        nums=list(range(48,58))
        alphas=list(range(65,123))
        pp = self.pprint
        # main loop ------------------
        while (k != ord(self.quitkey)):
            # Initialization, process user input
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            if k == curses.KEY_DOWN: cursor_y = constrain(cursor_y + 1,cmin,cmax)
            elif k == curses.KEY_UP: cursor_y = constrain(cursor_y - 1,cmin,cmax)
            elif(k == KEY_ENTER and cursor_y==cmin):
                # return to prev state
                self.prest()
                cursor_y = cmin
            elif k == KEY_ENTER: 
                #addstr(10,2,'enter pressed')
                yprev=self.sinds[-1]
                istate=self.states[self.sinds[-1]]
                ifn=istate[cursor_y-cmin-1][1]
                ifn()
                if(yprev!=self.sinds[-1]):
                    cursor_y =cmin
            #elif(k in alphas+nums):
            #else:
            elif(k in alphas+nums):
                self.pprint(f'{nums}')
                self.pprint(f'{k}',11)
            # process change of state
            istate=self.states[self.sinds[-1]]
            titlebar = f"{self.title} | '{self.quitkey}' to quit"
            
            widgets=[]
            #def __init__(self,text,loc_rc,wtype='lbl',callback=None):
            widgets.append(Widget(titlebar,(0,0)))
            widgets.append(Widget('- Options ---',(cmin-1,0)))
            cmax=self.cmin # cmin=2
            widgets.append(Widget('RETURN',(cmax,self.xoff),'btn',self.prest))
            cmax+=1
            widgets.append(Widget('hi1',(cmax,self.xoff),'btn',lambda:pp('hi1')))
            #for iop in istate:
            #    addop(cmax,iop[0])
            #    cmax+=1
            #cmax-=1
            #addstr(cmax+1,0,'-'*10)
            widgets.append(Widget('-'*10,(cmax+1,0)))


            # render
            for iw in widgets:
                iw.draw(stdscr)
            stdscr.move(cursor_y, self.xoff)
            #stdscr.move(*self.loc)
            k = stdscr.getch() #wait for input

    def run(self):
        # actually run class and get results
        curses.wrapper(self.main)


if __name__ == "__main__":
    Curse_Boiler().run()
