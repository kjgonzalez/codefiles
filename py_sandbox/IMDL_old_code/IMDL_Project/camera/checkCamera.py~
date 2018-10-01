# python code to ensure that 
# this is at least working on this computer.
# objective: show the camera with a dot in the middle

'''
1. grab camera frame
2. show frame
3. plot small circle in middle of frame
'''

import cv2
import numpy as np
import time


cv2.namedWindow('video')
cap = cv2.VideoCapture(0)

	

while(1): 

	_,frame = cap.read()
	cv2.circle(frame,(40,40),4,(0,0,255),-1)

	cv2.imshow('video',frame)
	
	
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
