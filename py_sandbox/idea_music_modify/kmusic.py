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

'''

import argparse
import os
import os.path as osp
import eyed3

def getsongs(path):
    return [osp.join(path,i) for i in os.listdir(path) if('mp3' in i)]

class Audiofile:
    def __init__(self,path,verbose=False):
        eyed3.log.setLevel('ERROR')
        self.path = path
        self.v=verbose
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
        d['fname']=  self.filename
        d['title']=  a.tag.title
        d['artist']= a.tag.artist
        d['album']=  a.tag.album
        d['genre']=  None if(a.tag.genre is None) else a.tag.genre.name
        d['year']=   None if(a.tag.release_date is None) else a.tag.release_date.year
        d['trknum']= a.tag.track_num[0]
        d['trktot']= a.tag.track_num[1]
        d['comment']=None if(len(a.tag.comments)<1) else a.tag.comments[0].text
        return d
    
    def edit(self,fname=None,title=None,artist=None,album=None,genre=None,year=None,trknum=None,trktot=None,comment=None):
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
    def autoFname(self):
        dd=self.props
        self.edit(fname=dd['artist']+' - '+dd['title']+'.mp3')
        return self


if(__name__ == '__main__'):
    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--a',dest='int1',type=int,help='first int',default=0)
    args=p.parse_args()
    

#eof

