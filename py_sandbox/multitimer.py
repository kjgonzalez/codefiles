'''
datecreated: 190830
objective: mock-up of talker timer

General Steps:
1. get a ui
2. have labels
3. have the active timer going
4. have a total timer
5. be able to export

'''

import tkinter as tk
import time
import numpy as np

# for python 3.x use 'tkinter' rather than 'Tkinter'


r = tk.Tk()
f=tk.Frame(r)
f.pack()

# names
names='dmself dmchar vax vex grog scanlan percy kiki none'.split(' ')
alts ='q,a,w,e,r,s,d,f, '.split(',')
n={alts[i]:names[i] for i in range(len(alts))}

names=names[:-1]
# control variables
v=dict()
for iname in names:
    v[iname]=tk.DoubleVar()
v['total']=tk.DoubleVar()

# label forms
l=dict()
for iname in names:
    l[iname]=tk.Label(f,textvariable=v[iname])
    l['_'+iname]=tk.Label(f,text=iname)
l['_total']=tk.Label(f,text='total')
l['total']=tk.Label(f,textvariable=v['total'])
l['spacer']=tk.Label(f,text=' '*100)
l['_total'].configure(font=('Helvetica', 10, 'bold'))
l['_total'].configure(font=('Helvetica', 10, ''))
# font=('Helvetica', 10, 'bold')

# initialize variables
for iname in names:
    v[iname].set(0)

for i,iname in enumerate(names):
    l['_'+iname].grid(row=i,column=0)
    l[iname].grid(    row=i,column=1)
l['_total'].grid(row=20,column=0)
l['total'].grid(row=20,column=1)
l['spacer'].grid(row=21,column=1)

target='none'
def focus(key):
    ''' given a certain key, change focus '''
    global target
    target=n[key]
    # change look of the label and ensure others are to original look
    for iname in names:
        l[iname].configure(font=('Helvetica', 10, ''))
        l['_'+iname].configure(font=('Helvetica', 10, ''))
    if(target!='none'):
        l[target].configure(font=('Helvetica', 10, 'bold'))
        l['_'+target].configure(font=('Helvetica', 10, 'bold'))

def updater(event=None):
    if(target!='none'):
        v[target].set(v[target].get()+0.1)
    v['total'].set(sum([v[iname].get() for iname in names]))
    r.after(100,updater) # time in milliseconds


def quit(event):
    f.quit()
# need one for each person, plus a stop
r.bind('q',lambda event:focus('q'))
r.bind('w',lambda event:focus('w'))
r.bind('e',lambda event:focus('e'))
r.bind('r',lambda event:focus('r'))
r.bind('a',lambda event:focus('a'))
r.bind('s',lambda event:focus('s'))
r.bind('d',lambda event:focus('d'))
r.bind('f',lambda event:focus('f'))
r.bind('<space>',lambda event:focus(' '))
r.bind('<Control-q>',quit)

updater()
r.mainloop()
r.destroy()





# eof
