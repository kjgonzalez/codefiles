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



class BOILERPLATE:
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
        #try: self.R.destroy() # after the mainloop, everything must be removed
        #except: pass

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
    BOILERPLATE().run()
    # main = MainWindow().run()
