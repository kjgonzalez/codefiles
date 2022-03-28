
'''
Author: Kris Gonzalez
DateCreated: 150416
Objective:
# python code to ensure that 
# this is at least working on this computer.
# objective: show the camera with a dot in the middle
1. grab camera frame
2. show frame
3. plot small circle in middle of frame

KJG180319:
will use this to practice a little bit with active data...
1. get frame size

'''

import cv2
import numpy as np
import time


cv2.namedWindow('video')
cap = cv2.VideoCapture(1)
print 'press q to exit'

_,frame = cap.read()
vidHeight = frame.shape[0]
vidWidth = frame.shape[1]

while(1): 

	_,frame = cap.read()
	cv2.circle(frame,(vidWidth/2,vidHeight/2),4,(0,0,255),-1)

	cv2.imshow('video',frame)
	
	
	k = cv2.waitKey(5) & 0xFF
	if k == ord('q'):
		break

cv2.destroyAllWindows()
