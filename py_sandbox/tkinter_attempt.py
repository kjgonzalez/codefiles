# PART ONE #######################################

# import Tkinter as tk
# root = tk.Tk()
# w = tk.Label(root, text="Hello, world!")
# w.pack()
# frame=tk.Frame(root)
# frame.pack()
# b1=tk.Button(frame,text='Close',command=frame.quit)
# def say_hi():
# 	print 'hello'
# b2=tk.Button(frame,text='Hi',command=say_hi())
# b1.pack()
# b2.pack()
# root.mainloop()


# PART TWO #######################################

# from Tkinter import *
# class App:
# 	def __init__(self,master):
# 		frame = Frame(master)
# 		frame.pack()
# 		self.button=Button(frame,text='Quit',fg='red',command=frame.quit)
# 		self.button.pack(side=LEFT)
# 		self.hi_there=Button(frame,text='Hello',command=self.say_hi)
# 		self.hi_there.pack(side=LEFT)
# 	def say_hi(self):
# 		print 'hi there'
# root=Tk()
# app=App(root)
# root.mainloop()
# root.destroy()


# PART THREE #####################################

# from Tkinter import *
# def say_hi():
# 	print 'hi'

# root = Tk()
# frame=Frame(root)
# frame.pack()
# button=Button(frame,text='Quit',fg='black',command=frame.quit)
# button.pack(side=LEFT)
# hi_there=Button(frame,text='hello',command=say_hi)
# hi_there.pack()

# root.mainloop()
# root.destroy()


# PART FOUR ######################################

# from Tkinter import *

# master = Tk()

# w = Canvas(master, width=200, height=100)
# w.pack()

# w.create_line(0, 0, 200, 100)
# w.create_line(0, 100, 200, 0, fill="red", dash=(4, 4))

# w.create_rectangle(50, 25, 150, 75, fill="blue")
# mainloop()


# PART FOUR ######################################

# from Tkinter import *

# root = Tk()

# def callback(event):
#     print "clicked at", event.x, event.y

# frame = Frame(root, width=100, height=100)
# frame.bind("<Button-1>", callback)
# frame.bind("<Button-3>", callback)
# frame.pack()

# root.mainloop()


# PART FIVE ######################################
# from Tkinter import *

# root = Tk()

# def key(event):
#     print "pressed", repr(event.char)

# def callback(event):
#     frame.focus_set()
#     print "clicked at", event.x, event.y

# frame = Frame(root, width=100, height=100)
# frame.bind("<Key>", key)
# frame.bind("<Button-1>", callback)
# frame.pack()

# root.mainloop()

'''
want: form to enter in different information. then store, load, modify it.
info: ncr. desc. combination of stuff

'''
# PART SIX #######################################
# from Tkinter import *
from tkinter import *
def listContents():
	from os import curdir, listdir
	dirList=listdir(curdir)
	for i in dirList:
		print(i)

root = Tk()
frame=Frame(root)
frame.pack()
b_quit=Button(frame,text='Close',fg='black',command=frame.quit)
b_quit.pack(side=LEFT)
b_getList=Button(frame,text='Reload',command=listContents)
b_getList.pack()
root.mainloop()
root.destroy()

# will start with buttons "Reload", "new", "close"


# root = Tk()
# frame=Frame(root)
# frame.pack()
# button=Button(frame,text='Quit',fg='black',command=frame.quit)
# button.pack(side=LEFT)
# hi_there=Button(frame,text='hello',command=say_hi)
# hi_there.pack()

# root.mainloop()
# root.destroy()

