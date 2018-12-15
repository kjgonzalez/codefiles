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
.... | control size of photo (max to window?)
.... | be able to rotate photo, save when move to next photo
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
        
        # setup gui elements
        self.main=tk.Tk()
        frame=tk.Frame(self.main)
        frame.pack()
        self.txt01=tk.Label(self.main,text=self.getfname())
        self.txt01.pack()
        but01=tk.Button(self.main,text='next pic',command=self.get_next)
        but01.pack()
        but02=tk.Button(self.main,text='prev pic',command=self.get_prev)
        but02.pack()
        init=self.files[0]
        img=tki.PhotoImage(pil.open(init))
        self.img01=tk.Label(image=img)
        self.img01.pack()
        
        # setup keybinds
        self.main.bind('<Escape>',lambda quit:self.main.destroy()) # quit
        self.main.bind('<a>',lambda prev:self.get_prev())
        self.main.bind('<d>',lambda next:self.get_next())
        
        # run everything
        self.main.mainloop()
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
    def getfname(self):
        curr=self.files[self.counter]
        return curr.split(os.sep)[-1]
    def get_next(self):
        self.incdec(1) # increment counter
        self.newpic(self.files[self.counter])
        self.txt01.configure(text=self.getfname())
        # self.txt01.text=self.getfname()
    def get_prev(self):
        self.incdec(0) # decrement counter
        self.newpic(self.files[self.counter])
        self.txt01.configure(text=self.getfname())
        # self.txt01.text=self.getfname()
    def fn(self):
        print(self.getfiles())
    def newpic(self,imgname):
        img=tki.PhotoImage(pil.open(imgname))
        self.img01.configure(image=img)
        self.img01.image=img
# class MainWindow
if(__name__=='__main__'):
    w=MainWindow()