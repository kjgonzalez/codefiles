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
from buffer_class import Buffer

##############################
vidsrc=1
ratio=0.5
# main =========================================================================

cap = cv2.VideoCapture(vidsrc)
B2G=cv2.COLOR_BGR2GRAY
cap_fps=cap.get(cv2.CAP_PROP_FPS)
cap_ht=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
cap_wd=cap.get(cv2.CAP_PROP_FRAME_WIDTH)


def quickTransform(cv2_img):
    B2G=cv2.COLOR_BGR2GRAY
    x=cv2.cvtColor(cv2_img,B2G)
    x=cv2.resize(x,(0,0),fx=0.5,fy=0.5)
    x=cv2.GaussianBlur(x,(21,21),0)
    return x

def qs(cv_img):
    cv2.imshow('.',cv_img)
    cv2.waitKey(0)
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

buff=Buffer(30) # store 1 second (30frames) 
# getBuffer, length, toBuffer
for i in range(30):
    # throw out first few frames of video
    raw=cv2.resize(cap.read()[1],(0,0),fx=ratio,fy=ratio)
    frame0=quickTransform(raw)

detected=False
ht,wd,_=raw.shape
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# control filename, 'fourcc' format, fps, and resolution
out = cv2.VideoWriter('output.avi',fourcc, cap_fps, (int(wd),int(ht)))

while(not detected):
    # Capture frame-by-frame
    ret,raw=cap.read()
    
    raw=cv2.resize(raw,(0,0),fx=ratio,fy=ratio)
    buff.toBuffer(raw)
    
    frame = quickTransform(raw)
    frameDelta=cv2.absdiff(frame0,frame)
    print(frameDelta.max())
    
    # frame-to-frame, if there's no change greater than 10, keep new frame as reference
    if(frameDelta.max()<5):
        frame0=frame
    
    if(frameDelta.max()<30):
        # nothing there
        text='empty'
        color=(0, 255, 0)
        detected=False
    else:
        # something there
        text='detected'
        color=(0, 0, 255)
        detected=True
        break

    raw_disp=np.copy(raw)
    cv2.putText(raw_disp, "Room Status: {}".format(text), (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # not really needed, but will keep anyway
    # thresh=cv2.threshold(frameDelta,25,255,cv2.THRESH_BINARY)[1]
    # thresh = cv2.dilate(thresh, None, iterations=2)
    
    cv2.imshow('raw',raw_disp)
    cv2.imshow('delta',frameDelta)
    # cv2.imshow('thresh',thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()

for iframe in buff.getBuffer():
    out.write(iframe)


while(detected):
    # Capture frame-by-frame
    ret,raw=cap.read()
    
    raw=cv2.resize(raw,(0,0),fx=ratio,fy=ratio)
    out.write(raw)
    frame = quickTransform(raw)
    frameDelta=cv2.absdiff(frame0,frame)
    print(frameDelta.max())
    
    # frame-to-frame, if there's no change greater than 10, keep new frame as reference
    if(frameDelta.max()<5):
        frame0=frame
    
    if(frameDelta.max()<30):
        # nothing there
        text='empty'
        color=(0, 255, 0)
        detected=False
        break
    else:
        # something there
        text='detected'
        color=(0, 0, 255)
        detected=True

    raw_disp=np.copy(raw)
    cv2.putText(raw_disp, "Room Status: {}".format(text), (10, 20),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

    # not really needed, but will keep anyway
    # thresh=cv2.threshold(frameDelta,25,255,cv2.THRESH_BINARY)[1]
    # thresh = cv2.dilate(thresh, None, iterations=2)
    
    cv2.imshow('raw',raw_disp)
    cv2.imshow('delta',frameDelta)
    # cv2.imshow('thresh',thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
out.release()


