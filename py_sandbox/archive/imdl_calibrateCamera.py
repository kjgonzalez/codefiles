'''
Author: Kris Gonzalez
DateCreated: 150303
Objective: use trackbar window to threshold visible colors on camera feed
'''

import cv2
import numpy as np
def nothing(x):
    pass

cap = cv2.VideoCapture(3) #select video source

ht=100
wd=500
img=np.zeros((ht,wd,3), np.uint8)
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
ini=[13,193,150,22,255,201] # orange balloon
cv2.setTrackbarPos('H lower','image',ini[0])
cv2.setTrackbarPos('S lower','image',ini[1])
cv2.setTrackbarPos('V lower','image',ini[2])
cv2.setTrackbarPos('H upper','image',ini[3])
cv2.setTrackbarPos('S upper','image',ini[4])
cv2.setTrackbarPos('V upper','image',ini[5])


#create trackbar, called H, in window image, w/ range (0,255), pass nothing
    #create sample color boxes
tL=(10,10)
bR=(wd/2-10,ht-10)

tL2=(wd/2+10,10)
bR2=(wd-10,ht-10)



while(1):

    #controls setup / plotting
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
        #plot everything
    img[:]=0 #set controls bkgd to black
    cv2.rectangle(img,tL,bR,(b_L,g_L,r_L),-1) #plot color rect1
    cv2.rectangle(img,tL2,bR2,(b_U,g_U,r_U),-1)    #plot color rect2

	# operations on the frame
    # capture a raw frame
    _, frame = cap.read()
    ratio=0.75
    # resize a the frame
    frame = cv2.resize(frame,None,fx=ratio, fy=ratio, interpolation = cv2.INTER_AREA)
    
    # Convert frame from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([h_L,s_L,v_L])
    upper = np.array([h_U,s_U,v_U])

    # Threshold the HSV image to get only colors in hsv range
    mask = cv2.inRange(hsv, lower, upper)
    #note that the mask is the one with the interest region in white
    
    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    #cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)



        #
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

