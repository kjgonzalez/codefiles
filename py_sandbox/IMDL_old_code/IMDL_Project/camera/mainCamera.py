import cv2
import numpy as np
import time

#not sure what this does yet, but used in trackbars
def nothing(x):
    pass

#set controls window parameters
ht=200
wd=512
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

# #initialize trackbar positions

ini=[0,0,0,179,255,255] # orange balloon
cv2.setTrackbarPos('H lower','image',ini[0])
cv2.setTrackbarPos('S lower','image',ini[1])
cv2.setTrackbarPos('V lower','image',ini[2])
cv2.setTrackbarPos('H upper','image',ini[3])
cv2.setTrackbarPos('S upper','image',ini[4])
cv2.setTrackbarPos('V upper','image',ini[5])
# set color window palettes
tL=(10,10)
bR=(wd/2-10,ht-10)
tL2=(wd/2+10,10)
bR2=(wd-10,ht-10)




def angleError(raw_cx,FrameWidth):
    cc=float(raw_cx)
    va=float(75) #degrees
    fw=float(FrameWidth)
    return va/fw*(cc-fw)+va/2


# 0408/0409 testing
# setting: KJG room, lamp inside, robot on ground
ball1=[13,193,150,22,255,201] # orange balloon 
ball2=[17,90,114,25,255,201] #pink balloon
ball3=[41,139,39,75,255,125]#green baloon


# DO NOT DELETE, ONLY COMMENT
# cv2.namedWindow('contours')


cap = cv2.VideoCapture(0) #select video source

t=time.time() #used to get looptime
while(1):

    # controls window
    cv2.imshow('image',img)
        #track set 1 - lower
    hL = cv2.getTrackbarPos('H lower','image')
    sL = cv2.getTrackbarPos('S lower','image')
    vL = cv2.getTrackbarPos('V lower','image')    
    hsvL=np.uint8([[[hL,sL,vL]]])   #trans to BGR
    bgrL=cv2.cvtColor(hsvL,cv2.COLOR_HSV2BGR)
    b_L=int(bgrL[0][0][0])
    g_L=int(bgrL[0][0][1])
    r_L=int(bgrL[0][0][2])
        #track set 1 - upper
    hU = cv2.getTrackbarPos('H upper','image')
    sU = cv2.getTrackbarPos('S upper','image')
    vU = cv2.getTrackbarPos('V upper','image')    
    hsvU=np.uint8([[[hU,sU,vU]]])   #trans to BGR
    bgrU=cv2.cvtColor(hsvU,cv2.COLOR_HSV2BGR)
    b_U=int(bgrU[0][0][0])
    g_U=int(bgrU[0][0][1])
    r_U=int(bgrU[0][0][2])
        #plot everything
    img[:]=0 #set controls bkgd to black
    cv2.rectangle(img,tL,bR,(b_L,g_L,r_L),-1) #plot rect1
    cv2.rectangle(img,tL2,bR2,(b_U,g_U,r_U),-1)    #plot rect2


    #IMAGE PROCESSING #######################################

    # Take each frame
    _, frame = cap.read()
    # # Resize the captured frame
    try:
        ratio=0.5 #note, 1 = 1:1 ratio
        frame = cv2.resize(frame,None,fx=ratio, fy=ratio, interpolation = cv2.INTER_AREA)
    except: 
        print "resize error"
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
            
            # get frame properties
            imgH=frameOrig.shape[0]
            imgW=frameOrig.shape[1]
            
            # hide all drawing items (DO NOT DELETE)
            # draw contours
            cv2.drawContours(frameOrig,contours,-1,(0,255,0),1)
            # create bounding circle
            (xcirc,ycirc),rcirc=cv2.minEnclosingCircle(cnt)
            center = (int(xcirc),int(ycirc))
            cv2.circle(frameOrig,center,int(rcirc),(0,0,255),2)
            print int(angleError(xcirc,imgW))
            #create 2D error line
            cv2.line(frameOrig,(imgW/2,imgH/2),(int(xcirc),int(ycirc)),(0,0,255),2)
    except:
        print "ColorspaceError"

    # END OF IMAGE PROCESSING #############################


        # DO NOT DELETE, ONLY COMMENT
    try:
        cv2.imshow('contours',frameOrig)
    except:
        print "VideoFrameError"

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()


