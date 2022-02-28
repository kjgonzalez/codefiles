'''
purpose: generate, store, and modify a family tree
general usage:
* GUI, with which one can visualize and modify a tree
* command-line, to modify the tree

general structure:
* all people stored in a dictionary, with each entry a person
Person:
    * first name
    * middle name
    * last name
    * birthdate
    * deathdate
    * partners
    * children
    * parents
* base person type: null (used for branches with no known parents, no children, no partner)

'''

import math
from datetime import date, timedelta
from datetime import datetime
now = datetime.now
from pprint import pprint
import tkinter as tk
from tkinter import font as ft # optional: control fonts used in tkinter

class Person:
    def __init__(self):
        self.fname = ''
        self.mname = ''
        self.lname = ''
        self.lname0= ''
        self.bday:date = None
        self.bloc = ''
        self.mom = '' # should be uid format
        self.dad = '' # should be uid format
        self.kids = [] # should be uid format
        self.dday:date = None
        self.dloc = ''

    def __repr__(self):
        return self.uid
    def set(self,firstname,middlename,lastname,bdayYYYYMMDD,birthloc,
            mom='',dad='',kids=[],ddayYYYYMMDD='',deathloc=''):
        self.fname = firstname
        self.mname = middlename
        self.lname = lastname
        self.bday = datetime.strptime(bdayYYYYMMDD,'%Y%m%d').date()
        self.bloc = birthloc
        self.mom = mom
        self.dad = dad
        if(ddayYYYYMMDD != ''):
            self.bday = datetime.strptime(bdayYYYYMMDD, '%Y%m%d').date()
            assert deathloc != '', "no death location given"
            self.dloc = deathloc
        if(type(kids) is list and len(kids)>0):
            # for each kid, check that proper format
            self.kids = kids
        return self
    @property
    def uid(self):
        bday = 'NULL' if(self.bday is None) else self.bday.strftime('%Y')
        return bday+self.fname+self.lname # temp
    @property
    def age(self):
        ''' todo: need workaround for leapyear bdays '''
        if(self.bday is None):
            return -1
        elif(self.dday is not None):
            ndays = self.dday-self.bday
        else:
            ndays = now().date() - self.bday
        return math.floor(ndays.days/365.25)

    def isalive(self):
        if(self.bday is None):
            return False
        return self.dday is None

    def iscorrect(self):
        ''' check that class is correctly filled out '''
        assert type(self.fname) is str,"invalid first name: "+self.fname
        assert type(self.mname) is str,"invalid middle name: "+self.mname
        assert type(self.lname) is str,"invalid last name: "+self.lname
        assert type(self.bloc) is str,"invalid birth location: "+self.bloc
        assert type(self.dloc) is str,"invalid death location: "+self.dloc
        mom = self.mom
        dad = self.dad
        assert type(mom) is str,"invalid mom name: "+mom
        assert type(dad) is str,"invalid dad name: "+dad
        assert (mom == '') or (mom[:4].isnumeric() and mom[4:].isalpha()),"invalid mom id"
        assert (dad == '') or (dad[:4].isnumeric() and dad[4:].isalpha()),"invalid dad id"
        return True
class FamilyTree:
    def __init__(self):
        self.fam = dict() # dictionary of families
    def add(self,pers:Person):
        # todo: add checks
        if(pers.iscorrect()):
            self.fam[pers.uid] = pers

class MainWindow:
    def __init__(self):
        self.R = tk.Tk() # create root object
        # self.R.resizable(False,False) # can optionally fix window dimensions
        self.R.title("Family Tree")
        helv = ft.Font(self.R,family='Helvetica',size=12) # default is 9
        self.F=tk.Frame(self.R) # declare root window
        self.F.grid()
        # self.F.pack() # construct root window

        # tkinter variable (best to declare these first)
        self.V=dict()
        self.V['n'] = tk.IntVar() # initialize a tkinter variable
        self.V['print'] = tk.IntVar() # booleans are treated as ints

        self.wlist_whole = tk.Listbox(self.F)
        self.wlist_immed = tk.Listbox(self.F)
        self.wlabel_sel = tk.Label(self.F,text='n/a')
        self.wlabel_meta = tk.Label(self.F,text='n/a')
        self.wbt_add = tk.Button(self.F,text='Add',command=self.cb_add)
        self.wbt_parents = tk.Button(self.F,text='Set Parents',command=self.cb_parents)
        self.wbt_kids = tk.Button(self.F,text='Add Children',command=self.cb_kids)
        self.wbt_modify = tk.Button(self.F,text='Modify',command=self.cb_modify)
        self.wbt_remove = tk.Button(self.F,text='Remove',command=self.cb_remove)
        self.wbt_save = tk.Button(self.F,text='Save',command=self.cb_save)

        self.wlist_whole.grid( row=0,column=0,rowspan=3)
        self.wlabel_sel.grid(  row=0,column=1)
        self.wlabel_meta.grid( row=1,column=1)
        self.wlist_immed.grid( row=2,column=1)
        self.wbt_add.grid(     row=3,column=0)
        self.wbt_parents.grid( row=4,column=0)
        self.wbt_kids.grid(    row=5,column=0)
        self.wbt_modify.grid(  row=3,column=1)
        self.wbt_remove.grid(  row=4,column=1)
        self.wbt_save.grid(    row=5,column=1)

        # once everything's been declared, it's easiest to place it all at once in one spot

        # bind custom events here, after laying out all GUI elements
        # self.R.bind('<q>',self.cb_quit) # case sensitive
        # self.R.bind('<Q>',self.cb_quit) # case sensitive
        # self.R.bind('<Down>',self.cb_vardn) # case sensitive
        # self.R.bind('<Up>',self.cb_varup) # case sensitive
        # self.R.bind("<KeyPress>", self.keydown)    # bind "keydown" fn to keyPRESS

    def cb_add(self):
        pass
    def cb_parents(self):
        pass
    def cb_kids(self):
        pass
    def cb_modify(self):
        pass
    def cb_remove(self):
        pass
    def cb_save(self):
        pass




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



p = Person()
p.fname = 'aida'
p.mname = 'cecilia'
p.lname = 'gonzalez'
p.bday = date(1960,2,29)
p.bloc = 'cartagena'
p.mom = '1929aida'
print(p.uid)
print(p.age)
print(p.isalive())
print(p.iscorrect())

'''
people are related via: 
granny-mom-daughter
'''

f = FamilyTree()
f.add(Person().set('aida','cecilia','gonzalez','19600229','carta'))
f.add(Person().set('jose','amado','gonzalez','19450718','antigua'))
pprint(f.fam)
MainWindow().run()
# eof
