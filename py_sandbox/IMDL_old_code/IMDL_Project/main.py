'''
objective: make the beaglebone a specialized 
sensor that looks through the camera, 
decides whether an object is detected, and tells
the teensy at what angle the desired object iss
'''

# INCLUDED MODULES ########################################
import Adafruit_BBIO.GPIO as gpio
import Adafruit_BBIO.ADC as adc
import Adafruit_BBIO.PWM as pwm
import cv2
import numpy as np
from time import sleep
from time import time
import kj
import serial
import Adafruit_BBIO.UART as UART

# initializations
showWindow=0 #0=none, 1 = only results window, 2 = all
onComputer=0

greenTarg=[35,50,141,52,255,255]
pinkTarg=[106,85,96,179,255,219]

ratio=0.5 #note, 1 = 1:1 ratio
blurVal=19 #should be a positive odd number
morphVal=11 #should be a positive odd number

gpio.cleanup()
pwm.cleanup()

# functions critical for trackbars
def nothing(x):
    pass
def saveValues(arr):
	saveFile = open('savedThresh','w')
	for i in range(len(arr)):
		saveFile.write(str(arr[i])+'\n')
	saveFile.close()
def openValues():
	openFile=open('savedThresh','r')
	arr=range(6)
	j=0
	for i in openFile:
		arr[j]=int(i)
		j+=1
	openFile.close()	
	return arr

#set controls window parameters
if(showWindow>1): 
	
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

	ini=[0,0,0,179,255,255] # orange balloon
	ini=openValues()
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


# FUNCTIONS ###############################################
def debugDONE():
	while(1):
		sleep(2)
		print "DONE"
def angleError(raw_cx,FrameWidth):
	cc=float(raw_cx)
	va=float(75) #degrees
	fw=float(FrameWidth)
	return va/fw*(cc-fw)+va/2
