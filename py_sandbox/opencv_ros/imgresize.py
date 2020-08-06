
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


# Load an color image in grayscale
img = cv2.imread(argv[1])
# will do some operations here

img2=resize2(img)
# end of operations here
#cv2.imshow('original',img)
cv2.imshow('small',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()


