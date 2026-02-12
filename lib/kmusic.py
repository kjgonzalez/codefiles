'''
codefiles-specific side of kmusic. will remake several things, goal is to have 
  simple music-properties modification tool. will try to build fully with 
  just eyed3, maybe mutagen if needed.

sample usage:
    a=Audiofile(pathname)
    a.edit(title='blah',artist='lala').autoAlbum().props

stat description
done basic class
done usable in ipython
???? because pandas not working, need to keep pandas confined to single places where it is used
???? usable with curses
todo add list of genres for reference
todo make filtering class for ease of use
todo auto-converter to deal with outdated id tag versions

ideal usage: 
    mlib = MusicLib(path,refresh=True)
    songlist=mlib.filter(filt={})
    song = songlist[i] # needs to tie back to mlib singleton
    song.edit()...

'''

import argparse
import os
import os.path as osp
import time
import eyed3
from eyed3 import id3

HAVE_PANDAS=True
HAVE_TKINTER=True
try:
    import pandas as pd
except ImportError:
    print('pandas not available, some functions will fail')
    HAVE_PANDAS=False
from klib import getlist
try:
    import tkinter as tk
    from tkinter import ttk
    from tkinter import filedialog as fd
except ImportError:
    print("no GUI available, shell only")
    HAVE_TKINTER=False
#genres = [i for i in id3.genres.values() if (type(i) not in [int, type(None)])]
#genres.sort()

class genres:
    acoustic='Acoustic'
    alternative='Alternative'
    altrock='AlternRock'
    bachata='Bachata'
    classical='Classical'
    classicrock='Classic Rock'
    country='Country'
    dubstep='Dubstep'
    electronic='Electronic'
    hiphop='Hip-Hop'
    indie='Indie'
    indierock='Indie Rock'
    indiepop='Indie Pop'
    instrumental='Instrumental'
    latin='Latin'
    latinrock='Latin Rock'
    merengue='Merengue'
    metal='Metal'
    musical='Musical'
    oldies='Oldies'
    pop='Pop'
    reggae='Reggae'
    reggaeton='Reggaeton'
    rnb = 'R&B'
    rock='Rock'
    rocknroll='Rock & Roll'
    salsa='Salsa'
    techno='Techno'

#class Dframe(pd.DataFrame):
#    def filt(self,col,isval='',hasval=''):
#        assert col in self.columns,'invalid col'
#        assert len(isval)+len(hasval)>0,'no parameter given'
#        if(len(isval)>0):
#            res = self[self[col]==isval]
#            return Dframe(res.reset_index(drop=0)) # todo: untested
#        else:
#            mask=[]
#            for ival in self[col]:
#                res = hasval in str(ival)
#                mask.append(res)
#            res = self[mask]
#            return Dframe(res.reset_index(drop=0))

def regen_allprops(path):
    ''' given a path, collect all relevant properties '''
    import pandas as pd
    allprops=[]
    for ifile in getlist(path,recursive=1,exts='mp3'):
        d=Audiofile(ifile).props
        allprops.append(d)
    #return Dframe(allprops)
    return pd.Dataframe(allprops)

def getsongs(path,filters=None,allow_err=False):
    ''' 
    Given a path and any filters, return results. filters is a complicated 
      variable, several examples will be given. There is no recursive folder search.
    
    "songs that are in genres [country, pop] and by Taylor Swift":
    {'genre':['country','pop'],'artist':'Taylor Swift'} # note: operator "in", not "=="

    "songs that are by ACDC and in album Back in Black":
    {'artist':'AC/DC','album':'Back in Black'}

    '''
    files = []
    #print('starting')
    for ifile in os.listdir(path):
        ipath = osp.join(path,ifile)
        if('mp3' not in ifile): continue
        #print('file:',ifile)
        if(filters is not None):
            d=Audiofile(ipath).props
            keep=True # if anything not met, set false
            for ikey in filters.keys():
                #print('  filter',ikey)
                # todo: use try/except
                ivals = filters[ikey]
                if(type(ivals) is not list): ivals = [ivals]
                #ivals = filters[ikey] if(type(ivals) is list) else [filters[ikey]]
                ichk = d[ikey]
                if(ichk is None):
                    ichk = '(n/a)'
                res = max([ichk in iv for iv in ivals])
                keep = min(res,keep)
            if(keep): files.append(ipath)

        else: files.append(ipath)
    return files

