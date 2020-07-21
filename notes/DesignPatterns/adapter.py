'''
Objective: demonstrate adapter pattern in a small bit of example code
Source: Design Patterns, pg 157
Example: There's a suite of drawing primitives that don't include text manipulation, because
    the original framework implements text manipulation in a very different way, internally.
    an adapter, aka wrapper, can make the class more uniform when drawing any object
'''

class TextView:
    def __init__(self,txt=''):
        self.txt = txt
        self.loc = (3,4)
        self.w = 5
        self.h = 1
    def GetExtent(self):
        return (self.loc[0],self.loc[0]+self.w,self.loc[1],self.loc[1]+self.h)

class Shape:
    def BoundingBox(self):
        return NotImplementedError("missing")
    def CreateManipulator(self):
        return NotImplementedError("missing")

class Line(Shape):
    def __init__(self,coord0,coord1):
        self.x0, self.y0 = coord0
        self.x1, self.y1 = coord1
    def BoundingBox(self):
        return self.x0, self.y0, self.x1, self.y1

class TextShape(Shape):
    def __init__(self,txt,coord0):
        self.text = TextView(txt=txt)
        self.x0, self.y0 = coord0
        self.x1, self.y1 = (None,None)
    def BoundingBox(self):
        ''' here, code's adapted to work from a different class into Shape class '''
        e = self.text.GetExtent() # format is (x0,x1,y0,y1)
        self.x0, self.x1, self.y0, self.y1 = e
        return self.x0, self.y0, self.x1, self.y1