import cv2
import numpy as np
import time
sleep = time.sleep
gpio.cleanup()
pwm.cleanup()


# FUNCTIONS ###############################################
def debugDONE():
	while(1):
		time.sleep(2)
		print "DONE"

def camHelper(color):
	hL=color[0]
	sL=color[1]
	vL=color[2]
	hU=color[3]
	sU=color[4]
	vU=color[5]
	ratio=0.75 #note, 1 = 1:1 ratio
	blurVal=5 #should be a positive odd number
	morphVal=11 #should be a positive odd number



	def angleError(raw_cx,FrameWidth):
		cc=float(raw_cx)
		va=float(75) #degrees
		fw=float(FrameWidth)
		return va/fw*(cc-fw)+va/2

	_, frame = cap.read()
	camAngle=0
	# Resize the captured frame
	frame = cv2.resize(frame,None,fx=ratio, fy=ratio,
					   interpolation = cv2.INTER_AREA)
	frameOrig=frame

	#blur with Gauss
	frame=cv2.GaussianBlur(frame,(blurVal,blurVal),0)

	# save only colors in desired range
	try:
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
			imgH=frameOrig.shape[0] #don't need this one
			imgW=frameOrig.shape[1]
			# create bounding circle
			(xcirc,ycirc),rcirc=cv2.minEnclosingCircle(cnt) #returns a float
			center = (int(xcirc),int(ycirc))
			cv2.circle(frameOrig,center,int(rcirc),(255,0,0),1)
			# camAngle=5
			#create 2D error line
			cv2.line(frameOrig,(imgW/2,imgH/2),(int(xcirc),int(ycirc)),(255,0,255),1)
			camAngle=angleError(xcirc,imgW)

		# END OF IMAGE PROCESSING #############################
	except:
		print "ColorspaceError"
		# camAngle=100


	try:
		cv2.imshow('contours',frameOrig)
	except:
		print "VideoFrameError"

	return int(camAngle)
def getCamAngle(color):
	# input: camera video
	# output: avg/stdev of processed images
	# purpose: simplify question of whether the target \
	#	waypoint has been identified.
	a=range(0,10)
	for i in range(0,10):
		a[i]=camHelper(color)
		print a[i] # for debugging
	a_avg=kj.avg(a)
	a_std=kj.stdev(a)
	return (a_avg,a_std)




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
# note: can set globals here

gpio.setup(pin_green,1)
gpio.setup(pin_yellow,1)
gpio.setup(pin_red,1)
gpio.setup(pin_blue,1)
gpio.setup(pin_button,0)
gpio.add_event_detect(pin_button,gpio.BOTH)

adc.setup()
kj.ledINIT()

t=time.time()*1000

# OPEN CV SETUP:
ball1=[14,66,135,23,255,255] # orange balloon
ball2=[17,90,114,25,255,201] #pink balloon
ball3=[41,139,39,75,255,125]#green baloon
balls=[ball1,ball2,ball3] #list of all colors

# ini=ball1

# hL2=ini[0]
# sL2=ini[1]
# vL2=ini[2]
# hU2=ini[3]
# sU2=ini[4]
# vU2=ini[5]

cv2.namedWindow('contours')
cap = cv2.VideoCapture(0) #select video source
# getCameraAngle() # initialize 



color=balls[0]
hL=color[0]
sL=color[1]
vL=color[2]
hU=color[3]
sU=color[4]
vU=color[5]



# MAIN LOOP ###############################################
while(1):
	#	print camHelper(balls[0])
	ratio=1 #note, 1 = 1:1 ratio
	blurVal=5 #should be a positive odd number
	morphVal=11 #should be a positive odd number
	camAngle=0


	def angleError(raw_cx,FrameWidth):
		cc=float(raw_cx)
		va=float(75) #degrees
		fw=float(FrameWidth)
		return va/fw*(cc-fw)+va/2

	_, frame = cap.read()

	# Resize the captured frame
	frame = cv2.resize(frame,None,fx=ratio, fy=ratio,
					   interpolation = cv2.INTER_AREA)
	frameOrig=frame

	#blur with Gauss
	frame=cv2.GaussianBlur(frame,(blurVal,blurVal),0)

	# save only colors in desired range
	try:

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
				print "ValueError: loc set to 0"
				loc=0

			# ensure never go out of bounds
			if(loc>len(contours)):
				print "OutOfBoundsError: loc set to zero"
				loc=0

			cnt=contours[loc]

			# get frame properties			
			imgH=frameOrig.shape[0] #don't need this one
			imgW=frameOrig.shape[1]
			# create bounding circle
			(xcirc,ycirc),rcirc=cv2.minEnclosingCircle(cnt) #returns a float
			center = (int(xcirc),int(ycirc))
			cv2.circle(frameOrig,center,int(rcirc),(255,0,0),1)
			# camAngle=5
			#create 2D error line
			cv2.line(frameOrig,(imgW/2,imgH/2),(int(xcirc),int(ycirc)),(255,0,255),1)
			camAngle=angleError(xcirc,imgW)
		# END OF IMAGE PROCESSING #############################
	except:
		print "ColorspaceError"

	try:
		cv2.imshow('contours',frameOrig)
		print "debug2"
	except:
		print "VideoFrameError"
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
# MAIN END ################################################
cv2.destroyAllWindows()
gpio.cleanup()
pwm.cleanup()