import numpy as np
import cv2
from sys import argv

def resize2(imgname,Screen2ImageRatio=2):
	''' Objective: provide SUPER simple way to resize an image relative to size
		of the active / main screen. The ratio is only an upper bound; the image
		is not resized if it is smaller than a ratio of the screen dimensions. 
		However, if it is larger, the image is resized.
	'''
	import Tkinter
	root = Tkinter.Tk()
	sc_dim = (root.winfo_screenheight(),root.winfo_screenwidth())
	
	im_dim = img.shape[:2]
	if(im_dim[0]*Screen2ImageRatio>sc_dim[0]):
		# shrink by height ratio
		f = float(sc_dim[0])/(Screen2ImageRatio*float(im_dim[0]))
		return cv2.resize(img,(0,0),fx=f,fy=f,)
	elif(im_dim[1]*Screen2ImageRatio>sc_dim[1]):
		# shrink by width ratio
		f = float(sc_dim[1])/(Screen2ImageRatio*float(im_dim[1]))
		return cv2.resize(img,(0,0),fx=f,fy=f)
	else:
		return img

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




# Load a color image
img = cv2.imread(argv[1])
# will do some operations here

img2=resize2(img)
# end of operations here
#cv2.imshow('original',img)
cv2.imshow('small',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

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


    # Take each frame
    #_, frame = cap.read()
    #ratio=0.75
    #frame = cv2.resize(frame,None,fx=ratio, fy=ratio,interpolation = cv2.INTER_AREA)


    ## Convert BGR to HSV
    #hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    ## define range of blue color in HSV
    ## KJGNOTE: this actually seems to be blue range in RGB
    ## lower_blue = np.array([130,255,255])

    #lower = np.array([h_L,s_L,v_L])
    #upper = np.array([h_U,s_U,v_U])

    ## Threshold the HSV image to get only blue colors
    #mask = cv2.inRange(hsv, lower, upper)
    ##note that the mask is the one with the interest region in white
    
    ## Bitwise-AND mask and original image
    #res = cv2.bitwise_and(frame,frame, mask= mask)
    
    ##cv2.imshow('frame',frame)
    ##cv2.imshow('mask',mask)
    #cv2.imshow('res',res)



        #
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
