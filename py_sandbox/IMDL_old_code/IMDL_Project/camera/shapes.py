#!/bin/python

# attempt to contours with shape recognition

import cv2
import numpy as np
from time import sleep
from time import time
showControls=1
def nothing(x):
    pass
ini=[0,0,0,179,255,255] # orange balloon
hL=ini[0]
sL=ini[1]
vL=ini[2]
hU=ini[3]
sU=ini[4]
vU=ini[5]
if(showControls==1):
	ht=200
	wd=512
	img=np.zeros((ht,wd,3), np.uint8)
	cv2.namedWindow('image')
	#make  trackbars for upper / lower ranges
	    #lower range
	cv2.createTrackbar('H lower','image',0,179,nothing)
	cv2.createTrackbar('S lower','image',0,255,nothing)
	cv2.createTrackbar('V lower','image',0,255,nothing)
	    #upper range
	cv2.createTrackbar('H upper','image',0,179,nothing)
	cv2.createTrackbar('S upper','image',0,255,nothing)
	cv2.createTrackbar('V upper','image',0,255,nothing)

	# #initialize trackbar positions


	cv2.setTrackbarPos('H lower','image',ini[0])
	cv2.setTrackbarPos('S lower','image',ini[1])
	cv2.setTrackbarPos('V lower','image',ini[2])
	cv2.setTrackbarPos('H upper','image',ini[3])
	cv2.setTrackbarPos('S upper','image',ini[4])
	cv2.setTrackbarPos('V upper','image',ini[5])
	# set color window palettes
	tL=(10,10)
	bR=(wd/2-10,ht-10)
	tL2=(wd/2+10,10)
	bR2=(wd-10,ht-10)



ratio=0.5 #note, 1 = 1:1 ratio
blurVal=19 #should be a positive odd number
morphVal=11 #should be a positive odd number


cap = cv2.VideoCapture(0) #select video source

while(1):

	if(showControls==1):
		# controls window
		cv2.imshow('image',img)
		#track set 1 - lower
		hL = cv2.getTrackbarPos('H lower','image')
		sL = cv2.getTrackbarPos('S lower','image')
		vL = cv2.getTrackbarPos('V lower','image')    
		hsvL=np.uint8([[[hL,sL,vL]]])   #trans to BGR
		bgrL=cv2.cvtColor(hsvL,cv2.COLOR_HSV2BGR)
		b_L=int(bgrL[0][0][0])
		g_L=int(bgrL[0][0][1])
		r_L=int(bgrL[0][0][2])
		    #track set 1 - upper
		hU = cv2.getTrackbarPos('H upper','image')
		sU = cv2.getTrackbarPos('S upper','image')
		vU = cv2.getTrackbarPos('V upper','image')    
		hsvU=np.uint8([[[hU,sU,vU]]])   #trans to BGR
		bgrU=cv2.cvtColor(hsvU,cv2.COLOR_HSV2BGR)
		b_U=int(bgrU[0][0][0])
		g_U=int(bgrU[0][0][1])
		r_U=int(bgrU[0][0][2])
		#plot everything
		img[:]=0 #set controls bkgd to black
		cv2.rectangle(img,tL,bR,(b_L,g_L,r_L),-1) #plot rect1
		cv2.rectangle(img,tL2,bR2,(b_U,g_U,r_U),-1)    #plot rect2

	_, frameOrig = cap.read()
	camAngle=0
	try:
		# Resize the captured frame
		frameOrig = cv2.resize(frameOrig,None,fx=ratio, fy=ratio,
						   interpolation = cv2.INTER_AREA)
	except:
		print "resize error"

	cv2.imshow('raw',frameOrig) #video frame
	#need: mask of area only where cross is
	frame1=cv2.cvtColor(frameOrig,cv2.COLOR_BGR2GRAY)
	frame2=cv2.cvtColor(frameOrig,cv2.COLOR_BGR2GRAY)

	hsv=cv2.cvtColor(frameOrig,cv2.COLOR_BGR2HSV) #create HSV version #need fix here...
	# bb,gg,rr=cv2.split(frame)
	lower=np.array([hL,sL,vL])
	upper=np.array([hU,sU,vU])

	# hsv image
	frameHSV=cv2.inRange(hsv,lower,upper) #this is the true result

	# normal binary image
	ret,thresh1 = cv2.threshold(frame1,50,255,cv2.THRESH_BINARY)
	
	#get image of cross, in white w/ black background. plus noise
	ret,thresh2=cv2.threshold(frame2,100,255,cv2.THRESH_BINARY_INV)

	# show everything
	cv2.imshow('binary',thresh1) #video frame
	cv2.imshow('binary_inv',thresh2) #video frame
	cv2.imshow('hsv',frameHSV)


	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
