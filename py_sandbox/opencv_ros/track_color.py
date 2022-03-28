'''
Author: Kris Gonzalez
DateCreated: 150303
Objective: use trackbar window to threshold visible colors on camera feed,
	then draw contours around the largest thresholded object. once this object
	is tracked via color thresholding, can perform some basic operations.
	
Conclusions: 
* highly sensitive to brightness / light intensity
* must be calibrated 
* doesn't actually tell you much about what you've detected

There are more sophisticated ways of tracking an object, will move on.
'''

# INITIAILIZATIONS
#initialize trackbar positions
ini=[13,193,150,22,255,201] # orange balloon
ini=[38,70,88,95,255,201] # green usb mouse adapter
import cv2
import numpy as np
from sys import argv

def nothing(x):
    pass
cap = cv2.VideoCapture(int(argv[1])) #select video source
ht=100;wd=500 # kjg180324: these values used again later. do not delete
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
# set initial positions
cv2.setTrackbarPos('H lower','image',ini[0])
cv2.setTrackbarPos('S lower','image',ini[1])
cv2.setTrackbarPos('V lower','image',ini[2])
cv2.setTrackbarPos('H upper','image',ini[3])
cv2.setTrackbarPos('S upper','image',ini[4])
cv2.setTrackbarPos('V upper','image',ini[5])
#create trackbar, called H, in window image, w/ range (0,255), pass 'nothing'
#create sample color boxes
tL=(10,10)
bR=(wd/2-10,ht-10)
tL2=(wd/2+10,10)
bR2=(wd-10,ht-10)



while(1):

    # trackbar operations ######################################################
    if (True): # this is done to hide all the trackbar code
        cv2.imshow('image',img)
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
        #plot trackbars
        img[:]=0 #set controls bkgd to black
        cv2.rectangle(img,tL,bR,(b_L,g_L,r_L),-1) #plot color rect1
        cv2.rectangle(img,tL2,bR2,(b_U,g_U,r_U),-1)    #plot color rect2
        # update threshold arrays
        lower = np.array([h_L,s_L,v_L])
        upper = np.array([h_U,s_U,v_U])
    # ini=[38,70,88,95,255,201] # green usb mouse adapter
    # operations on the frame ##################################################

    # capture a raw frame
    _, frame = cap.read()
    #ratio=0.6

    # resize a the frame
    #frame = cv2.resize(frame,None,fx=ratio, fy=ratio, interpolation = cv2.INTER_AREA)
    cv2.imshow('frame',frame)	# show original resized frame

    # Convert frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Threshold the HSV image to get only colors in hsv range
    thresholded = cv2.inRange(hsv, lower, upper)
    # this matrix represents the mask that are non-zero values to be analyzed
    # note that the mask is the one with the interest region in white
    # at this point, probably want to
    # Bitwise-AND mask and original image
    # technically, thresholded image would be enough because find contours
    # treats the image as a binary (black/else).
    frame = cv2.bitwise_and(frame,frame, mask= thresholded)
    # at this point, have black/white image with desired object in white

    # split channels to obtain single-channel, binary image for findContours
    frame_singleChannel,b,c=cv2.split(frame)

    # perform erosion / dilation ('opening') to remove some noise
    kern = np.ones((4,4),np.uint8)
    f2_open = cv2.morphologyEx(frame_singleChannel,cv2.MORPH_OPEN,kern)

    #find all available contours in image
    im_idk,contours, hierarchy = cv2.findContours(f2_open,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # KJGNOTE: now that have contours of image, some interesting things
    #	can begin to happen...
    # 1. want to find largest area contour: maxContour=max(contours, key=cv2.contourArea)
    # 2. find bounding rect = x_topleft,y_topleft,wide,height = cv2.boundingRect(cnt)
    # 	2a. centroid: xcent=x_topleft+wide/2, ycent=y_topleft+height/2


    # manipulate contours
    #print 'No. contours:',len(contours)
    F = 685.7
    W = 7.0
    contmax=0
    if(len(contours)>0):
        # if have at least one contour
        cmain=max(contours, key=cv2.contourArea)
        cmain_A=cv2.contourArea(cmain)
        cmain_rect=cv2.boundingRect(cmain) #(x,y,wide,height)
        cmain_xcent=cmain_rect[0]+cmain_rect[2]/2
        cmain_ycent=cmain_rect[1]+cmain_rect[3]/2
        if(cmain_A>1500):
            # if area is believably large to suggest not actually noise
            cv2.circle(frame,(cmain_xcent,cmain_ycent),5,(0,0,255),-1)
            print ('estimated dist:',F*W/float(cmain_rect[3]),'cm')

    cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    # KJGNOTE: YOU CAN ONLY DRAW COLORED CONTOURS ON 3-CHANNEL IMAGES, DUH
    ## args: srcImg, contourData, No., color, lineThick

    cv2.imshow('res',frame)		# show white/black frame



    #
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break


cv2.destroyAllWindows()

