'''
this is where i'll develop the UI form that can open a music file, edit the
    contents, save, and move to another file.

things to fix:
* control text size in all items with one variable - done
* give root (self.R) window a title - done
* instead of grid, may want to use place - no, using grid. - done
* be able to load one song, edit data, and save it. - done
* prevent saving if no changes made - done
* be able to go to prev / next song in a list - done
* highlight which song is currently loaded in listbox - doesn't really work
* use hotkeys like CTRL+Q for quit - done
===== div: in progress ===========
* switch to a new song by double-clicking on it in listbox (popup: save?)

TODO: if a local config file doesn't exist, set that up with user right away

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
        self.printstate = lambda: print('state:',self.V['autochkCMT'].get())
        self.printindex = lambda: print('selected:',self.I['files'].curselection())
        self.printautotxt = lambda:print('text:',self.V['autoCMT'].get())
        self.printfields = lambda:print(self.getAllFields())
        self.reloadFirst = lambda:self.setAllFromFile(self._filelist[0])
        self._filelist = [ifile for ifile in os.listdir('.') if('mp3' in ifile)]
        self._fields = 'fname title artist album track genre year comment'.split(' ')
        self._current = None # needs to be set at first run
        self.origInfo = None # initialize dict variable for original metadata
        self.R = tk.Tk()
        self.R.resizable(False,False)
        self.R.title('UI Form')
        helv = ft.Font(self.R,family='Helvetica',size=fontSize)
        self.F=tk.Frame(self.R)
        self.F.pack()

        # control variables
        self.V=dict()
        self.V['autochkCMT'] = tk.IntVar() # status for auto-Comment
        self.V['autochkFNM'] = tk.IntVar() # status for auto-Filename
        self.V['autoCMT'] = tk.StringVar() # text for auto-comment
        self.V['autoFNM'] = tk.StringVar() # text for auto-filename
        for ifield in self._fields:
            self.V[ifield] = tk.StringVar()

        # buttons
        self.B = dict() # dictionary of buttons
        self.B['save'] = tk.Button(self.F,font=helv,text='SAVE',command=self.saveData)
        self.B['prev'] = tk.Button(self.F,font=helv,text='PREV',command=self.loadPrevFile)
        self.B['next'] = tk.Button(self.F,font=helv,text='NEXT',command=self.loadNextFile)
        self.B['quit'] = tk.Button(self.F,font=helv,text='QUIT',command=self.quit) # fg='black'

        # checkmarks
        self.C=dict()
        self.C['autochkCMT'] = tk.Checkbutton(self.F,font=helv,text='AutoComment',variable=self.V['autochkCMT'])
        self.C['autochkFNM'] = tk.Checkbutton(self.F,font=helv,text='AutoFilename',variable=self.V['autochkFNM'])

        # entry forms
        self.E=dict()
        for ifield in self._fields:
            self.E[ifield] = tk.Entry(self.F,font=helv,textvariable=self.V[ifield],width=40)
        self.E['autoCMT'] = tk.Entry(self.F,font=helv,textvariable=self.V['autoCMT'])

        # label forms
        self.L=dict()
        for ifield in self._fields:
            self.L[ifield] = tk.Label(self.F,font=helv,text=ifield)
        # self.L['autoFNM'] = tk.Label(self.F,font=helv,textvariable=self.V['autoFNM']) # original
        self.L['autoFNM'] = tk.Label(self.F,font=helv,text='<Artist> - <Title>.mp3')

        # listbox(es)
        self.I=dict()
        self.I['files'] = tk.Listbox(self.F,font=helv,activestyle='dotbox',width=40)

        # placement of all items
        self.B['save'].grid(    row=11,column= 8)
        self.B['prev'].grid(    row=11,column= 9)
        self.B['next'].grid(    row=11,column=10)
        self.B['quit'].grid(    row=11,column=11)
        self.C['autochkCMT'].grid(row= 7,column= 1)
        self.C['autochkFNM'].grid(row= 8,column= 1)
        self.E['fname'].grid(   row= 1,column=8,columnspan=4)
        self.E['title'].grid(   row= 2,column=8,columnspan=4)
        self.E['artist'].grid(  row= 3,column=8,columnspan=4)
        self.E['album'].grid(   row= 4,column=8,columnspan=4)
        self.E['track'].grid(   row= 5,column=8,columnspan=4)
        self.E['genre'].grid(   row= 6,column=8,columnspan=4)
        self.E['year'].grid(    row= 7,column=8,columnspan=4)
        self.E['comment'].grid( row= 8,column=8,columnspan=4)
        self.E['autoCMT'].grid( row= 7,column= 2)
        self.L['autoFNM'].grid( row= 8,column= 2)
        self.L['fname'].grid(   row= 1,column=7)
        self.L['title'].grid(   row= 2,column=7)
        self.L['artist'].grid(  row= 3,column=7)
        self.L['album'].grid(   row= 4,column=7)
        self.L['track'].grid(   row= 5,column=7)
        self.L['genre'].grid(   row= 6,column=7)
        self.L['year'].grid(    row= 7,column=7)
        self.L['comment'].grid( row= 8,column=7)
        self.I['files'].grid(   row= 1,column= 1,rowspan=6,columnspan=2) #,columnspan=3,rowspan=6)

        # bind custom events
        self.E['title'].bind( '<KeyRelease>',self.updateAutoFileName)
        self.E['artist'].bind('<KeyRelease>',self.updateAutoFileName)
        self.R.bind('<Control-s>',self.saveData)
        self.R.bind('<Control-S>',self.saveData)
        self.R.bind('<Control-j>',self.loadPrevFile)
        self.R.bind('<Control-J>',self.loadPrevFile)
        self.R.bind('<Control-k>',self.loadNextFile)
        self.R.bind('<Control-K>',self.loadNextFile)
        self.R.bind('<Control-q>',self.quit)
        self.R.bind('<Control-Q>',self.quit)

    def quit(self,*kargs):
        print('exiting')
        self.F.quit()

    def updateFileList(self):
        self._filelist = [ifile for ifile in os.listdir('.') if('mp3' in ifile)]

    def updateAutoFileName(self,event): # perhaps "tk.Event" ?
        ''' here, will outline the formatting for auto-filenaming, and this
            function is to be used as a callback
        * For now, keeping things just as <Artist> - <Title>
        * want to run this on keypress of artist & title widgets
        '''
        text = '{} - {}.mp3'.format(self.V['artist'].get(),self.V['title'].get())
        self.V['autoFNM'].set(text)

    def populateListBox(self):
        ''' Clears anything in the list box, then populates it with
        items_list.
        '''
        end=max(self.I['files'].size()-1,0) # use max in case no lines
        self.I['files'].delete(0,end)
        for item in self._filelist:
            self.I['files'].insert(tk.END,item) # adds newline

    def setAllFromIndex(self,index):
        ''' given self._filelist, load a given index and update
            self._current
        '''
        self.setAllFromFile(self._filelist[index])
        self._current = index


    def setAllFromFile(self,filename):
        ''' given a filename, populate metadata fields '''
        info = ka.MetaMP3(filename).getAllData()
        # info['fname'] = os.path.splitext(filename)[0] # giving with ext for now
        info['fname'] = filename
        self.origInfo = info # replaces previous data each time a file is loaded
        # first assert all, then start populating
        for ifield in self._fields:
            assert ifield in info.keys(), 'field missing: '+ifield
        for ifield in self._fields:
            self.V[ifield].set(info[ifield])
        self.updateAutoFileName(None) # Needs input argument to run

    def setField(self,field,value):
        assert field in self._fields,'invalid field:'+field
        self.V[field].set(value)

    def getAllFields(self):
        ''' return dict of all fields '''
        res = dict()
        for ifield in self._fields:
            res[ifield]=self.V[ifield].get()

        # override comment if auto-comment enabled
        if(self.V['autochkCMT'].get()):
            # auto-comment enabled, override current comment value
            res['comment'] = self.V['autoCMT'].get()
        # override filename if auto-filename enabled
        if(self.V['autochkFNM'].get()):
            # auto-filename enabled, override current filename.
            res['fname'] = self.V['autoFNM'].get()
        return res

    def saveData(self,*kargs): # kargs needed for callback
        ''' write out the new metadata to file '''
        # case 1: only metadata is changed. save that and quit
        i1 = self.origInfo
        i2 = self.getAllFields()
        diff = {ifield:i1[ifield]!=i2[ifield] for ifield in self._fields}
        ndiff = len([i for i in diff.values() if(i)])

        if(ndiff==0):
            # no diff between i1 and i2, no changes made
            print('no changes')
        elif(ndiff==1 and diff['fname']):
            # only the filename was changed. rename file, update list, update "original" info
            print('only filename change')
            os.rename(i1['fname'],i2['fname'])
            self.updateFileList()
            self.populateListBox()
            self.origInfo=i2
        elif(not diff['fname']):
            # only metadata was changed. update metadata, update "original" info
            print('only metadata change')
            dat = ka.MetaMP3(i2['fname'])
            for ifield in dat.tags:
                dat.set(ifield,i2[ifield])
            dat.save()
            self.origInfo=i2
        else:
            # both filename and metadata changed. rename, update list, change meta, update "original" info
            print('metadata and filename change')
            os.rename(i1['fname'],i2['fname'])
            self.updateFileList()
            self.populateListBox()
            dat = ka.MetaMP3(i2['fname'])
            for ifield in dat.tags:
                dat.set(ifield,i2[ifield])
            dat.save()
            self.origInfo=i2

    def loadNextFile(self,*kargs):
        ''' callback for use with "Next" button. load next file in list. wrap
            around to start of list if at end.
        '''
        ind = self._current+1
        if(ind >=len(self._filelist)):
            ind = 0
        self.setAllFromIndex(ind)

    def loadPrevFile(self,*kargs):
        ''' callback for use with "Prev" button. '''
        ind = self._current - 1
        if(ind <0):
            ind = len(self._filelist)-1
        self.setAllFromIndex(ind)

    def run(self):
        ''' handle initialization of function here '''
        self.populateListBox()

        # run initial loading of metadata
        self.setAllFromIndex(0) # initialize data fields
        self.R.mainloop()
        self.R.destroy()

# kjg190626: ok, for the moment, will run from 00... folder

if(__name__=='__main__'):
    listdir = [ifile for ifile in os.listdir('.') if('mp3' in ifile)]

    main = MainWindow()
    main.run()
