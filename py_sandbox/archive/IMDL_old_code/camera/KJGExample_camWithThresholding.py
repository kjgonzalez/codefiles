import cv2
import numpy as np


#create controls window
def nothing(x):
    pass
cv2.namedWindow('image')
    # trackbars: minVal / maxVal
cv2.createTrackbar('minVal','image',0,255,nothing)
cv2.createTrackbar('maxVal','image',0,255,nothing)
    #trackbars: adaptive thresholding values
cv2.createTrackbar('first','image',0,255,nothing)
cv2.createTrackbar('second','image',0,255,nothing)
cv2.createTrackbar('third','image',0,255,nothing)

#initialize trackbar positions
cv2.setTrackbarPos('minVal','image',100)
cv2.setTrackbarPos('maxVal','image',200)

cv2.setTrackbarPos('first','image',255)
cv2.setTrackbarPos('second','image',11)
cv2.setTrackbarPos('third','image',2)


h=1
w=300
img=np.zeros((h,w,3),np.uint8)



cap = cv2.VideoCapture(1) #select video source



while(1):

    #show controls window
    cv2.imshow('image',img)
    minVal=cv2.getTrackbarPos('minVal','image')
    maxVal=cv2.getTrackbarPos('maxVal','image')

    first=cv2.getTrackbarPos('first','image')
    second=cv2.getTrackbarPos('second','image')
    third=cv2.getTrackbarPos('third','image')






    # Take each frame
    _, frame = cap.read()
    
    #resize the captured frame
    ratio=0.4 #note, 1 = 1:1 ratio
    frame = cv2.resize(frame,None,fx=ratio, fy=ratio, interpolation = cv2.INTER_AREA)
    # cv2.imshow('original',frame)
    frame2=frame    

    #blur img with Gauss
    frame=cv2.GaussianBlur(frame,(7,7),0)
    # cv2.imshow('blur',frame)
    
    #convert to grayscale, which allows easier thresholding
    frame=cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    # cv2.imshow('original',frame)

    #Simple threshold blurred image. not sure what "ret," does

    #Adaptive threshold image
    frame=cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
        cv2.THRESH_BINARY,11,2)
    cv2.imshow('Adaptive Thresh',frame)


    #erode, then dilate the image to help get rid of noise
    kernel=np.ones((3,3),np.uint8)
    frame=cv2.morphologyEx(frame, cv2.MORPH_CLOSE, kernel)
    # cv2.imshow('morphing',frame)
    #show results
    # cv2.imshow('frame',frame) #currently choosing to hide original
    # cv2.imshow('resized',res)

    
    frame=cv2.Canny(frame2,minVal,maxVal)
    cv2.imshow('canny',frame)

    #end 
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()