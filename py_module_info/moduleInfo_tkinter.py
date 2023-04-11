'''
datecreated: 191026
objective: give good examples on how to use various tkinter modules.
notes:
* will be using object oriented implementation, best approach for tkinter
* will be using grid layout to build everything, simple and powerful


things to demonstrate:
* simple window - done
* hotkeys - done
* button - done
* how to organize variables / elements (dictionaries) - done
* how to arrange all buttons (grid) - done
* tkinter variables - done
* checkmarks - done
* multi-button input - done

common keybinds:
more info:
    https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/key-names.html
    https://stackoverflow.com/questions/16082243/how-to-bind-ctrl-in-python-tkinter
  Up, Down, Left, Right
  Control-c
  slash, backslash, 1, Key-1
  <Double-Button-1>
| event                 | name                  |
| Ctrl-c                | Control-c             |
| Ctrl-/                | Control-slash         |
| Ctrl-\                | Control-backslash     |
| Ctrl+(Mouse Button-1) | Control-1             |
| Ctrl-1                | Control-Key-1         |
| Enter key             | Return                |
|                       | Button-1              |
|                       | ButtonRelease-1       |
|                       | Home                  |
|                       | Up, Down, Left, Right |
|                       | Configure             |
| window exposed        | Expose                |
| mouse enters widget   | Enter                 |
| mouse leaves widget   | Leave                 |
|                       | Key                   |
|                       | Tab                   |
|                       | space                 |
|                       | BackSpace             |
|                       | KeyRelease-BackSpace  |
| any key release       | KeyRelease            |
| escape                | Escape                |
|                       | F1                    |
|                       | Alt-h                 |



'''

import tkinter as tk
from tkinter import font as ft # optional: control fonts used in tkinter
from tkinter import ttk

class GUI:
    def __init__(self):
        self.R = tk.Tk()
        self.R.title('hello tkinter')
        # self.R.resizable(False,False) # can optionally fix window dimensions
        # self.R.geometry(1000x750)
        self.F = tk.Frame(self.R)
        helv = ft.Font(self.R,family='Helvetica',size=12)
        self.varint = tk.IntVar()
        self.varstr = tk.StringVar()
        self.lbl = tk.Label(self.F,text='onetwo')
        self.btn = tk.Button(self.F,text='button',command=lambda:print('hello world'))
        self.chk = tk.Checkbutton(self.F,text='print')
        self.rfm = tk.Frame(self.F)
        self.rb1 = tk.Radiobutton(self.rfm,variable=self.varint,value=1)
        self.rb2 = tk.Radiobutton(self.rfm,variable=self.varint,value=2)
        self.cbx = ttk.Combobox(self.F)
        self.lbx = tk.Listbox(self.F)
        # todo: scrollbar
        # todo: text
        # todo: scale
        # todo: spinbox
        # todo: progressbar
        # todo: canvas
        # todo: menu

        self.F.grid(row=0,column=0)
        self.btn.grid(row=1,column=0)
        self.chk.grid(row=2,column=0)
        self.rfm.grid(row=3,column=0)
        self.lbl.grid(row=4,column=0)
        self.cbx.grid(row=5,column=0)
        self.lbx.grid(row=6,column=0)

        self.rb1.grid(row=0,column=0)
        self.rb2.grid(row=0,column=1)
        self.R.bind('<q>',lambda x: self.F.quit())

    def run(self):
        self.R.mainloop() # vital for each and every tkinter function
        try: self.R.destroy() # after the mainloop, everything must be removed
        except: pass

class MainWindow:
    def __init__(self):
        self.R = tk.Tk() # create root object
        # self.R.resizable(False,False) # can optionally fix window dimensions
        self.R.title("Hello Tkinter")
        helv = ft.Font(self.R,family='Helvetica',size=12) # default is 9
        self.F=tk.Frame(self.R) # declare root window
        self.F.pack() # construct root window

        # tkinter variable (best to declare these first)
        self.V=dict()
        self.V['n'] = tk.IntVar() # initialize a tkinter variable
        self.V['print'] = tk.IntVar() # booleans are treated as ints

        self.B=dict() # easiest way to save and reference various objects
        self.B['quit'] = tk.Button(self.F,text='QUIT',command=self.cb_quit) # min button declaration
        self.B['inc'] = tk.Button(self.F,text='INCREMENT',command=self.cb_varup)
        self.B['greet'] = tk.Button(self.F,text='Hello!',command=self.cb_hello)

        self.C=dict()
        self.C['print'] = tk.Checkbutton(self.F,text='print?',variable=self.V['print'])

        # self.A=tk.Canvas(self.F,width=400,height=300,borderwidth=10,background='white')
        # self.A.create_rectangle(10,10,50,50,fill='black')

        self.L=dict()
        self.L['static'] = tk.Label(self.F,text='SomeText')
        self.L['n'] = tk.Label(self.F,textvariable=self.V['n'])

        # once everything's been declared, it's easiest to place it all at once in one spot
        self.B['quit'].grid(row=1,column=0)
        self.B['inc'].grid(row=1,column=1)
        self.B['greet'].grid(row=1,column=2)
        self.L['static'].grid(row=0,column=0) # only integers 0 or greater
        self.L['n'].grid(row=2,column=1)
        self.C['print'].grid(row=2,column=0)
        # self.A.grid(row=3,column=3)

        # bind custom events here, after laying out all GUI elements
        self.R.bind('<q>',self.cb_quit) # case sensitive
        self.R.bind('<Q>',self.cb_quit) # case sensitive
        self.R.bind('<Down>',self.cb_vardn) # case sensitive
        self.R.bind('<Up>',self.cb_varup) # case sensitive
        # self.R.bind("<KeyPress>", self.keydown)    # bind "keydown" fn to keyPRESS

    def keydown(self,e):
        print(e)


    def cb_quit(self,*kargs): # using *kargs instead of "event" to just accept everything
        print('exiting')
        self.F.quit()

    def cb_hello(self,*kargs):
        print('hello world!')

    def cb_varup(self,*kargs):
        self.V['n'].set(self.V['n'].get()+1) # purely via tkinter, can use normal vars as well
        if(self.V['print'].get()):
            # variable set to 1
            print(self.V['n'].get())

    def cb_vardn(self,*kargs):
        self.V['n'].set(self.V['n'].get()-1)
        if(self.V['print'].get()):
            print(self.V['n'].get())

    def run(self):
        self.R.mainloop() # vital for each and every tkinter function
        self.R.destroy() # after the mainloop, everything must be removed


if(__name__=='__main__'):
    GUI().run()
    # main = MainWindow().run()
