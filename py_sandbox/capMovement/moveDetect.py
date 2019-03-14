'''
objective: capture a certain number of frames and keep in buffer, while also recording the first 5 seconds that something shows up.

source: https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/
will break up into steps: 
1. just open up webcam - done
4. be able to detect movement - done
2. record 2 seconds (60 frames)
3. be able to constantly put frames into buffer and throw out old frames
5. be able to have buffer that then writes and saves 2 seconds before movement is detected along with next 2 seconds of movement.
'''

# initializations ==============================================================
import cv2
import numpy as np
import os
import copy
import klib
assert klib.PYVERSION == 3, "Please use python version 3"

##############################
vidsrc=1

# main =========================================================================

cap = cv2.VideoCapture(vidsrc)
B2G=cv2.COLOR_BGR2GRAY
cap_fps=cap.get(cv2.CAP_PROP_FPS)
cap_ht=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

def quickTransform(cv2_img):
    B2G=cv2.COLOR_BGR2GRAY
    x=cv2.cvtColor(cv2_img,B2G)
    x=cv2.resize(x,(0,0),fx=0.5,fy=0.5)
    x=cv2.GaussianBlur(x,(21,21),0)
    return x


for i in range(30):
    # throw out first few frames of video
    frame0=quickTransform(cap.read()[1])

while(True):
    # Capture frame-by-frame
    raw=cap.read()[1]
    
    frame = quickTransform(raw)
    frameDelta=cv2.absdiff(frame0,frame)
    print(frameDelta.max())
    
    # frame-to-frame, if there's no change greater than 10, keep new frame as reference
    if(frameDelta.max()<5):
        frame0=frame
    
    if(frameDelta.max()<30):
        # nothing there
        text='empty'
    else:
        # something there
        text='detected'

    cv2.putText(raw, "Room Status: {}".format(text), (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)

    # not really needed, but will keep anyway
    # thresh=cv2.threshold(frameDelta,25,255,cv2.THRESH_BINARY)[1]
    # thresh = cv2.dilate(thresh, None, iterations=2)
    
    cv2.imshow('raw',raw)
    cv2.imshow('delta',frameDelta)
    cv2.imshow('thresh',thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()


