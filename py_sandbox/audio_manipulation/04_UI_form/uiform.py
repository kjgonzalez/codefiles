'''
this is where i'll develop the UI form that can open a music file, edit the
    contents, save, and move to another file.

things to fix:
* control text size in all items with one variable - done
* give root (self.R) window a title - done
* instead of grid, may want to use place - no, using grid. - done

* be able to load one song, edit data, and save it.
* be able to go to prev / next song in a list
* display which song is currently loaded in listbox
* switch to a new song by clicking on it in listbox
* use hotkeys like CTRL+Q for quit
'''

import os,sys,time
import tkinter as tk
from tkinter import font as ft
fontSize = 12 # default font size is 9
import kaudio as ka


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
        self.printfields = lambda:print(self.getAllFields())
        self._fields = 'fname title artist album track genre year comment'.split(' ')
        self.R = tk.Tk()
        self.R.resizable(False,False)
        self.R.title('UI Form')
        helv = ft.Font(self.R,family='Helvetica',size=fontSize)

        self.F=tk.Frame(self.R)
        self.F.pack()

        # control variables
        self.V=dict()
        self.V['autochk'] = tk.IntVar() # for use with C['auto']
        self.V['autotxt'] = tk.StringVar()
        for ifield in self._fields:
            self.V[ifield] = tk.StringVar()

        # buttons
        self.B = dict() # dictionary of buttons
        self.B['save'] = tk.Button(self.F,font=helv,text='SAVE',command=self.printfields)
        self.B['prev'] = tk.Button(self.F,font=helv,text='PREV',command=self.passfn)
        self.B['next'] = tk.Button(self.F,font=helv,text='NEXT',command=self.passfn)
        self.B['exit'] = tk.Button(self.F,font=helv,text='EXIT',command=self.F.quit) # fg='black'


        # checkmark(s)
        self.C=dict()
        self.C['autochk'] = tk.Checkbutton(self.F,font=helv,text='autocomment',variable=self.V['autochk'])


        # entry forms
        self.E=dict()
        for ifield in self._fields:
            self.E[ifield] = tk.Entry(self.F,font=helv,textvariable=self.V[ifield],width=40)
        self.E['autotxt'] = tk.Entry(self.F,font=helv,textvariable=self.V['autotxt'])



        # label forms
        self.L=dict()
        for ifield in self._fields:
            self.L[ifield] = tk.Label(self.F,font=helv,text=ifield)
        self.L['auto'] = tk.Label(self.F,font=helv,text='autocomment')

        # listbox(es)
        self.I=dict()
        self.I['files'] = tk.Listbox(self.F,font=helv,activestyle='dotbox',width=40)

        # placement of all items
        self.B['save'].grid(    row=11,column= 8)
        self.B['prev'].grid(    row=11,column= 9)
        self.B['next'].grid(    row=11,column=10)
        self.B['exit'].grid(    row=11,column=11)
        self.C['autochk'].grid( row= 7,column= 1)
        self.E['fname'].grid(   row= 1,column=8,columnspan=4)
        self.E['title'].grid(   row= 2,column=8,columnspan=4)
        self.E['artist'].grid(  row= 3,column=8,columnspan=4)
        self.E['album'].grid(   row= 4,column=8,columnspan=4)
        self.E['track'].grid(   row= 5,column=8,columnspan=4)
        self.E['genre'].grid(   row= 6,column=8,columnspan=4)
        self.E['year'].grid(    row= 7,column=8,columnspan=4)
        self.E['comment'].grid( row= 8,column=8,columnspan=4)
        self.E['autotxt'].grid( row= 7,column= 2)
        self.L['fname'].grid(   row= 1,column=7)
        self.L['title'].grid(   row= 2,column=7)
        self.L['artist'].grid(  row= 3,column=7)
        self.L['album'].grid(   row= 4,column=7)
        self.L['track'].grid(   row= 5,column=7)
        self.L['genre'].grid(   row= 6,column=7)
        self.L['year'].grid(    row= 7,column=7)
        self.L['comment'].grid( row= 8,column=7)
        self.I['files'].grid(   row= 1,column= 1,rowspan=6,columnspan=2) #,columnspan=3,rowspan=6)

    def populateListBox(self,items_list):
        ''' Clears anything in the list box, then populates it with
        items_list.
        '''
        end=max(self.I['files'].size()-1,0) # use max in case no lines
        self.I['files'].delete(0,end)
        for item in items_list:
            self.I['files'].insert(tk.END,item) # adds newline

    def setAllFromFile(self,filename):
        ''' given a filename, populate metadata fields '''
        info = ka.MetaMP3(filename).getAllData()
        info['fname'] = filename
        self.setAllFromDict(info)

    def setAllFromDict(self,info_dict):
        ''' Given a dict of info, repopulate the fields in the window
        '''
        # first assert all, then start populating
        for ifield in self._fields:
            assert ifield in info_dict.keys(), 'field missing: '+ifield

        for ifield in self._fields:
            self.V[ifield].set(info_dict[ifield])

    def setField(self,field,value):
        assert field in self._fields,'invalid field:'+field
        self.V[field].set(value)

    def getAllFields(self):
        ''' return dict of all fields '''
        res = dict()
        for ifield in self._fields:
            res[ifield]=self.V[ifield].get()

        # override comment if autocomment enabled
        if(self.V['autochk'].get()):
            # autocomment enabled, override current comment value
            res['comment'] = self.V['autotxt'].get()
        return res

    def run(self):
        self.R.mainloop()
        self.R.destroy()


# print(os.getcwd())

# kjg190626: ok, for the moment, will run from 00... folder

listdir = [ifile for ifile in os.listdir('.') if('mp3' in ifile)]
print(listdir)



main = MainWindow()
main.populateListBox(listdir)


# x = ka.MetaMP3(listdir[0]).getAllData()
# x['fname'] = listdir[0]
# main.setAllFromDict(x)
main.setAllFromFile(listdir[0])
main.run()
