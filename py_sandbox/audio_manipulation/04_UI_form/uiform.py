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

TODO: update listbox highlight when click "next" or "previous"
TODO: load from double-clicking listbox
TODO: be able to clear metadata that isn't listed
TODO: make a status line with label

'''

import os,sys,time
import tkinter as tk
from tkinter import font as ft
from tkinter import filedialog
import kaudio as ka
import json
fontSize = 12 # default font size is 9

def clean_string(input):
    ''' remove disallowed characters from title string so it can be used in filename '''
    res = input+''
    disallowed = '/\:*?"<>|¿'
    for i in disallowed:
        res = res.replace(i,'')
    res = res.replace('  ',' ')
    return res

class MainWindow:
    ''' Class to contain and load main window interface. this only initializes
        window with empty values, member functions are needed to then fill out
        what goes in each place.
    '''

    def __init__(self):

        if(not os.path.exists('config.json')):
            print('first time setup')
            root = tk.Tk()
            root.withdraw()
            tempdir = filedialog.askdirectory(parent=root, initialdir=os.getcwd(),
                                              title='Please select a music directory')
            if(tempdir == ''):
                raise Exception('failed to give valid location')
            d = {'path': tempdir}
            with open('config.json', 'w') as fout:
                json.dump(d, fout, indent=1)
        with open('config.json') as f:
            dat = json.load(f)

        self._targpath = dat['path']
        print(self._targpath)
        self.passfn = lambda : print('hello world')
        self.printstate = lambda: print('state:',self.V['autochkCMT'].get())
        self.printindex = lambda: print('selected:',self.I['files'].curselection())
        self.printautotxt = lambda:print('text:',self.V['autoCMT'].get())
        self.printfields = lambda:print(self.getAllFields())
        self.reloadFirst = lambda:self.setAllFromFile(self._filelist[0])
        self._filelist = None
        self.updateFileList()
        self._fields = 'fname title artist album track genre year comment'.split(' ')
        self._current = None # needs to be set at first run
        self.origInfo = None # initialize dict variable for original metadata
        self.R = tk.Tk()
        self.R.resizable(True,False)
        self.R.title('UI Form')
        helv = ft.Font(self.R,family='Helvetica',size=fontSize)
        self.F=tk.Frame(self.R)
        self.F.pack()
        self._prev_info = dict()

        # control variables
        self.V = dict()
        self.V['autochkCMT'] = tk.IntVar() # status for auto-Comment
        self.V['autochkFNM'] = tk.IntVar(value=1) # status for auto-Filename
        self.V['autoCMT'] = tk.StringVar() # text for auto-comment
        self.V['autoFNM'] = tk.StringVar() # text for auto-filename
        for ifield in self._fields:
            self.V[ifield] = tk.StringVar()

        # buttons
        self.B = dict() # dictionary of buttons
        self.B['path'] = tk.Button(self.F,font=helv,text='newpath',command=self.update_config_path)
        self.B['fill'] = tk.Button(self.F,font=helv,text='FILL',command=self.fill_old_data)
        self.B['save'] = tk.Button(self.F,font=helv,text='SAVE',command=self.saveData)
        self.B['prev'] = tk.Button(self.F,font=helv,text='PREV',command=self.loadPrevFile)
        self.B['next'] = tk.Button(self.F,font=helv,text='NEXT',command=self.loadNextFile)
        self.B['quit'] = tk.Button(self.F,font=helv,text='QUIT',command=self.quit) # fg='black'

        # checkmarks
        self.C = dict()
        self.C['autochkCMT'] = tk.Checkbutton(self.F,font=helv,text='AutoComment',variable=self.V['autochkCMT'])
        self.C['autochkFNM'] = tk.Checkbutton(self.F,font=helv,text='AutoFilename',variable=self.V['autochkFNM'])

        # entry forms
        self.E = dict()
        for ifield in self._fields:
            self.E[ifield] = tk.Entry(self.F,font=helv,textvariable=self.V[ifield],width=80)
        self.E['autoCMT'] = tk.Entry(self.F,font=helv,textvariable=self.V['autoCMT'])

        # label forms
        self.L = dict()
        for ifield in self._fields:
            self.L[ifield] = tk.Label(self.F,font=helv,text=ifield)
        self.L['autoFNM'] = tk.Label(self.F,font=helv,text='<track> <artist> - <title>.mp3')

        # listbox(es)
        self.I = dict()
        self.I['files'] = tk.Listbox(self.F,font=helv,activestyle='dotbox',width=80)

        # placement of all items
        self.I['files'].grid(row=1, column=1, rowspan=6, columnspan=10)  # ,columnspan=3,rowspan=6)
        self.C['autochkCMT'].grid(row=7, column=1)
        self.E['autoCMT'].grid(row=7, column=2)
        self.C['autochkFNM'].grid(row=8, column=1)
        self.L['autoFNM'].grid(row=8, column=2)

        self.L['fname'].grid(   row= 9, column=1)
        self.E['fname'].grid(   row= 9, column=2,columnspan=10)
        self.L['title'].grid(   row= 10,column=1)
        self.E['title'].grid(   row= 10,column=2,columnspan=10)
        self.L['artist'].grid(  row= 11,column=1)
        self.E['artist'].grid(  row= 11,column=2,columnspan=10)
        self.L['album'].grid(   row= 12,column=1)
        self.E['album'].grid(   row= 12,column=2,columnspan=10)
        self.L['track'].grid(   row= 13,column=1)
        self.E['track'].grid(   row= 13,column=2,columnspan=10)
        self.L['genre'].grid(   row= 14,column=1)
        self.E['genre'].grid(   row= 14,column=2,columnspan=10)
        self.L['year'].grid(    row= 15,column=1)
        self.E['year'].grid(    row= 15,column=2,columnspan=10)
        self.L['comment'].grid( row= 16, column=1)
        self.E['comment'].grid( row= 16, column=2,columnspan=10)


        self.B['path'].grid(    row=17, column=1)
        self.B['fill'].grid(    row=17, column=2)
        self.B['save'].grid(    row=17,column= 3)
        self.B['prev'].grid(    row=17,column= 4)
        self.B['next'].grid(    row=17,column=5)
        self.B['quit'].grid(    row=17,column=6)

        # bind custom events
        self.E['title'].bind( '<KeyRelease>',self.updateAutoFileName)
        self.E['artist'].bind('<KeyRelease>',self.updateAutoFileName)
        self.R.bind('<Control-s>',self.saveData)
        self.R.bind('<Control-S>',self.saveData)
        self.R.bind('<Control-a>',self.loadPrevFile)
        self.R.bind('<Control-A>',self.loadPrevFile)
        self.R.bind('<Control-d>',self.loadNextFile)
        self.R.bind('<Control-D>',self.loadNextFile)
        self.R.bind('<Control-f>',self.fill_old_data)
        self.R.bind('<Control-F>',self.fill_old_data)
        self.R.bind('<Control-q>',self.quit)
        self.R.bind('<Control-Q>',self.quit)

    def quit(self,*kargs):
        print('exiting')
        self.F.quit()

    def update_config_path(self):

        _dir = filedialog.askdirectory(parent=self.R, initialdir=self._targpath,
                                       title='Please select a music directory')
        if(_dir == ''):
            print('no change')
            return None
        dd = {'path': _dir}
        with open('config.json', 'w') as ffout:
            json.dump(dd, ffout, indent=1)
        self._targpath = _dir
        print('you selected:',_dir)
        self.updateFileList()
        self.populateListBox()
        self.setAllFromIndex(0) # initialize data fields
        self.update_prev_data()

    def updateFileList(self):
        self._filelist = [os.path.join(self._targpath,ifile) for ifile in
                          os.listdir(self._targpath) if('mp3' in ifile)]

    def updateAutoFileName(self,event): # perhaps "tk.Event" ?
        ''' here, will outline the formatting for auto-filenaming, and this
            function is to be used as a callback
        * For now, keeping things just as <Artist> - <Title>
        * want to run this on keypress of artist & title widgets
        '''
        filepath = os.path.dirname(self.V['fname'].get())

        # if track number is available, prepend it to filename
        track=self.V['track'].get().split('/')[0]
        if(track != ''):
            track = '{:0>2} '.format(track)

        text = track+'{} - {}.mp3'.format(self.V['artist'].get(),self.V['title'].get())
        text = clean_string(text)
        self.V['autoFNM'].set(os.path.join(filepath,text))

    def populateListBox(self):
        ''' Clears anything in the list box, then populates it with
        items_list.
        '''
        end = max(self.I['files'].size()-1,0) # use max in case no lines
        self.I['files'].delete(0,end)
        for item in self._filelist:
            self.I['files'].insert(tk.END,item) # adds newline

    def setAllFromIndex(self,index):
        ''' given self._filelist, load a given index and update
            self._current
        '''
        self.update_prev_data() # before switching, get what's currently there
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
            self.updateAutoFileName(1) # requires argument while updating
            res['fname'] = self.V['autoFNM'].get()
        return res

    def fill_old_data(self,*kargs):
        # use previous file's data and fill in artist, album, genre, year, comment
        # print('previous:',self._prev_info)
        for ifield in self._prev_info.keys():
            self.V[ifield].set(self._prev_info[ifield])

    def update_prev_data(self):
        self._prev_info = {
            'artist':self.E['artist'].get(),
            'album':self.E['album'].get(),
            'genre':self.E['genre'].get(),
            'year':self.E['year'].get(),
            'comment':self.E['comment'].get(),
        }

    def saveData(self,*kargs): # new version of save
        print('saving metadata & filename')
        i1 = self.origInfo
        i2 = self.getAllFields()

        os.rename(i1['fname'], i2['fname'])
        self.updateFileList()
        self.populateListBox()
        dat = ka.MetaMP3(i2['fname'])
        for ifield in dat.tags:
            dat.set(ifield, i2[ifield])
        dat.save()
        self.origInfo = i2

        # after saving, update fname and comment, the only two that can be auto-changed by program
        self.V['fname'].set(i2['fname'])
        self.V['comment'].set(i2['comment'])

    def saveData_old0(self,*kargs): # kargs needed for callback
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
            os.rename(os.path.abspath(i1['fname']),i2['fname'])
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
        self.update_prev_data() # initialize "prevoius" data
        self.R.mainloop()
        self.R.destroy()

# kjg190626: ok, for the moment, will run from 00... folder



if(__name__ == '__main__'):

    # look for config file, if none found, prompt user for starting directory
    main = MainWindow()
    main.run()
