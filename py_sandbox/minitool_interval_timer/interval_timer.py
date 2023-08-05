'''
goal: basic interval timer that plays a noise every N seconds, can choose if repeats
'''

import time
import tkinter as tk
import tkinter.font as tkFont
from playsound import playsound

sound = '/home/kjg/Downloads/sc2_timer_help/macro_cycle.mp3'

class GUI:
    ''' the very most basic starting gui to help get any project rolling'''
    @staticmethod
    def makeplace(elem,row,col):
        elem.grid(row=row,column=col,sticky='n') # need more later
        return elem

    def __init__(self):
        self.R = tk.Tk()
        self.R.title('Simple Interval Timer')
        self.R.resizable(False,False) # can optionally fix window dimensions
        # self.R.geometry("1000x750") # start at a particular window size
        # self.R.geometry("+10+10") # start at a particular location
        mp = self.makeplace
        font = tkFont.Font(size=20)

        self.lbl = mp(tk.Label(self.R,text='Time [s]',font=font),0,0)
        self.ent:tk.Entry = mp(tk.Entry(self.R,width=10,font=font),1,0)
        self.ent.insert(0,'25')
        self.var_restart = tk.IntVar()
        self.chk_restart = mp(tk.Checkbutton(self.R,text='restart',font=font,variable=self.var_restart),3,0)
        self.btn_run = mp(tk.Button(self.R,text='Run',font=font,command=lambda:self.cb_startstop_timer()),4,0)
        self.lbl_time:tk.Label= mp(tk.Label(self.R,text='00s',font=font),5,0)

        self.R.bind('<q>',lambda x: self.R.quit())

        self.runtimer=False
        self.t0=0

    def cb_startstop_timer(self):
        self.t0 = time.time()
        self.runtimer=not self.runtimer

        if(self.runtimer):
            self.chk_restart.configure(state='disabled')
            self.ent.configure(state='disabled')
            self.btn_run.configure(text='Stop')
        else:
            self.chk_restart.configure(state='normal')
            self.ent.configure(state='normal')
            self.btn_run.configure(text='Run')

        self.update()

    def update(self):
        maxtime = int(self.ent.get())
        restart = self.var_restart.get()
        if(self.runtimer==False): return None
        dt = int(time.time()-self.t0)
        self.lbl_time.configure(text=f'{dt:0>2d}s')
        if(dt>=maxtime):
            playsound(sound,False)
            if(restart): self.t0=time.time()
            else: self.cb_startstop_timer()
        self.lbl_time.after(100,self.update)

    def run(self):
        self.R.mainloop() # vital for each and every tkinter function


if(__name__ == '__main__'):
    GUI().run()

# eof
