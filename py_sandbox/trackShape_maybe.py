'''
Author: Kris Gonzalez
DateCreated: 180501
Objective: practice object detection / tracking with shapes. try to avoid
	doing anything with color if possible.

source of link: https://www.pyimagesearch.com/2016/02/01/opencv-center-of-contour/

main subtask to look at:
	"Recognize various shapes, such as circles, squares, rectangles,
	triangles, and pentagons using only contour properties."

KJGNOTE: want to see if possible to identify other shapes, or versions
	of other shapes.

KJG Mid-Conclusion:
Ok, shape detection is kind of bogus. not really good on it's own, there needs
	to basically be some sort of filtering beforehand, can't just look at
	shapes as-is, at least while avoiding color. so, seems like will need to
	look for something else...?


'''

# initializations ==========================================
# main image to use will be from tutorial:
filename= 'imgs/shapes.jpg'

import cv2
import numpy as np

def qs(image):
	cv2.imshow('',image)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
# def qs

# main code ================================================

# load image and do some basic filtering. troubling though...
img = cv2.imread(filename)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
img2 = cv2.threshold(blur,60,255,cv2.THRESH_BINARY)[1] # just take image

# find contours
contours = cv2.findContours(img2.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
contours = contours[1] #apparently needed for the right tuple?
# import ipdb; ipdb.set_trace()
contours = contours[1:] # skip first one, apparently some sort of error
i = 0
for c in contours:
	# compute the center of the contour
	M = cv2.moments(c)
	cX = int(M["m10"] / M["m00"])
	cY = int(M["m01"] / M["m00"])

	# draw the contour and center of the shape on the image
	cv2.drawContours(img, [c], -1, (0, 255, 0), 2)
	cv2.circle(img, (cX, cY), 7, (255, 255, 255), -1)
	cv2.putText(img, str(i), (cX - 20, cY - 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
	i=i+1
# show the image (modification: show only final result)
# import ipdb; ipdb.set_trace()
# cv2.imwrite('imgs/shapes2.jpg',img)
# cv2.imshow("Image", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
