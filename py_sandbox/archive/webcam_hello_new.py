'''
source:
https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_gui/py_video_display/py_video_display.html
'''

# INITIALIZATIONS //////////////////////////////////////////////////////////////
import numpy as np
import cv2
from sys import argv

# pick video source
if(argv[1].isdigit()):
	vidsrc=int(argv[1])
else:
	print 'ERROR: argument expected as integer'
	exit()

# initialize functions
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

def changeResolution(feed,newheight=10000,newwidth=10000):
	cap.set(cv2.CAP_PROP_FRAME_WIDTH, newheight)
	cap.set(cv2.CAP_PROP_FRAME_HEIGHT,newwidth)
	return 0


# MAIN PROGRAM /////////////////////////////////////////////////////////////////
# # # # # # #

cap = cv2.VideoCapture(vidsrc)

changeResolution(cap,1080)

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()

	# frame operations
	drawLines(frame,10,color=(0,255,0)) # draw evenly spaced horizontal lines (green)
	drawLines(frame,1,'v') # draw bisecting vertical line
	
	# Display the resulting frame
	cv2.imshow('frame',frame)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()