def camHelper(color):
	hL=color[0]
	sL=color[1]
	vL=color[2]
	hU=color[3]
	sU=color[4]
	vU=color[5]

	_, frame = cap.read()
	camAngle=0
	try:
		# Resize the captured frame
		frame = cv2.resize(frame,None,fx=ratio, fy=ratio,
						   interpolation = cv2.INTER_AREA)
	except:
		print "resize error"
	frameOrig=frame

	#blur with Gauss
	frame=cv2.GaussianBlur(frame,(blurVal,blurVal),0)
	
	# save only colors in desired range
	# try:
	hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #create HSV version #need fix here...
	bb,gg,rr=cv2.split(frame)
	lower=np.array([hL,sL,vL])
	upper=np.array([hU,sU,vU])
	frame=cv2.inRange(hsv,lower,upper) #this is the true result
	#get from HSV to Grayscale

	frameGray=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR) #back to BGR version
	frameGray=cv2.cvtColor(frameGray,cv2.COLOR_BGR2GRAY) #now to Grayscale
	

	#erode then dilate, aka open the image
	kernel = np.ones((morphVal,morphVal),np.uint8)
	frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel)

	# combine and threshold
	frame=cv2.bitwise_and(frameGray,frameGray,mask=frame)
	# cv2.imshow('debug',frame)
	# now make everything not-black into white.
	ret,frame2=cv2.threshold(frame,0,255,cv2.THRESH_BINARY)
	# cv2.imshow('debug2',frame2)
	# find contours in the image
	contours, hierarchy = cv2.findContours(frame2,
		cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


	# get frame properties			
	imgH=frameOrig.shape[0]
	imgW=frameOrig.shape[1]

	# find moments, get centroid (as long as there are contours)
	if(len(contours)==0):
		# if no contours detected
		print "none found"
	else:
		#if contours are detected...

		# find largest contour
		i=0
		j=0 #find largest contour, the jth value
		for i in range(len(contours)):
			if(cv2.contourArea(contours[j])<cv2.contourArea(contours[i])):
				j=i
		# with index of largest, now make centroid around it! :D

		#calibrate for when object is within 3ft (area size based)
		# only count if the object is larger than ... 350sqpx
	
		(xcirc,ycirc),rcirc=cv2.minEnclosingCircle(contours[j])
		center = (int(xcirc),int(ycirc))
		if(cv2.contourArea(contours[j])>350):
			# only consider the object valid if larger than 350sqpx
			camAngle=int(angleError(xcirc,imgW))
		else:
			camAngle=0

	if(showWindow>0):
		try:
			# draw...
			cv2.drawContours(frameOrig,contours,-1,(0,255,0),2) #contours
			cv2.circle(frameOrig,center,int(rcirc),(0,0,255),2) # bounding circle
			cv2.line(frameOrig,(imgW/2,imgH/2),center,(0,0,255),2) #err line
			# and show it all on...
			cv2.imshow('contours',frameOrig) #video frame
		except:
			print "VideoFrameError"

	return int(camAngle)

def getCamData(color):
	# input: camera video
	# output: avg/stdev of processed images
	# purpose: simplify question of whether the target \
	#	waypoint has been identified.
	a=range(0,10)
	for i in range(0,10):
		a[i]=camHelper(color)
		# print a[i] # for debugging
	a_avg=kj.avg(a)
	a_std=kj.stdev(a)
	return (a_avg,a_std)
def serialReceive():
	# input: serial data from Teensy
	# output: parsed integer values
	# purpose: facilitate communication between
	#	boards. only expect to receive uint8 
	# 	values from the teensy

	# read data (assumes available)
	strInfo=ser.readline()
	strInfo=strInfo[0:len(strInfo)-1]
	from string import count
	vars=range(count(strInfo,',')+1)
	i=0;
	prev=0;
	n=len(strInfo)
	cc=0
	while(i<n):
		if(strInfo[i]==','):
			# print cc
			vars[cc]=int(strInfo[prev:i])
			prev=i+1
			cc+=1
		i+=1
	vars[cc]=int(strInfo[prev:i])
	return vars
def serialSend(arr):
	for i in range(0,len(arr)-1):
		ser.write(str(arr[i])+',')
	i+=1
	ser.write(str(arr[i])+'!') # note: terminate with '!'


# PIN DEFINES #############################################

# OUTPUTS
pin_green = "P8_7"
pin_yellow = "P8_8"
pin_red = "P8_14"
pin_blue = "P8_15"
cols=[pin_green,pin_yellow,pin_red,pin_blue]

# INPUTS
pin_button = "P8_17"


# SETUP ###################################################
# note: set globals here 
if(onComputer==0):
	# if not on computer, do below
	gpio.setup(pin_green,1)
	gpio.setup(pin_yellow,1)
	gpio.setup(pin_red,1)
	gpio.setup(pin_blue,1)
	gpio.setup(pin_button,0)
	gpio.add_event_detect(pin_button,gpio.BOTH)

	adc.setup()
	kj.ledINIT()
	UART.setup("UART1")
	ser=serial.Serial(port = "/dev/ttyO1",baudrate=115200)
	ser.close()
	ser.open()
	ser.flushInput()
	ser.flushOutput()


	# i=0
	# while(1):
	# 	kj.led(i,1)
	# 	sleep(0.5)
	# 	kj.led(i,0)
	# 	i+=1
	# 	if(i==3): 
	# 		i=0

# OPEN CV SETUP:

contourTarg=[0,23,72,26,255,255]
Target=[greenTarg,pinkTarg,contourTarg]
focus=0
temp=[0,23,72,26,255,255]

cap = cv2.VideoCapture(0) #select video source

color=2 # color index for hsv values


# get everything moving	
if(onComputer==0):
	ser.write(str(1)+',')

# MAIN LOOP ###############################################
tstart=time() #get start time
elapsed=tstart-time()
while(1):
	# objectives: 
	# check camera, send (camera angle), receive color, <change LED's (not yet)>, repeat

	# step 1: check camera
	if(showWindow>1):
		camData=camHelper(temp) #debugging purposes
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
		temp=[hL,sL,vL,hU,sU,vU]
	else:
		camData=camHelper(Target[focus])
		print camData

		# auto switch values between green and pink
		# elapsed=time()-tstart
		# if(elapsed>2):
		# 	#switch targets
		# 	if(focus==0):
		# 		focus=1
		# 		mainTarg=pinkTarg
		# 		# print "switch"
		# 	elif(focus==1):
		# 		focus=0
		# 		mainTarg=greenTarg
		# 		# print "switch"
		# 	tstart=time() #reset timer


	# step 2: send / receive data
	if(onComputer==0):
		ser.write(str(camData)+',')

		if(ser.inWaiting()>0):
			focus=int(ser.readline())




#	serialSend([0,camData,0]) # (state, camData, buttonState)

	# step 3:receive data
#	TnsData=serialReceive()
#	print TnsData	

	# sleep(4) # wait a few seconds before next check (have to slow down robot for that)

	# DO NOT TOUCH, KEEP AT END OF FORLOOP
	# KEEP ENABLED WHEN SHOWING WINDOWS
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
# MAIN END ################################################

# ENABLE BELOW TO SHOW WINDOW
if(showWindow>0):
	cv2.destroyAllWindows()
	saveValues(temp)
gpio.cleanup()
pwm.cleanup()
# if the kernel ever gets fixed, enable this code
# UART.cleanup()

