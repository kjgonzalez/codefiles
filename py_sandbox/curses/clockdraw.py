'''
try to plot a clock value based on given time
test area:

ABCDEF 

each character here takes up approx (20,26) px. ascii art must take this into account

'''

import math as m

def sind(deg): return m.sin(m.radians(deg))
def cosd(deg): return m.cos(m.radians(deg))


def clock_ascii(HHMMSS):
    # just for fun, print out clock in ascii art if possible
    pass
def ascii_circle(radius_char):
    '''
    # given character width, draw a circle using an asterisk (*)
    # get precise coords for ideal circle, bin to ascii positions
    # just print width
    
    make a circle, then bin in cells that fit the circle. needs 
      small enough step size to catch. maybe 1 deg?
    note: with <ir,ic> plane, 0deg is at bottom and goes ccw
    for r=4 circle:
      0deg >> cos(0) = 1 >> ir=3,ic=3
      90 >> 1,7
      180 >> 0,3
      270 >> 1,0
    '''
    r=radius_char

    arr=['-'*2*r for i in range(r)]
    
    for ideg in range(0,360,10):
        ir = r/2*(cosd(ideg)+1)
        ic = sind(ideg)*r+r
        ir2 = int(round(ir*(r-1)/r,0))
        ic2 = int(round(ic*(2*r-1)/(2*r),0))
        #print(ir2,ic2)
        a = arr[ir2]
        a = a[:ic2]+'*'+a[ic2+1:]
        arr[ir2]=a
        #print('test:',a)
        #print(ideg,end=' ')
    for irow in arr:
        print(irow)
    

    #print(' '*0+'*'+' '*(2*r-2)+'*')

if(__name__ == '__main__'):
    ascii_circle(10)
    #ascii_circle(10)
# 

