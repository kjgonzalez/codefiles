'''
simple interface in order to manipulate a webcam image to look correct on screen
primary goal is to enable easier debugging on family computers
python -m venv ve_camera
python -m pip install opencv-python==4.5.5.62 Pillow
'''

import cv2
import PIL.Image as pil
from PIL import ImageTk
import tkinter as tk
from tkinter import ttk

def makeandplace(elem,row,col,sticky='wn'):
    elem.grid(row=row,column=col,sticky=sticky)
    return elem

class VideoStream():
    def __init__(self,src):
        self.src = src
        self.cap = cv2.VideoCapture(src)

    def get(self,flipv=False,fliph=False,rot=0,scale=1):
        ret,frm = self.cap.read()
        if(not ret): return None
        if(flipv): frm = cv2.flip(frm,0)
        if(fliph): frm = cv2.flip(frm,1)
        if(rot!=0):
            for i in range(0,rot,90):
                frm = cv2.rotate(frm,cv2.ROTATE_90_COUNTERCLOCKWISE)
        frm = cv2.resize(frm,(int(frm.shape[1]*scale),int(frm.shape[0]*scale)))
        frm = cv2.cvtColor(frm,cv2.COLOR_BGR2RGB)
        return frm

    def set_res(self, WxH):
        w,h = WxH.split('x')

        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, int(w))
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,int(h))

class GUI:
    def __init__(self):
        self.R = tk.Tk()
        self.R.title('KJG Webcam')
        self.F = makeandplace(tk.Frame(self.R),0,0)
        self.img = ImageTk.PhotoImage(pil.new('RGB',(400,400)))
        self.lbl_img = makeandplace(tk.Label(self.R,image=self.img),0,1)
        # self.R.resizable(False,False) # can optionally fix window dimensions
        # self.R.geometry(1000x750)
        ''' things to have: flip vert, flip horiz, rotate 90deg (stacking) '''
        self.hval = tk.IntVar()
        self.vval = tk.IntVar()
        self.cbx_src =  makeandplace(ttk.Combobox(self.F,state='readonly',values=list('0123')),2,0)
        self.cbx_src.set(0)
        self.btn_src =  makeandplace(tk.Button(self.F,text='changeSrc',command=self.cb_changesrc),3,0)
        self.chk_vert = makeandplace(tk.Checkbutton(self.F,text='Flip Vert',variable=self.vval,offvalue=False,onvalue=True),4,0)
        self.chk_horiz= makeandplace(tk.Checkbutton(self.F,text='Flip Horiz',variable=self.hval,offvalue=False,onvalue=True),5,0)
        self.btn_rot90= makeandplace(tk.Button(self.F,text='Rot90',command=self.cb_rotate),6,0)
        self.lbl_res =  makeandplace(tk.Label(self.F,text='set resolution'),7,0)
        self.ent_res =  makeandplace(tk.Entry(self.F,width=30),8,0)
        self.ent_res.insert(0,'1280x720')
        self.lbl_scl =  makeandplace(tk.Label(self.F,text='scale image'),9,0)
        self.ent_scl =  makeandplace(tk.Entry(self.F,width=30),10,0)
        self.ent_scl.insert(0,'1.0')

        # bindings
        self.R.bind('<q>',lambda x:self.F.quit())
        self.R.bind('<Return>',self.cb_changeres)
        self.angle = 0
        self.scaling = float(self.ent_scl.get())
        self.resolution = self.ent_res.get()+'a'

        # non-gui stuff
        self.vs = VideoStream(0)
        self.cb_changeres()

    def cb_changesrc(self,*kargs):
        src2 = int(self.cbx_src.get())
        if(self.vs.src == src2): return None
        vs2 = VideoStream(int(self.cbx_src.get()))
        if(vs2.get().shape is None): return None

        self.vs = vs2

    def cb_changeres(self,*kargs):
        if(self.ent_res.get() != self.resolution):
            self.resolution = self.ent_res.get()
            self.vs.set_res(self.ent_res.get())
        self.scaling = float(self.ent_scl.get())

    def cb_rotate(self): self.angle = self.angle+90 if(self.angle<260) else 0

    def cb_update(self):

        img = self.vs.get(self.vval.get(),self.hval.get(),self.angle,self.scaling)
        img = pil.fromarray(img)
        self.img = ImageTk.PhotoImage(img)
        self.lbl_img.configure(image=self.img)

        self.lbl_img.after(28,self.cb_update)

    def run(self):
        self.cb_update()
        self.R.mainloop()
        try: self.R.destroy()
        except tk.TclError: pass

if(__name__ == '__main__'):
    GUI().run()

