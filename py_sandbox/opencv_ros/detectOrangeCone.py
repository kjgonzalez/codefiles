'''
Author: Kris Gonzalez
DateCreated: 180320
Objective: use some sort of classical engineering for blob detection. load the 
	cone image and detect the orange cone

todo: update this code for py3, modernize (KJG20220616)

'''

import numpy as np
import cv2
from sys import argv
import tkinter as Tkinter

def resize2(imgname,Screen2ImageRatio=2):
	''' Objective: provide SUPER simple way to resize an image relative to size
		of the active / main screen. The ratio is only an upper bound; the image
		is not resized if it is smaller than a ratio of the screen dimensions. 
		However, if it is larger, the image is resized.
	'''
	
	root = Tkinter.Tk()
	sc_dim = (root.winfo_screenheight(),root.winfo_screenwidth())
	
	im_dim = imgname.shape[:2]
	if(im_dim[0]*Screen2ImageRatio>sc_dim[0]):
		# shrink by height ratio
		f = float(sc_dim[0])/(Screen2ImageRatio*float(im_dim[0]))
		return cv2.resize(imgname,(0,0),fx=f,fy=f,)
	elif(im_dim[1]*Screen2ImageRatio>sc_dim[1]):
		# shrink by width ratio
		f = float(sc_dim[1])/(Screen2ImageRatio*float(im_dim[1]))
		return cv2.resize(imgname,(0,0),fx=f,fy=f)
	else:
		return imgname
# def resize2
def nothing(x):
	'Objective: enable working of trackbars (not sure why needed)'
	pass
# def nothing

# CONTROL SECTION ##############################################################
vid_src = 1 # 0=built-in, 1=usb camera
null=      [0,0,0,255,255,255] # trackbar init lo/hi values
ini_orange=[0,104,206,23,255,255]
ini_blue=  [102,115,124,109,255,255]
ini_green= [58,49,77,80,255,255]
ini_yellow=[24,105,0,30,255,255]

ini_track=ini_orange

# CTRL END #####################################################################


# INITIALIZATIONS ################################

# send user message to bash: 
print('end program with ESC')

# load image
#pre = cv2.imread(argv[1])
pre = cv2.imread('imgs/zoom.jpg')
pic = resize2(pre)
# open video stream
cap = cv2.VideoCapture(vid_src)

#show image
cv2.imshow('thing',pic)

# with simple image load, would show this portion
#cv2.waitKey(0)
#cv2.destroyAllWindows()


# initialize trackbars / trackbar control window
wd=500
ht=100
canvas=np.zeros((ht,wd,3), np.uint8)
cv2.namedWindow('image')
# (255,125,73) rgb
#make  trackbars for upper / lower ranges
    #lower range
cv2.createTrackbar('H lower','image',0,179,nothing)
cv2.createTrackbar('S lower','image',0,255,nothing)
cv2.createTrackbar('V lower','image',0,255,nothing)
    #upper range
cv2.createTrackbar('H upper','image',0,179,nothing)
cv2.createTrackbar('S upper','image',0,255,nothing)
cv2.createTrackbar('V upper','image',0,255,nothing)

#initialize trackbar positions
cv2.setTrackbarPos('H lower','image',ini_track[0])
cv2.setTrackbarPos('S lower','image',ini_track[1])
cv2.setTrackbarPos('V lower','image',ini_track[2])
cv2.setTrackbarPos('H upper','image',ini_track[3])
cv2.setTrackbarPos('S upper','image',ini_track[4])
cv2.setTrackbarPos('V upper','image',ini_track[5])


#create trackbar, called H, in window image, w/ range (0,255), pass nothing
    #create sample color boxes
tL=(10,10)
bR=(wd/2-10,ht-10)

tL2=(wd/2+10,10)
bR2=(wd-10,ht-10)


while(1):

	#controls setup / plotting
	cv2.imshow('image',canvas)
		#track set 1 - lower
	h_L = cv2.getTrackbarPos('H lower','image')
	s_L = cv2.getTrackbarPos('S lower','image')
	v_L = cv2.getTrackbarPos('V lower','image')    
	hsvL=np.uint8([[[h_L,s_L,v_L]]])   #trans to BGR
	bgrL=cv2.cvtColor(hsvL,cv2.COLOR_HSV2BGR)
	b_L=int(bgrL[0][0][0])
	g_L=int(bgrL[0][0][1])
	r_L=int(bgrL[0][0][2])
		#track set 1 - upper
	h_U = cv2.getTrackbarPos('H upper','image')
	s_U = cv2.getTrackbarPos('S upper','image')
	v_U = cv2.getTrackbarPos('V upper','image')    
	hsvU=np.uint8([[[h_U,s_U,v_U]]])   #trans to BGR
	bgrU=cv2.cvtColor(hsvU,cv2.COLOR_HSV2BGR)
	b_U=int(bgrU[0][0][0])
	g_U=int(bgrU[0][0][1])
	r_U=int(bgrU[0][0][2])
		#plot everything
	canvas[:]=0 #set controls bkgd to black
	cv2.rectangle(canvas,tL,bR,(b_L,g_L,r_L),-1) #plot color rect1
	cv2.rectangle(canvas,tL2,bR2,(b_U,g_U,r_U),-1)    #plot color rect2

	# operations on the frame ####################
	
	# capture a raw frame
	_, frame = cap.read()
	ratio=0.75
	# resize a the frame
	frame = cv2.resize(frame,None,fx=ratio, fy=ratio, interpolation = cv2.INTER_AREA)
	
	# Convert frame from BGR to HSV
	hsv = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV) # kjg: frame>>pic

	lower = np.array([h_L,s_L,v_L])
	upper = np.array([h_U,s_U,v_U])

	# Threshold the HSV image to get only colors in hsv range
	mask = cv2.inRange(hsv, lower, upper)
	#note that the mask is the one with the interest region in white

	# Bitwise-AND mask and original image
	res = cv2.bitwise_and(pic,pic, mask= mask)

	#cv2.imshow('frame',frame)
	#cv2.imshow('mask',mask)
	cv2.imshow('res',res)

	# exit code
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()


