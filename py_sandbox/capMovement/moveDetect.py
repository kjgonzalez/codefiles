'''
objective: capture a certain number of frames and keep in buffer, while also recording the first 5 seconds that something shows up.

will break up into steps: 
1. just open up webcam
4. be able to detect movement
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
vidsrc=0

# main =========================================================================

cap = cv2.VideoCapture(vidsrc)
B2G=cv2.COLOR_BGR2GRAY
fold=cv2.cvtColor(cap.read(),B2G) # older 
fnew=copy.copy(fold)  
while(True):
    fold=copy.copy(fnew)
    # Capture frame-by-frame
    
    ret, fnew = cap.read()
    
    cv2.imshow('frame',fnew)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()