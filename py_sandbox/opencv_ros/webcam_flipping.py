'''
source:
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
'''
import numpy as np
import cv2
from sys import argv
import klib
assert klib.PYVERSION == 3, "Please use python version 3"
import argparse

p=argparse.ArgumentParser()
p.add_argument('--src',type=int,default=0,help='video source')
# p.add_argument('--s',type=str,default="it's a nice day",help='string to print')
p.add_argument('--hFlip',default=False,action='store_true',help='flip img about horizontal')
p.add_argument('--vFlip',default=False,action='store_true',help='flip img about vertical')
args=p.parse_args()

vidsrc=args.src

cap = cv2.VideoCapture(vidsrc)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    if(args.vFlip):
        # flip about vertical:
        frame=np.flip(frame,0)

    if(args.hFlip):
        # flip about vertical:
        frame=np.flip(frame,1)

    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    #cv2.imshow('frame',gray)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
