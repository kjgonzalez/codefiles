import cv2
import numpy as np
import time


#initialize trackbar positions
ini=[14,66,135,23,255,255]

hL=ini[0]
sL=ini[1]
vL=ini[2]
hU=ini[3]
sU=ini[4]
vU=ini[5]


cv2.namedWindow('contours')


cap = cv2.VideoCapture(0) #select video source

t=time.time() #used to get looptime
while(1):


    #IMAGE PROCESSING #######################################

    # Take each frame
    _, frame = cap.read()
#    frame=cv2.flip(frame,1)
    # # Resize the captured frame
    ratio=0.5 #note, 1 = 1:1 ratio
    frame = cv2.resize(frame,None,fx=ratio, fy=ratio, interpolation = cv2.INTER_AREA)
    frameOrig=frame

    #blur with Gauss
    blurVal=5 #should be a positive odd number
    frame=cv2.GaussianBlur(frame,(blurVal,blurVal),0)

    # save only colors in desired range
    try:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #create HSV version #need fix here...
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

        # find moments, get centroid (as long as there are contours)
        if len(contours) > 0: 

            # first, want to find the largest contour, by area: 
            try:
                loc=contours.index(max(contours,key=cv2.contourArea))
            # print loc
            except ValueError:
                print "ValueError: loc set to 0"
                loc=0

            # ensure never go out of bounds
            if(loc>len(contours)):
                print "OutOfBoundsError: loc set to zero"
                loc=0
            
            cnt=contours[loc]
            
            # get frame properties, get largest object properties
            M=cv2.moments(cnt)
            cx=int(M['m10']/M['m00']) # remember A*xavg=int(fn*dA)
            cy=int(M['m01']/M['m00'])
            imgH=frameOrig.shape[0]
            imgW=frameOrig.shape[1]
            
            # create bounding circle
            (xcirc,ycirc),rcirc=cv2.minEnclosingCircle(cnt)
            center = (int(xcirc),int(ycirc))
            cv2.circle(frameOrig,center,int(rcirc),(255,0,0),1)


            #create 2D error line
            cv2.line(frameOrig,(imgW/2,imgH/2),(cx,cy),(255,0,255),1)




        # END OF IMAGE PROCESSING #############################
    except:
        print "ColorspaceError"


    try:
        cv2.imshow('contours',frameOrig)
    except:
        print "VideoFrameError"

    # # get loop time (KJGNOTE: typ loop time below 45ms on laptop)
    print int((time.time()-t)*1000)
    t=time.time()

    #end program when hit 'Escape' key
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()

