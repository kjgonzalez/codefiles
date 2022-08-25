'''
Author: Kris Gonzalez
Date Created: 180423
Objective: learn how the two thresholds of canny edge
	detection affect the result

KJGNOTE: probably want to do some blurring next time in order to better
	remove other lines

todo: update for py3, modern code (KJG20220616)
'''

import cv2
import numpy as np
from sys import argv

# initializations
def quickshow(img):
	cv2.imshow('QuickShow',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
def nothing(x):
	pass

# load image
pic = cv2.imread('imgs/zoom.jpg')
#quickshow(pic)

## use argv arguments to change parmeters one run at a time
#thresh1 = int(argv[1])
#thresh2 = int(argv[2])

#out = cv2.Canny(pic,thresh1,thresh2)

#quickshow(out)


# setup trackbars (note: no rules for values, all combos are valid)
img = np.zeros((10,300,3),np.uint8)
cv2.namedWindow('trackbar')
cv2.createTrackbar('Thresh1','trackbar',0,1000,nothing)
cv2.createTrackbar('Thresh2','trackbar',0,1000,nothing)
# set initial position
cv2.setTrackbarPos('Thresh1','trackbar',100)
cv2.setTrackbarPos('Thresh2','trackbar',200)


# start of main loop
while True:
	cv2.imshow('trackbar',img)
	t1 = cv2.getTrackbarPos('Thresh1','trackbar')
	t2 = cv2.getTrackbarPos('Thresh2','trackbar')

	output = cv2.Canny(pic,t1,t2)
	cv2.imshow('result',output)

	# end code
	k = cv2.waitKey(1) & 0xFF
	if k == ord('q'):
		break


cv2.destroyAllWindows()
