'''Example that demonstrates keeping track of multiple key events'''
from tkinter import *

class Playfield:
    def __init__(self):
        # this dict keeps track of keys that have been pressed but not
        # released
        self.pressed = {}

        self._create_ui()

    def start(self):
        self._animate()
        self.root.mainloop()

    def _create_ui(self):
        self.root = Tk()
        self.p1label = Label(text="press w, s to move player 1 up, down", 
                             anchor="w")
        self.p2label = Label(text="press o, l to move player 2 up, down", 
                             anchor="w")
        self.canvas = Canvas(width=440, height=440)
        self.canvas.config(scrollregion=(-20, -20, 420, 420))

        self.p1label.pack(side="top", fill="x")
        self.p2label.pack(side="top", fill="x")
        self.canvas.pack(side="top", fill="both", expand="true")

        self.p1 = Paddle(self.canvas, tag="p1", color="red", x=0, y=0)
        self.p2 = Paddle(self.canvas, tag="p2", color="blue", x=400, y=0)

        self._set_bindings()

    def _animate(self):
        if self.pressed["w"]: self.p1.move_up()
        if self.pressed["s"]: self.p1.move_down()
        if self.pressed["o"]: self.p2.move_up()
        if self.pressed["l"]: self.p2.move_down()
        self.p1.redraw()
        self.p2.redraw()
        self.root.after(10, self._animate)

    def _set_bindings(self):
        for char in ["w","s","o", "l"]:
            self.root.bind("<KeyPress-%s>" % char, self._pressed)
            self.root.bind("<KeyRelease-%s>" % char, self._released)
            self.pressed[char] = False

    def _pressed(self, event):
        self.pressed[event.char] = True

    def _released(self, event):
        self.pressed[event.char] = False

class Paddle():
    def __init__(self, canvas, tag, color="red", x=0, y=0):
        self.canvas = canvas
        self.tag = tag
        self.x = x
        self.y = y
        self.color = color
        self.redraw()

    def move_up(self):
        self.y = max(self.y -2, 0)

    def move_down(self):
        self.y = min(self.y + 2, 400)

    def redraw(self):
        x0 = self.x - 10
        x1 = self.x + 10
        y0 = self.y - 20
        y1 = self.y + 20
        self.canvas.delete(self.tag)
        self.canvas.create_rectangle(x0,y0,x1,y1,tags=self.tag, fill=self.color)

if __name__ == "__main__":
    p = Playfield()
    p.start()