import numpy as np
import cv2
from sys import argv

# Load an color image in grayscale
img = cv2.imread(argv[1])
# will do some operations here

# etc
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()