'''
Author: Kristian Gonzalez
DateCreated: 180321
Version2Created: 181029

Objective: Want to understand and possibly improve python opencv, to be used
	for batch editing photos, especially those for the database building.

KJGNOTE: Will leave custom functions in-place instead of organizing at top, in
	order to give context in code.

Some sample operations that need to be understood and shown:

* load an image
* flip / rotate an image
* convert image to grayscale
* resize an image (ratio or specific size)
* crop an image
* draw on image (text and rectangle)
* display an image
'''

# Initializations ##########################################
# import klib
# if(klib.PYVERSION!=3):
#     raise Exception('must use python3. exiting.')
import cv2
import numpy as np
import os
import klib

def qs(img,title='CLOSE WITH KEYBOARD'):
    cv2.imshow(title,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
def rect2(img, center,dims,angle, color,*kargs):
    ''' general steps:
    1. take in parameters
    2. rotate rectangle centered at origin
    3. translate to given spot.

     '''
    xc,yc=center
    w,h=dims
    theta = np.radians(angle)
    c,s=np.cos(theta),np.sin(theta)
    R=np.array([
        [c,-s,0],
        [s,c,0],
        [0,0,1]]) # 3x3
    pts=np.array([
        [-w,h,1],
        [w,h,1],
        [w,-h,1],
        [-w,-h,1],
        [-w,h,1]   ])/2

    # rotate points
    pts2=pts@R
    pts2[:,0]+=xc
    pts2[:,1]+=yc
    pts2=pts2[:,:2].reshape((-1,1,2)).astype(int)
    cv2.polylines(img,[pts2],True,RED)

## delete last script's output file(s)
#for ifile in os.listdir('.'):
    #if('delme' in ifile):
        #os.remove(ifile)

# load image ###########################
filename=klib.data.jpgpath
img = cv2.imread(filename)
print('path:',filename)
print('h,w,ch:',img.shape)# print as (row,column,channels) format

# flip / rotate an image
img2=cv2.flip(img,0) # 0 is up-down flip, 1 is left-right flip
img2=cv2.rotate(img2,cv2.ROTATE_90_CLOCKWISE)

# resize an image
res_ratio = cv2.resize(img,(0,0),fx=0.5,fy=0.5) # resize image by ratio
res_value = cv2.resize(img,(400,400),(0,0)) # resize image by value

# crop an image. cropping is just an equation, and origin is top-left
# note that matrix values work in RRCC coordinate system
crop1 = img[70:200,30:200] # using rc format, [x1:x2,y1:y2]

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
	  centerXY: 2-value int tuple, (width,height) coordinates. e.g.: (10,15). default = center
	  wide: desired width of crop rectangle. default=500px
	  height: desired height of crop rectangle. default=500px
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
crop2 = cropCentered(img,wide=505,height=505)

# save an image back to disk
qs(res_ratio)
# cv2.imwrite('out.jpg',res_ratio)

# LEARNING ABOUT BLURS #####################################
# blur helps remove noise
# it also helps provide artificial variety when training
# 	an algorithm
#

# have already imported cv2, np, and os


# different blur items to consider:
# 		blur, boxFilter, bilateralFilter, GaussianBlur, medianBlur
#cv2.blur(src,ksize)
#cv2.boxFilter(src,ddepth,(ksize,ksize)) #hard to visually tell diff from 'blur'
#cv2.medianBlur(src,ksize) #makes things look more like an oil pastel or so
#cv2.bilateralFilter(src,d,sigmaColor) # more for offline work, keeps edges
