'''
Author: Kris Gonzalez
DateCreated: 181214
Objective: Create simple photo viewer that may be improved to then quickly edit photos in folders.

simple goals: 
stat | descrip
done | make main window
done | show a single photo
done | enable closing window with 'Esc'
.... | be able to cycle through multiple photos
.... | be able to rotate photo, save when move to next photo
.... | optional: get rid of exif data?

DEBUGGING:
* figure out how to avoid doubly-destroying the main window

ASSUMPTIONS: 
* python3
* will be editing photos and preserving exif data
'''


import tkinter as tk
from PIL import ImageTk as tki
import PIL.Image as pil
import matplotlib.pyplot as plt

class MainWindow:
	def __init__(self):
		self.main=tk.Tk()
		frame=tk.Frame(self.main)
		frame.pack()
		self.main.bind('<Escape>',lambda quit:self.main.destroy()) # quit
		txt01=tk.Label(self.main,text="Hello World")
		txt01.pack()
		but01=tk.Button(self.main,text='new pic',command=self.newpic)
		but01.pack()
		but02=tk.Button(self.main,text='getlist',command=self.fn)
		but02.pack()
		imgname='orig.jpg'
		img=tki.PhotoImage(pil.open(imgname))
		self.img01=tk.Label(image=img)
		self.img01.pack()
		self.main.mainloop()
	def run(self):
		self.main.mainloop()
	def fn(self):
		print(self.getfiles())
	def newpic(self):
		imgname='temp.gif'
		img=tki.PhotoImage(pil.open(imgname))
		self.img01.configure(image=img)
		self.img01.image=img
		#self.img01.pack()
	def getfiles(self):
		import os
		return os.listdir('.')
# class MainWindow
if(__name__=='__main__'):
	w=MainWindow()