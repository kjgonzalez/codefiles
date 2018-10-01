import cv2
import numpy as np
import time

#create controls window
def nothing(x):
    pass
cv2.namedWindow('controls')
    #lower range
cv2.createTrackbar('H lower','controls',0,179,nothing)
cv2.createTrackbar('S lower','controls',0,255,nothing)
cv2.createTrackbar('V lower','controls',0,255,nothing)
    #upper range
cv2.createTrackbar('H upper','controls',0,179,nothing)
cv2.createTrackbar('S upper','controls',0,255,nothing)
cv2.createTrackbar('V upper','controls',0,255,nothing)

#initialize trackbar positions
cv2.setTrackbarPos('H lower','controls',0)
cv2.setTrackbarPos('S lower','controls',108)
cv2.setTrackbarPos('V lower','controls',147)
cv2.setTrackbarPos('H upper','controls',179)
cv2.setTrackbarPos('S upper','controls',255)
cv2.setTrackbarPos('V upper','controls',255)

#temp while wearing blue/green
ini=[100,52,13,179,255,186]

cv2.setTrackbarPos('H lower','controls',ini[0])
cv2.setTrackbarPos('S lower','controls',ini[1])
cv2.setTrackbarPos('V lower','controls',ini[2])
cv2.setTrackbarPos('H upper','controls',ini[3])
cv2.setTrackbarPos('S upper','controls',ini[4])
cv2.setTrackbarPos('V upper','controls',ini[5])



h=1
w=300
img=np.zeros((h,w,3),np.uint8)

cap = cv2.VideoCapture(0) #select video source

t=time.time()
while(1):

    #show controls window
    cv2.imshow('controls',img)
         #track set - lower
    hL = cv2.getTrackbarPos('H lower','controls')
    sL = cv2.getTrackbarPos('S lower','controls')
    vL = cv2.getTrackbarPos('V lower','controls')
        #track set - upper
    hU = cv2.getTrackbarPos('H upper','controls')
    sU = cv2.getTrackbarPos('S upper','controls')
    vU = cv2.getTrackbarPos('V upper','controls')

    # Take each frame
    _, frame = cap.read()
    frame=cv2.flip(frame,1)
    # # Resize the captured frame
    # ratio=0.25 #note, 1 = 1:1 ratio
    # frame = cv2.resize(frame,None,fx=ratio, fy=ratio, interpolation = cv2.INTER_AREA)
    frameOrig=frame

    #blur with Gauss
    blurVal=5 #should be a positive odd number
    frame=cv2.GaussianBlur(frame,(blurVal,blurVal),0)

    # save only colors in desired range
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #create HSV version
    bb,gg,rr=cv2.split(frame)
    lower=np.array([hL,sL,vL])
    upper=np.array([hU,sU,vU])
    frame=cv2.inRange(hsv,lower,upper) #this is the true result

    #get from HSV to Grayscale
    frameGray=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR) #back to BGR version
    frameGray=cv2.cvtColor(frameGray,cv2.COLOR_BGR2GRAY) #now to Grayscale
    

    #erode then dilate, aka open the image
    morphVal=11 #should be a positive odd number
    kernel = np.ones((morphVal,morphVal),np.uint8)
    frame = cv2.morphologyEx(frame, cv2.MORPH_OPEN, kernel) 
    
    # combine and threshold 
    frame=cv2.bitwise_and(frameGray,frameGray,mask=frame)

    # now make everything not-black into white. 
    ret,frame2=cv2.threshold(frame,0,255,cv2.THRESH_BINARY)
    
    # find contours in the image
    contours, hierarchy = cv2.findContours(frame2,\
        cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    # superimpose contours onto a frame
    frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2BGR)
    cv2.drawContours(frameOrig, contours, -1, (0,255,0), 3) 
    #fn(drawLoc, contourInfo, number, color, thickness)
    cv2.imshow('contours',frameOrig)





    # #get loop time
    # print int((time.time()-t)*1000)
    # t=time.time()

    #end program when hit 'Escape' key
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()



    # COPY-ABLE CODE TO GO FROM HSV TO GRAYSCALE, DO NOT REMOVE
    # #get from HSV to Grayscale
    # lala=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR) #back to BGR version
    # lala=cv2.cvtColor(lala,cv2.COLOR_BGR2GRAY) #now to Grayscale
    # cv2.imshow('to grayscale',lala)