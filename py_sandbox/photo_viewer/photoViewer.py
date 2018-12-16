'''
Author: Kris Gonzalez
DateCreated: 181214
Objective: Create simple photo viewer that may be improved to then quickly edit photos in folders.

Simple goals: 
STAT | DESCRIP
done | make main window
done | show a single photo
done | enable closing window with 'Esc'
done | be able to cycle through multiple photos
done | control size of photo (max to window?)
.... | rotate currently loaded photo
.... | save any edits when move to next photo
.... | optional: get rid of exif data?

DEBUGGING:
* figure out how to avoid doubly-destroying the main window
* what metadata should be shown on status window? 
    * file name / path
    * dimensions
    * ratio?

ASSUMPTIONS: 
* python3
* will be editing photos and preserving exif data
'''


import tkinter as tk
from PIL import ImageTk as tki
import PIL.Image as pil
import matplotlib.pyplot as plt
import kimg
import os

class MainWindow:
    def __init__(self):
        # load img files data, initialize
        self.files=kimg.getlist(recursive=False)
        self.n=len(self.files)
        self.counter=0
        self.image=pil.open(self.files[0])
        
        # setup gui elements
        self.main=tk.Tk()
        screen=( self.main.winfo_screenwidth(),
                self.main.winfo_screenheight() )
        iniD=[int(i*2/3) for i in screen]
        self.main.geometry("{}x{}".format(*iniD)) # width,height
        
        # setup button frame and all relevant buttons
        kb={} # initialize keybinds
        kb['prev']='<a>'
        kb['next']='<d>'
        kb['rot']='<r>'
        self.fra_but=tk.Frame(self.main)
        self.fra_but.pack()
        but_prv=tk.Button(self.fra_but,
                text='prev pic {}'.format(kb['prev']),command=self.get_prev)
        but_prv.pack(side=tk.LEFT)
        but_nxt=tk.Button(self.fra_but,
                text='next pic {}'.format(kb['next']),command=self.get_next)
        but_nxt.pack(side=tk.LEFT)
        # but_dim=tk.Button(self.fra_but,text='wdims',command=self.getwdims)
        # but_dim.pack(side=tk.LEFT)
        but_rot=tk.Button(self.fra_but,
                text='Rot90CW {}'.format(kb['rot']),command=self.img_rotate)
        but_rot.pack(side=tk.LEFT)
        but_dbg=tk.Button(self.fra_but,text='DEBUG',command=self.rundebug)
        but_dbg.pack(side=tk.RIGHT)
        
        # setup in-window text
        self.fra_txt=tk.Frame(self.main)
        self.fra_txt.pack()
        self.txt01=tk.Label(self.fra_txt)
        self.txt01.pack(side=tk.LEFT)
        self.txtdims=tk.Label(self.fra_txt)
        self.txtdims.pack(side=tk.LEFT)
        self.updateText()
        
        # load image into window
        self.img01=tk.Label(image)
        self.img01.pack()
        self.newpic(self.image_path)
        
        # setup keybinds
        self.main.bind('<Escape>',lambda quit:self.main.destroy()) # quit
        self.main.bind(kb['prev'],lambda prev:self.get_prev())
        self.main.bind(kb['next'],lambda next:self.get_next())
        self.main.bind(kb['rot'],lambda rot:self.img_rotate())
        
        # run everything
        self.main.mainloop()
    @property
    def imagepath(self):
        ''' return path to currently loaded file '''
        return self.files[self.counter]
    def incdec(self,dir):
        # 0 = down, 1 = up
        if(dir==0):
            # decrement
            self.counter-=1
            if(self.counter<0):
                self.counter=self.n-1
        else:
            # increment
            self.counter+=1
            if(self.counter>=self.n):
                self.counter=0
    # def incdec
    def rundebug(self):
        import ipdb;ipdb.set_trace()
    def getfname(self):
        curr=self.files[self.counter]
        return curr.split(os.sep)[-1]
    def updateText(self):
        self.txt01.configure(text=self.getfname())
        dim_str='[W,H]: [{},{}]'.format(*self.image.size)
        self.txtdims.configure(text=dim_str)
    def get_next(self):
        self.incdec(1) # increment counter
        self.newpic(self.files[self.counter])
        self.updateText()
    def get_prev(self):
        self.incdec(0) # decrement counter
        self.newpic(self.files[self.counter])
        self.updateText()
    def fn(self):
        print(self.getfiles())
    def getwdims(self):
        ''' Return current (width,height) of window. NOTE: pillow library uses 
            'size', which returns dimensions as (width,height) '''
        HToffset=50 # (offset for control stuff.)
        wsize=(self.main.winfo_width(),self.main.winfo_height()-HToffset)
        return wsize
    def newpic(self,imgname):
        ''' Load new pic for display. note that PIL displays dimensions via 
            'size', which returns values as (width,height) '''
        # kjgnote: pil *.size returns (width,height) in pixels
        self.image=pil.open(imgname)
        img=self.resizeToWindow(self.image,self.getwdims())
        img=tki.PhotoImage(img)
        self.img01.configure(image=img)
        self.img01.image=img
    def img_rotate(self):
        ''' rotate image, update window
        KJGNOTE: may need new 'update' function, because this function shares
            code with "newpic"
        '''
        self.image=self.image.rotate(90,expand=1) # CW 90deg
        img=self.resizeToWindow(self.image,self.getwdims())
        img=tki.PhotoImage(img)
        self.img01.configure(image=img)
        self.img01.image=img
        self.updateText()
    def resizeToWindow(self,img_pil,wdims):
        ''' Return img resized to window. img_pil comes in as pil image object, 
            with dimensions expressed as (width,height)'''
        I=[float(i) for i in img_pil.size] # get as (w,h). img dims
        M=[float(i) for i in wdims] # get (w,h). max dims
        minR=min([M[k]/I[k] for k in range(2)]) # min ratio
        if(minR<1.0):
            return img_pil.resize(tuple([int(i*minR) for i in I]))
        else:
            return img_pil
# class MainWindow

if(__name__=='__main__'):
    w=MainWindow()