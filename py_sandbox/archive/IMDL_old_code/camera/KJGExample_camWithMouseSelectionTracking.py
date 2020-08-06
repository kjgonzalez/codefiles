import cv2
import numpy as np
import time


#initialize trackbar positions
ini=[0,108,110,179,255,255]
hL=ini[0]
sL=ini[1]
vL=ini[2]
hU=ini[3]
sU=ini[4]
vU=ini[5]


# setup mouse color selection: 
drawing = False # true if mouse is pressed
ix,iy = -1,-1
counter=0
createWin=False
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,moving,createWin
    circleRadius=10
    
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        moving = True
        ix,iy=x,y


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        moving = False
        createWin=True

cv2.namedWindow('contours')
cv2.setMouseCallback('contours',draw_circle)

box=41 # Mouse Selection Box
ROIb=0 #initialize ROI colors
ROIg=0
ROIr=0
# end of mouse color selection setup


cap = cv2.VideoCapture(0) #select video source

t=time.time() #used to get looptime
while(1):


    #IMAGE PROCESSING #######################################

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
    try:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #create HSV version #need fix here...
    except:
        print "ColorspaceConversionError"
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
    cv2.drawContours(frameOrig, contours, -1, (0,255,0), 1) 
    #fn(drawLoc, contourInfo, number, color, thickness)
    
    # find moments, get centroid (as long as there are contours)
    if len(contours) > 0: 

        #first, want to find the largest contour, by area: 
        try:
            loc=contours.index(max(contours,key=cv2.contourArea))
        # print loc
        except ValueError:
            print "ValueError, handled: loc set to 0"
            loc=0

        #ensure never go out of bounds
        if(loc>len(contours)):
            print "OutOfBoundsError: loc>contour, reset to zero"
            loc=0
        
        cnt=contours[loc]
        
        #get frame properties, get largest object properties
        M=cv2.moments(cnt)
        cx=int(M['m10']/M['m00']) # remember A*xavg=int(fn*dA)
        cy=int(M['m01']/M['m00'])
        imgH=frameOrig.shape[0]
        imgW=frameOrig.shape[1]
        
        # create circle, put it into frame (optional)
        
        cv2.circle(frameOrig,(cx,cy), 7, (0,0,255), -1)

        # create a bounding rectangle (optional)
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frameOrig,(x,y),(x+w,y+h),(0,255,0),1)

        #create crosshairs (optional)
        cv2.line(frameOrig,(imgW/2,0),(imgW/2,imgH),(0,0,0),1)
        cv2.line(frameOrig,(0,imgH/2),(imgW,imgH/2),(0,0,0),1)
        #(image to place, startCoord, endCoord, color, thick)

        #create error "line"
        cv2.line(frameOrig,(imgW/2,imgH/2),(cx,cy),(255,0,255),1)


    # END OF IMAGE PROCESSING #############################


    # if mouse is being used, show the selection box
    if(drawing==True and moving==True):
        # print "drawing"
        # cv2.circle(img,(ix,iy),10,(0,0,255),2)
        cv2.rectangle(frameOrig,(ix-(box-1)/2,iy-(box-1)/2),\
            (ix+(box-1)/2,iy+(box-1)/2),(0,0,255),1)
    # when done clicking, show averaged color
    cv2.rectangle(frameOrig,(1,1),(50,50),(ROIb,ROIg,ROIr),-1)


    #when mouse is unclicked (lifted), create ROI image
    if(createWin==True):    
        xMin=ix-(box-1)/2
        xMax=ix+(box-1)/2
        yMin=iy-(box-1)/2
        yMax=iy+(box-1)/2
        roi=frameOrig[yMin:yMax,xMin:xMax]
        # roi=cv2.GaussianBlur(roi,(5,5),0)
        roi=cv2.blur(roi,(15,15))
        ROIb,ROIg,ROIr,_ = cv2.mean(roi)
        # print ROIb,ROIg,ROIr
        # cv2.imshow('roi',roi)
        createWin=False
        
        # get bgr and convert it to hsv values
        ROIbgr = np.uint8([[[ROIb,ROIg,ROIr]]])
        ROIhsv = cv2.cvtColor(ROIbgr,cv2.COLOR_BGR2HSV)
        ROIh=int(ROIhsv[0][0][0])
        ROIs=int(ROIhsv[0][0][1])
        ROIv=int(ROIhsv[0][0][2])

        # take hsv values, make lower/upper ranges
        hff=20 # h offset
        sff=80 #s offset
        vff=40 #v offset
        hL=max(ROIh-hff,0) #min/abs to prevent out of range error
        sL=max(ROIs-sff,0)
        vL=max(ROIv-vff,0)
        hU=min(ROIh+hff,179)
        sU=min(ROIs+sff,255)
        vU=min(ROIv+vff,255)

        # need to deal with red color somehow: 
        if(hL < 10 or hU > 245): 
            hL=0
            hU=255


        # ini=[0,108,110,179,255,255]

    try:
        cv2.imshow('contours',frameOrig)
    except:
        print "VideoFrameError"

    # #get loop time (KJGNOTE: typ loop time below 80ms on laptop)
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