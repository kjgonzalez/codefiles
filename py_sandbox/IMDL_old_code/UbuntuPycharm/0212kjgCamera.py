import cv2

import numpy as np

img = cv2.imread('picture.jpg')

px=img[100,100,0]
print px
print img.size
print img.dtype