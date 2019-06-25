'''
this is where i'll develop the UI form that can open a music file, edit the
    contents, save, and move to another file.

things to fix:
* control text size in all items with one variable
* have each widget perform its correct function
* be able to load / save all data as needed
* give root (self.R) window a title

'''

import os,sys,time
import tkinter as tk


class MainWindow:
    ''' Class to contain and load main window interface. this only initializes
        window with empty values, member functions are needed to then fill out
        what goes in each place.
    '''

    def __init__(self):
        self.passfn = lambda : print('hello world')
        self.printstate = lambda: print('state:',self.V['autochk'].get())
        self.printindex = lambda: print('selected:',self.I['files'].curselection())
        self.printautotxt = lambda:print('text:',self.V['autotxt'].get())

        self.R = tk.Tk()
        self.R.resizable(False,False)
        self.F=tk.Frame(self.R)
        self.F.pack()

        # control variables
        self.V=dict()
        self.V['autochk'] = tk.IntVar() # for use with C['auto']
        self.V['fname'] = tk.StringVar() # filename
        self.V['title'] = tk.StringVar()
        self.V['artist'] = tk.StringVar()
        self.V['album'] = tk.StringVar()
        self.V['track'] = tk.StringVar()
        self.V['year'] = tk.StringVar()
        self.V['comment'] = tk.StringVar()
        self.V['autotxt'] = tk.StringVar()

        # buttons
        self.B = dict() # dictionary of buttons
        self.B['save'] = tk.Button(self.F,text='SAVE',command=self.getListboxInfo)
        self.B['prev'] = tk.Button(self.F,text='PREV',command=self.printindex)
        self.B['next'] = tk.Button(self.F,text='NEXT',command=self.printautotxt)
        self.B['exit'] = tk.Button(self.F,text='EXIT',command=self.F.quit) # fg='black'

        self.B['save'].grid(row=11,column=3)
        self.B['prev'].grid(row=11,column=6)
        self.B['next'].grid(row=11,column=9)
        self.B['exit'].grid(row=11,column=10)
        # [self.B[key].pack() for key in self.B.keys()]

        # checkmark(s)
        self.C=dict()
        self.C['autochk'] = tk.Checkbutton(self.F,text='autocomment',variable=self.V['autochk'])

        self.C['autochk'].grid(row=6,column=1)
        # [self.C[key].pack() for key in self.C.keys()]

        # entry forms
        self.E=dict()
        self.E['fname'] = tk.Entry(self.F,textvariable=self.V['fname'])
        self.E['title'] = tk.Entry(self.F,textvariable=self.V['title'])
        self.E['artist'] = tk.Entry(self.F,textvariable=self.V['artist'])
        self.E['album'] = tk.Entry(self.F,textvariable=self.V['album'])
        self.E['track'] = tk.Entry(self.F,textvariable=self.V['track'])
        self.E['year'] = tk.Entry(self.F,textvariable=self.V['year'])
        self.E['comment'] = tk.Entry(self.F,textvariable=self.V['comment'])
        self.E['autotxt'] = tk.Entry(self.F,textvariable=self.V['autotxt'])

        self.E['fname'].grid(row=1,column=14)
        self.E['title'].grid(row=2,column=14)
        self.E['artist'].grid(row=3,column=14)
        self.E['album'].grid(row=4,column=14)
        self.E['track'].grid(row=5,column=14)
        self.E['year'].grid(row=6,column=14)
        self.E['comment'].grid(row=7,column=14)
        self.E['autotxt'].grid(row=7,column=1)
        # [self.E[key].pack() for key in self.E.keys()]

        # label forms
        self.L=dict()
        self.L['fname'] = tk.Label(self.F,text='fname')
        self.L['title'] = tk.Label(self.F,text='title')
        self.L['artist'] = tk.Label(self.F,text='artist')
        self.L['album'] = tk.Label(self.F,text='album')
        self.L['track'] = tk.Label(self.F,text='track')
        self.L['year'] = tk.Label(self.F,text='year')
        self.L['comment'] = tk.Label(self.F,text='comment')
        self.L['auto'] = tk.Label(self.F,text='autocomment')

        self.L['fname'].grid(row=1,column=10)
        self.L['title'].grid(row=2,column=10)
        self.L['artist'].grid(row=3,column=10)
        self.L['album'].grid(row=4,column=10)
        self.L['track'].grid(row=5,column=10)
        self.L['year'].grid(row=6,column=10)
        self.L['comment'].grid(row=7,column=10)
        # [self.L[key].pack() for key in self.L.keys()]

        # listbox(es)
        self.I=dict()
        self.I['files'] = tk.Listbox(self.F,activestyle='dotbox')

        self.I['files'].grid(row=1,column=1,columnspan=5,rowspan=4)
        # [self.I[key].pack() for key in self.I.keys()]
    def populateListBox(self,items_list):
        ''' clears anything in the list box, then populates it with
        items_list.
        '''
        end=max(self.I['files'].size()-1,0)
        self.I['files'].delete(0,end)
        for item in items_list:
            self.I['files'].insert(tk.END,item)

    def getListboxInfo(self):
        print('number of lines:',self.I['files'].size())

    def run(self):
        self.R.mainloop()
        self.R.destroy()

main = MainWindow()
main.populateListBox('abcdefghijklmnopqrs')
main.populateListBox('hello')
main.run()
