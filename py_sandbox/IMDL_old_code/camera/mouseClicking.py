#SAY WHAT KIND OF EVENT IT NEEDS TO BE HERE:
#00- EVENT_FLAG_ALTKEY
#01- EVENT_FLAG_CTRLKEY
#02- EVENT_FLAG_LBUTTON
#03- EVENT_FLAG_MBUTTON
#04- EVENT_FLAG_RBUTTON
#05- EVENT_FLAG_SHIFTKEY
#06- EVENT_LBUTTONDBLCLK
#07- EVENT_LBUTTONDOWN
#08- EVENT_LBUTTONUP
#09- EVENT_MBUTTONDBLCLK
#11- EVENT_MBUTTONDOWN
#12- EVENT_MBUTTONUP
#13- EVENT_MOUSEMOVE
#14- EVENT_RBUTTONDBLCLK
#15- EVENT_RBUTTONDOWN
#16- EVENT_RBUTTONUP

import cv2
import numpy as np
from matplotlib import pyplot as plt
from common import clock, draw_str

drawing = False # true if mouse is pressed
ix,iy = -1,-1
counter=0
createWin=False

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,moving,createWin
    circleRadius=10
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        moving = True
        ix,iy=x,y


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        moving = False
        createWin=True
###

# histogram function definition
def hist_curv(im):
	h = np.zeros((300,256,3))
	if len(im.shape)==2:
		color=[(255,255,255)]
	elif im.shape[2]==3:
		color = [(255,0,0),(0,255,0),(0,0,255)]
	for ch,col in enumerate(color):
		hist_item = cv2.calcHist([im],[ch],None,[256],[0,256])
		cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
		hist=np.int32(np.around(hist_item))
		pts = np.int32(np.column_stack((bins,hist)))
		cv2.polylines(h,[pts],False,col)
	y=np.flipud(h)
	return y

def hist_lines(im):
	h=np.zeros((300,256,3))
	if len(im.shape)!=2:
		print "hist_lines applicable only for grayscale images"
		im = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
	hist_item = cv2.calcHist([im],[0],None,[256],[0,256])
	cv2.normalize(hist_item,hist_item,0,255,cv2.NORM_MINMAX)
	hist=np.int32(np.around(hist_item))
	for x,y in enumerate(hist):
		cv2.line(h,(x,0),(x,y),(255,255,255))
	y = np.flipud(h)
	return y
# no more opencv-version of histogram stuff






img = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)



cap = cv2.VideoCapture(0) #select video source

# MAIN LOOP ################################################

box=41 # Mouse Selection Box
ROIb=0 #initialize ROI colors
ROIg=0
ROIr=0

while(1):
	_, img = cap.read()

	if(drawing==True and moving==True):
		# cv2.circle(img,(ix,iy),10,(0,0,255),2)
		cv2.rectangle(img,(ix-(box-1)/2,iy-(box-1)/2),\
			(ix+(box-1)/2,iy+(box-1)/2),(0,0,255),1)
	cv2.rectangle(img,(1,1),(50,50),(ROIb,ROIg,ROIr),-1)
	
	draw_str(img, (20, 20), str(counter))


	# make window of ROI that was clicked when the mouse was lifted
	if(createWin==True):	
		xMin=ix-(box-1)/2
		xMax=ix+(box-1)/2
		yMin=iy-(box-1)/2
		yMax=iy+(box-1)/2
		roi=img[yMin:yMax,xMin:xMax]
		# roi=cv2.GaussianBlur(roi,(5,5),0)
		roi=cv2.blur(roi,(15,15))
		ROIb,ROIg,ROIr,_=cv2.mean(roi)
		print ROIb,ROIg,ROIr
		cv2.imshow('roi',roi)
		createWin=False
		

	try: 
		cv2.imshow('image',img)
	except:
		print "VideoFrameError"

	k = cv2.waitKey(1) & 0xFF
	if k == ord('m'):
	    counter=counter+1
	elif k == 27:
	    break

cv2.destroyAllWindows()
