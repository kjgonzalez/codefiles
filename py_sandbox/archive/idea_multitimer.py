'''
datecreated: 190830
objective: mock-up of talker timer
goal is to track how much each person talks in critical role podcast

General Steps:
1. get a ui
2. have labels
3. have the active timer going
4. have a total timer
5. be able to export

'''

import tkinter as tk
import time
import numpy as np

# for python 3.x use 'tkinter' rather than 'Tkinter'

class MainWindow():
    def __init__(self):
        self.r = tk.Tk()
        self.f=tk.Frame(self.r)
        self.f.pack()
        # names
        names='dmself dmchar vax vex grog scanlan percy kiki none'.split(' ')
        alts ='q,a,w,e,r,s,d,f, '.split(',')
        self.n={alts[i]:names[i] for i in range(len(alts))}
        self.names=names[:-1]
        self.target='none'

        # control variables
        self.v=dict()
        for iname in names:
            self.v[iname]=tk.DoubleVar()
        self.v['total']=tk.DoubleVar()

        # label forms
        self.l=dict()
        for iname in names:
            self.l[iname]=tk.Label(self.f,textvariable=self.v[iname])
            self.l['_'+iname]=tk.Label(self.f,text=iname)
        self.l['_total']=tk.Label(self.f,text='total')
        self.l['total']=tk.Label(self.f,textvariable=self.v['total'])
        self.l['spacer']=tk.Label(self.f,text=' '*100)
        self.l['_total'].configure(font=('Helvetica', 10, 'bold'))
        self.l['_total'].configure(font=('Helvetica', 10, ''))

        # initialize variables
        for iname in names:
            self.v[iname].set(0)

        for i,iname in enumerate(names):
            self.l['_'+iname].grid(row=i,column=0)
            self.l[iname].grid(    row=i,column=1)
        self.l['_total'].grid(row=20,column=0)
        self.l['total'].grid(row=20,column=1)
        self.l['spacer'].grid(row=21,column=1)

        # need one for each person, plus a stop
        self.r.bind('q',lambda event:self.focus('q'))
        self.r.bind('w',lambda event:self.focus('w'))
        self.r.bind('e',lambda event:self.focus('e'))
        self.r.bind('r',lambda event:self.focus('r'))
        self.r.bind('a',lambda event:self.focus('a'))
        self.r.bind('s',lambda event:self.focus('s'))
        self.r.bind('d',lambda event:self.focus('d'))
        self.r.bind('f',lambda event:self.focus('f'))
        self.r.bind('<space>',lambda event:self.focus(' '))
        self.r.bind('<Control-q>',self.quit)

    def run(self):
        self.updater()
        self.r.mainloop()

    def focus(self,key):
        ''' given a certain key, change focus '''
        self.target=self.n[key]
        # change look of the label and ensure others are to original look
        for iname in self.names:
            self.l[iname].configure(font=('Helvetica', 10, ''))
            self.l['_'+iname].configure(font=('Helvetica', 10, ''))
        if(self.target!='none'):
            self.l[self.target].configure(font=('Helvetica', 10, 'bold'))
            self.l['_'+self.target].configure(font=('Helvetica', 10, 'bold'))

    def updater(self,event=None):
        if(self.target!='none'):
            self.v[self.target].set(self.v[self.target].get()+0.1)
        self.v['total'].set(sum([self.v[iname].get() for iname in self.names]))
        self.r.after(100,self.updater) # time in milliseconds

    def quit(self,event):
        self.f.quit()

# r.destroy()
obj=MainWindow()
obj.run()




# eof
