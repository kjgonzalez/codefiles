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

gpio.cleanup()
pwm.cleanup()
showWindow=1



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

	ratio=1 #note, 1 = 1:1 ratio
	blurVal=7 #should be a positive odd number
	morphVal=15 #should be a positive odd number




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

	# now make everything not-black into white.
	ret,frame2=cv2.threshold(frame,0,255,cv2.THRESH_BINARY)

	# find contours in the image
	contours, hierarchy = cv2.findContours(frame2,
		cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	# find moments, get centroid (as long as there are contours)
	if len(contours) > 0:

		# first, want to find the largest contour, by area:
		try:
			loc=contours.index(max(contours,key=cv2.contourArea))
		# print loc
		except ValueError:
			# print "ValueError: loc set to 0"
			loc=0

		# ensure never go out of bounds
		if(loc>len(contours)):
			# print "OutOfBoundsError: loc set to zero"
			loc=0

		cnt=contours[loc]

		# get frame properties			
		imgH=frameOrig.shape[0]
		imgW=frameOrig.shape[1]
		
		# hide all drawing items (DO NOT DELETE)
		# draw contours
		cv2.drawContours(frameOrig,contours,-1,(0,255,0),1)
		# create bounding circle
		(xcirc,ycirc),rcirc=cv2.minEnclosingCircle(cnt)
		center = (int(xcirc),int(ycirc))
		cv2.circle(frameOrig,center,int(rcirc),(0,0,255),2)
		# print int(angleError(xcirc,imgW))
		#create 2D error line
		cv2.line(frameOrig,(imgW/2,imgH/2),center,(0,0,255),2)
		camAngle=int(angleError(xcirc,imgW))
		# print camAngle

		# END OF IMAGE PROCESSING #############################
	# except:
	# 	print "ColorspaceError"
		# camAngle=100

	if(showWindow==1):
		try:
			cv2.imshow('contours',frameOrig)
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

def serialSendSingle(value):
	ser.write(str(value)+'!')


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

state=0


# OPEN CV SETUP:
orange=[7,189,90,25,255,255] # orange balloon
pink=[17,90,114,25,255,201] #pink balloon
green=[41,31,86,91,255,252]#green baloon
balls=[orange,pink,green] #list of all colors

if(showWindow==1):
	cv2.namedWindow('contours')
cap = cv2.VideoCapture(0) #select video source

color=2 # color index for hsv values


# MAIN LOOP ###############################################
while(1):
	# objectives: 
	# check camera, send (camera angle), receive color, <change LED's (not yet)>, repeat
	
	# step 1: check camera
	camData=camHelper(balls[color])
	print camData
#	if(camData[1]<10):
#		camData=camData[0]
#		print "now camData is ",camData
#	else:
#		camData=0

	# step 2: send data
	serialSendSingle(camData)
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
if(showWindow==1):
	cv2.destroyAllWindows()
gpio.cleanup()
pwm.cleanup()
# if the kernel ever gets fixed, enable this code
# UART.cleanup()
