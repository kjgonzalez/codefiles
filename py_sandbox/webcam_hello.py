'''
source:
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
'''
import numpy as np
import cv2
from sys import argv
import klib
assert klib.PYVERSION == 3, "Please use python version 3"

if(argv[1].isdigit()):
	vidsrc=int(argv[1])
else:
	print('ERROR: argument expected as integer')
	exit()

cap = cv2.VideoCapture(vidsrc)
while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

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