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
import pandas as pd
from klib import getlist
try:
    import tkinter as tk
    from tkinter import ttk
except:
    print("no GUI available, shell only")
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

class Dframe(pd.DataFrame):
    def filt(self,col,isval='',hasval=''):
        assert col in self.columns,'invalid col'
        assert len(isval)+len(hasval)>0,'no parameter given'
        if(len(isval)>0):
            res = self[self[col]==isval]
            return Dframe(res.reset_index(drop=0)) # todo: untested
        else:
            mask=[]
            for ival in self[col]:
                res = hasval in str(ival)
                mask.append(res)
            res = self[mask]
            return Dframe(res.reset_index(drop=0))

def regen_allprops(path):
    ''' given a path, collect all relevant properties '''
    allprops=[]
    for ifile in getlist(path,recursive=1,exts='mp3'):
        d=Audiofile(ifile).props
        allprops.append(d)
    return Dframe(allprops)

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
    def makeplace(elem,row,col):
        elem.grid(row=row,column=col) # need more later
        return elem

    def __init__(self):
        self.R = tk.Tk()
        self.R.title('hello tkinter')
        # self.R.resizable(False,False) # can optionally fix window dimensions
        # self.R.geometry("1000x750") # start at a particular window size
        # self.R.geometry("+10+10") # start at a particular location
        mp = self.makeplace

        self.F = mp(tk.Frame(self.R),0,0)

        self.lbl = mp(tk.Label(self.F,text='test'),0,0)
        self.ent = mp(tk.Entry(self.F,width=10),0,1)

        self.frm_radio = mp(tk.Frame(self.R),1,0)
        self.var_radio = tk.IntVar()
        self.rbn_1 = mp(tk.Radiobutton(self.frm_radio,text='one',variable=self.var_radio,value=1),0,0)
        self.rbn_2 = mp(tk.Radiobutton(self.frm_radio,text='two',variable=self.var_radio,value=2),0,1)

        self.scl_power = mp(tk.Scale(self.R,from_=0,to=100,length=200,orient=tk.HORIZONTAL),2,0)
        self.chk_opt = mp(tk.Checkbutton(self.R,text='activate'),3,0)
        self.btn_run = mp(tk.Button(self.R,text='Run This',command=self.cb_advance_pbar),4,0)
        self.prb_complete = mp(ttk.Progressbar(self.R,length=200),5,0) # note: need ttk

        self.lbx_vals:tk.Listbox = mp(tk.Listbox(self.R,height=4),6,0)
        self.lbx_vals.insert(tk.END,*('one two three four five six seven eight nine ten'.split(' ')))

        self.cbx_vals:ttk.Combobox = mp(ttk.Combobox(self.R,width=20,state='readonly'),7,0)
        self.cbx_vals['values'] = 'one two three four five'.split(' ')


        self.cnv_draw:tk.Canvas = mp(tk.Canvas(self.R,width=200,height=200,background='white'),20,0)
        # todo: scrollbar
        # todo: text
        # todo: spinbox
        # todo: menu
        # todo: keypresses

        self.R.bind('<q>',lambda x: self.F.quit())
        self.R.bind('<Button-1>',self.cb_draw_point)

    def cb_advance_pbar(self):
        temp = self.prb_complete['value']+10
        if(temp>100): self.prb_complete['value']=0
        else: self.prb_complete['value'] = temp

    def cb_draw_point(self,event):
        # print(event)
        if('canvas' not in str(event.widget)): return None
        x,y = event.x,event.y
        sz=2
        self.cnv_draw.create_oval(x-sz,y-sz,x+sz,y+sz,fill='red',outline='green',width=2)

    def _entryfocus(self):
        ents = []
        ents.append(str(self.ent))
        if(str(self.R.focus_get()) in ents): return True
        return False

    def run(self):
        self.R.mainloop() # vital for each and every tkinter function




if(__name__ == '__main__'):
    #p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    #p.add_argument('--a',dest='int1',type=int,help='first int',default=0)
    #args=p.parse_args()

    ''' debug: look for carlos bollorque music '''
    path = '/data/data/com.termux/files/home/storage/music/'
    path = 'debugging'
    print('exists:',os.path.exists(path))
    #files = getsongs(path,filters={'artist':'Carlos Bollorque'})
    files = getsongs(path)
    print(f'{len(files)} files')
    print(Audiofile(files[0]).props)
    #for ifile in files: print('',ifile)
#eof

