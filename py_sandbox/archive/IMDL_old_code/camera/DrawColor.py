# trying to learn how to plot colors, to understand what the fuck opencv considers colors.

import numpy as np
import cv2

#black image
height=300
width=300
rgb=(200,255,100)

#make the background
img=np.zeros((300,300,3),np.uint8)

#diagonal line, rectangle
#cv2.line(img,(0,0),(511,511),(255,0,0),5)
topLeft=(height/4*0,width/4*0)
botRight=(height,width)

cv2.rectangle(img,topLeft,botRight,rgb,-10)
cv2.circle(img,(150,150),4,(0,0,0),-1)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print "done"



