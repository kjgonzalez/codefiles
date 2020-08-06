'''
quick practice with tkinter
'''


from Tkinter import *
print 'Tkinter loaded'

master = Tk()

def callback():
    print "click!"

b = Button(master, text="OK", command=callback)
b.pack()

mainloop()