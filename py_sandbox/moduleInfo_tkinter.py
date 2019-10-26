'''
datecreated: 191026
objective: give good examples on how to use various tkinter modules.
notes:
* will be using object oriented implementation, best approach for tkinter

things to demonstrate:
* simple window
* how to arrange all butons (dicts)
* button
* checkmarks
* one-line text field
* long text field?
* label field
* tkinter variables
* hotkeys
* listboxes (?)
* drawing area?

'''

import tkinter as tk

class MainWindow:
    def __init__(self):
        pass
        self.R = tk.Tk() # create root object
        # self.R.resizable(False,False) # can optionally fix window dimensions
        self.R.title("Hello Tkinter")
        helv = ft.Font(self.R,family='Helvetica',size=fontSize)
        self.F=tk.Frame(self.R) # declare root window
        self.F.pack() # construct root window

    def run(self):
        self.R.mainloop() # vital for each and every tkinter function
        self.R.destroy() # after the mainloop, everything must be removed


if(__name__=='__main__'):
    main = MainWindow()
    main.run()
