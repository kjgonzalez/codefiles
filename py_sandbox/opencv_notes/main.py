'''
Author: Kristian Gonzalez
DateCreated: 180321
Objective: Want to understand and possibly improve python opencv, to be used 
	for batch editing photos, especially those for the database building.

KJGNOTE: Will leave custom functions in-place instead of organizing at top, in
	order to give context in code.

Some sample operations that need to be understood and shown: 
* load an image to be manipulated
* save an image in memory back to disk
* resize
	- by ratio
	- to specific size
* crop a photo 
'''


# Initializations ##########################################
import cv2
import numpy as np
import os


# delete last script's output file(s)
for ifile in os.listdir('.'):
	if('delme' in ifile):
		os.remove(ifile)

# load image ###########################
filename='orig.JPG'
orig = cv2.imread(filename)

# resize image by ratio
res_ratio = cv2.resize(orig,(0,0),fx=0.1,fy=0.1)
# resize image by value
res_value = cv2.resize(orig,(400,400),(0,0))

# crop an image. cropping is just an equation, and origin is top-left
# note that matrix values work in YX coordinate system
a=orig.shape # get original's shape
crop1 = orig[0:300,0:500]

# will create custom crop function that centers a rectangle about a point and 
# 	stays within bounds of original image

def constrain(value,minVal,maxVal):
	''' Objective: return constrained value of value
	'''
	return min( maxVal, max(minVal,value) )

def cropCentered(image,centerYX=-1,wide=500,height=500):
	'''
	Objective: get an image and return a cropped rectangle based on a given
		center, width, and height. Cropped image is bounded by bounds of image,
		but will try to keep orignal size of bounding box.
	Assumptions: 
		- cv2 already imported
		- numpy as np already imported
	Arguments:
	  image: opencv image (numpy array)
	  centerXY: 2-value int tuple, (width,height) coordinates. e.g.: (10,15)
	  wide: desired width of crop rectangle
	  height: desired height of crop rectangle
	'''
	
	
	# first get image bounds
	a=image.shape
	origHt=a[0]
	origWd=a[1]
	# check if arguments were given, choose defaults if not
	if(centerYX == -1):
		# choose center of image
		centerYX = ( origHt/2 , origWd/2 )
	# get limits of crop, but constrain to image limits
	top = centerYX[0]-(height-height/2) #kjgnote: compress if used full-time
	top = constrain(top,0,origHt)
	left = centerYX[1]-(wide-wide/2)
	left = constrain(left,0,origWd)
	bottom = (top+height)
	bottom = constrain(bottom,0,origHt)
	right = (left+wide)
	right = constrain(right,0,origWd)
	final = image[ top:bottom,left:right]
	return final
# crop image using centered crop
crop2 = cropCentered(orig,wide=505,height=505)

## show image / results
#cv2.imshow('output',crop2)
#cv2.imshow('out2',res_ratio)

## save an image back to disk
#cv2.imwrite('delme.jpg',crop2)


#cv2.waitKey(0)
#cv2.destroyAllWindows()


# LEARNING ABOUT BLURS #####################################
# blur helps remove noise
# it also helps provide artificial variety when training 
# 	an algorithm
# 

# have already imported cv2, np, and os

filename = 'green_sample.jpg'
orig = cv2.imread(filename) # load new image to work with

# different blur items to consider:
# 		blur, boxFilter, bilateralFilter, GaussianBlur, medianBlur
#cv2.blur(src,ksize)
#cv2.boxFilter(src,ddepth,(ksize,ksize)) #hard to visually tell diff from 'blur'
#cv2.medianBlur(src,ksize) #makes things look more like an oil pastel or so
#cv2.bilateralFilter(src,d,sigmaColor) # more for offline work, keeps edges
















