'''
Author: Kris Gonzalez
Date Created: 180418
Objective: basic webcam hello world, but with a few augmentations. for one, 
	displays horizontal and vertical bisecting lines.
	

Source:
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html



'''
import numpy as np
import cv2
from sys import argv




if(argv[1].isdigit()):
	vidsrc=int(argv[1])
else:
	print 'ERROR: argument expected as integer'
	exit()

def drawLines(frame,nLines=1,orient='h',color=(0,0,255)):
	'''
	Objective: draw evenly-spaced lines on screen. will start with 
		horizontal ones.
	'''
	import cv2
	import numpy as np
	ht=frame.shape[0]
	wd=frame.shape[1]
	if(orient=='h'):
		step = int(float(ht)/float(nLines+1)) # spacing between lines
	elif(orient=='v'):
		step = int(float(wd)/float(nLines+1)) # spacing between lines
	for i in range(nLines):
		# first is zero, so need to add 1
		if(orient=='h'):
			p1 = (0 ,step*(i+1)) # (x,y)
			p2 = (wd,step*(i+1))
		elif(orient=='v'):
			p1 = (step*(i+1),0) # (x,y)
			p2 = (step*(i+1),ht)
		cv2.line(frame,p1,p2,color)
	return 0 # done


cap = cv2.VideoCapture(vidsrc)

while(True):
	# Capture Frame-by-Frame /////////////////////////////////////////
	ret, frame = cap.read()
	
	# Frame operations ///////////////////////////////////////////////
	drawLines(frame,10)
	drawLines(frame,1,'v')
	
	
	
	
	# Display Result /////////////////////////////////////////////////
	cv2.imshow('frame',frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()