def checkall(songlist:list,properties:list='fname artist genre'.split(' ')):
    ''' simple table of list of song metadata for quick scan'''
    import pandas as pd
    d = {i:[] for i in properties}
    for ifile in songlist:
        dd=Audiofile(ifile).props
        for i in properties:
            d[i].append(dd[i])
    return pd.DataFrame(d)

class Audiofile:
    def __init__(self,path,verbose=False,autoversion=False):
        eyed3.log.setLevel('ERROR')
        self.path = path
        self.v=verbose
        if(autoversion):
            tmp = eyed3.load(self.path)
            ver = tmp.tag.version
        assert 'mp3' in os.path.splitext(path)[1],'invalid filetype, mp3 only'
        if(self.v):
            dd = self.props
            print('fname:  ',self.filename)
            print('title:  ',dd['title'])
            print('artist: ',dd['artist'])
            print('album:  ',dd['album'])
            print('genre:  ',dd['genre'])
            print('year:   ',dd['year'])
            print('trknum: ',dd['trknum'])
            print('trktot: ',dd['trktot'])
            print('comment:',dd['comment'])
    @property
    def props(self):
        a = eyed3.load(self.path)
        d={}
        # d['fname']=  self.filename # todo: remove for 'path'
        d['title']=  a.tag.title
        d['artist']= a.tag.artist
        d['album']=  a.tag.album
        d['genre']=  None if(a.tag.genre is None) else a.tag.genre.name
        d['year']=   None if(a.tag.release_date is None) else a.tag.release_date.year
        d['trknum']= a.tag.track_num[0]
        d['trktot']= a.tag.track_num[1]
        # d['dir']=self.dirname # todo: remove for 'path'
        try:
            d['comment']=None if(len(a.tag.comments)<1) else a.tag.comments[0].text
        except:
            d['comment']=None
        d['path']=self.path
        return d
    
    def edit(self,fname=None,title=None,artist=None,album=None,genre=None,year=None,trknum=None,trktot=None,comment=None,autocomment=True):
        if(fname is not None): self.rename(fname)
        a = eyed3.load(self.path)
        if(title is not None): a.tag.title=title
        if(artist is not None): a.tag.artist=artist
        if(album is not None): a.tag.album=album
        if(genre is not None): a.tag.genre=genre
        if(year is not None): a.tag.release_date = year
        
        # handle track numbering as tuple
        # todo: handle more flexibly (just num, just tot, assertions)
        if(trknum is not None and trktot is not None): a.tag.track_num = (trknum,trktot)
        
        if(autocomment):
            txt='KJG'+time.strftime("%y%m%d",time.localtime(time.time()))
            if(comment is not None):
                comment = txt+': '+comment
            else:
                comment = txt

        if(comment is not None):
            if(len(a.tag.comments)<1):
                a.tag.comments.set(comment) # maybe has to be used every time?
            else:
                a.tag.comments[0].text=comment
        a.tag.save()
        return self

    @property
    def filename(self):
        return os.path.basename(self.path)
    @property
    def dirname(self):
        return os.path.dirname(self.path)
    def rename(self,fname):
        assert '.mp3' in fname,'must include valid filetype'
        base = os.path.dirname(self.path)
        path2=os.path.join(base,fname)
        os.rename(self.path,path2)
        self.path=path2
    def autoAlbum(self):
        dd=self.props
        self.edit(album=dd['title']+' - Single')
        return self
    def autoFname(self,withtrk=False):
        dd=self.props
        name2=dd['artist']+' - '+dd['title']+'.mp3'
        if(withtrk):
            name2=f"{dd['trknum']:0>2} "+name2
        # todo: filename sanitization step
        self.edit(fname=name2)
        return self


