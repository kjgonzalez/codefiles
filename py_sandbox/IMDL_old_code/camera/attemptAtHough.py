import cv2
import numpy as np

img = cv2.imread('test.png',0)
img = cv2.medianBlur(img,11)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.cv.CV_HOUGH_GRADIENT,\
	1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
#fn(grayscaleIMG,method,1/accumulator,minUniqueDist,coeff1,coeff2)
# dp - doesn't seem to be useful
# param1 - doesn't affect very much with still image
# param2 - increase means less circles
# min/maxRadius - not worth trouble
# KJGNOTE: ideally, want about 10 circles identified



# find largest radius of array, save that vector's values
maxR=0
maxX=0
maxY=0
minR=100
for i in range(0,len(circles[0])):
	# find largest circle
	if(maxR<circles[0][i][2]):
		maxX=circles[0][i][0]
		maxY=circles[0][i][1]
		maxR=circles[0][i][2]
	# find smallest circle, for debugging
	if(minR>circles[0][i][2]):
		minR=circles[0][i][2]

print minR
print len(circles[0])

# plot all circles (remove eventually)
circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),1)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),2)

# specially plot the largest circle
cv2.circle(cimg,(maxX,maxY),maxR,(0,0,255),3)


cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
