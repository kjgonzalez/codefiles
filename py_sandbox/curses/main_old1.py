import sys,os
import curses
KEY_ENTER = 10
def constrain(val,vmin,vmax): return min(max(vmin,val),vmax)

class Widget:
    def __init__(self,text,loc_rc):
        self.text=text
        self.loc=loc_rc
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
    def addop(self,yloc,text:str):
        self.scr.addstr(yloc,self.xoff,'> '+text)
    def addBtn(self,text:str,callback):
        # add "button"
        pass
    def addEnt(self,text:str):
        # add "entry". be able to handle when cursor over element. 
        pass
    def addLbl(self,text:str):
        # add "label". be able to handle when text is modified
        pass

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
        addop = self.addop
        nums=list(range(48,58))
        alphas=list(range(65,123))
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
            
            # render basic text
            #titlebar = f"{self.title} | Pos: ({cursor_y},{self.xoff}) | 'q' to quit"
            titlebar = f"{self.title} | '{self.quitkey}' to quit"
            addstr(0,0,titlebar)
            addstr(cmin-1,0,'- Options ------')
            cmax=self.cmin
            addop(cmax,'RETURN')
            cmax+=1
            for iop in istate:
                addop(cmax,iop[0])
                cmax+=1
            cmax-=1
            addstr(cmax+1,0,'-'*10)
            # render results of user operation
            stdscr.move(cursor_y, self.xoff)
            #stdscr.move(*self.loc)
            k = stdscr.getch() #wait for input

    def run(self):
        # actually run class and get results
        curses.wrapper(self.main)


if __name__ == "__main__":
    Curse_Boiler().run()