class GuiKmusic:
    ''' the very most basic starting gui to help get any project rolling'''
    @staticmethod
    def makeplace(elem,row,col,sticky='nw'):
        elem.grid(row=row,column=col,sticky=sticky) # need more later
        return elem

    def __init__(self):
        self.R = tk.Tk()
        self.R.title('KMusic GUI')
        self.R.resizable(False,False) # can optionally fix window dimensions
        mp = self.makeplace

        #self.R.rowconfigure(0,weight=1) # todo: figure out rowconfigure
        #frm_select.rowconfigure(2,weight=1)

        frm_select:tk.Frame = mp(tk.Frame(self.R),0,0)
        self.btn_selfile = mp(tk.Button(frm_select,text='Select File',command=self.cbSelFile),0,0)
        self.btn_selfldr = mp(tk.Button(frm_select,text='Select Folder',command=self.cbSelFolder),0,1)
        self.ent_selpath:tk.Entry = mp(tk.Entry(frm_select,width=70,state='readonly'),0,2) # normal, disabled, readonly

        frm_modreg:tk.Frame = mp(tk.Frame(self.R),1,0)
        self.lbx_files = mp(tk.Listbox(frm_modreg,height=20,width=50),0,0) # todo: add scrollbar

        frm_items:tk.Frame = mp(tk.Frame(frm_modreg),0,1)
        mp(tk.Label(frm_items,text='Title'),0,0)
        self.ent_title=mp(tk.Entry(frm_items,width=40),0,1)
        mp(tk.Label(frm_items,text='Artist'),1,0)
        self.ent_artist = mp(tk.Entry(frm_items, width=40), 1, 1)
        mp(tk.Label(frm_items,text='Album'),2,0)
        self.ent_album = mp(tk.Entry(frm_items, width=40), 2, 1)
        mp(tk.Label(frm_items,text='Genre'),3,0)
        self.ent_genre = mp(tk.Entry(frm_items, width=40), 3, 1)
        mp(tk.Label(frm_items,text='Year'),4,0)
        self.ent_year = mp(tk.Entry(frm_items, width=40), 4, 1)
        mp(tk.Label(frm_items,text='TrackNum'),5,0)
        self.ent_tracknum = mp(tk.Entry(frm_items, width=40), 5, 1)
        mp(tk.Label(frm_items,text='nTracks'),6,0)
        self.ent_ntracks = mp(tk.Entry(frm_items, width=40), 6, 1)

        self.R.bind('<q>',lambda x: self.cbQuit())
        self.R.bind('<Double-Button-1>',lambda x: self.cbSelItemFromList()) # <Double-Button-1>

    def cbQuit(self):
        if('entry' in str(self.R.focus_get())):
            print('ignoring')
        else:
            self.R.quit()

    def cbSelFolder(self):
        print('select folder')
        path = fd.askdirectory(title='Select Folder')
        if(path==''): return
        self.setSelectedEntry(path)

    def cbSelFile(self):
        print('select file')
        path = fd.askopenfilenames(title='Select File')[0]
        if(path==''): return
        self.setSelectedEntry(path)
        # todo: load info about selected item


    def cbSelItemFromList(self):
        x = self.R.focus_get()
        if(self.R.focus_get()!=self.lbx_files):
            return
        # todo: get selected item from list and load info


    def setSelectedEntry(self,val:str):
        self.ent_selpath.config(state='normal')
        self.ent_selpath.delete(0,tk.END)
        self.ent_selpath.insert(0,val)
        self.ent_selpath.config(state='readonly')

    def run(self):
        self.R.mainloop() # vital for each and every tkinter function




if(__name__ == '__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--gui',action='store_true',default=False,help='use GUI')
    p.add_argument('--tui',action='store_true',default=False,help='use text interface')
    p.add_argument('--song',default='',help='path to single song file, for use with tui')
    args=p.parse_args()

    # ''' debug: look for carlos bollorque music '''
    # path = '/data/data/com.termux/files/home/storage/music/'
    # path = 'debugging'
    # print('exists:',os.path.exists(path))
    # #files = getsongs(path,filters={'artist':'Carlos Bollorque'})
    # files = getsongs(path)
    # print(f'{len(files)} files')
    # print(Audiofile(files[0]).props)
    # #for ifile in files: print('',ifile)


    if(args.gui):
        if(not HAVE_TKINTER):
            print('tkinter not available, option "gui" invalid')
            exit()
        print('run gui')
        GuiKmusic().run()

    elif(args.tui):
        print('run tui (not implemented yet)')

    else:
        print('no options given')




#eof

