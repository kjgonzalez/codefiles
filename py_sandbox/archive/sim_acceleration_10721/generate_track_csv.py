'''
Script to generate csv files of cone locations for a track. Use this in
conjunction with a png image. color definitions are below.

RGB / HSV values:
blue [0,38,255]		/ [115,255,255]
yellow [255,216,0]	/ [25,255,255]
orange [255,106,0]	/ [13,255,255]

General Steps:
import file to variable
do a filter for each color and get 3 different masks
find non zero values and generate csv from array of points

KJGNOTE, skeleton commands:
a=cv2.imread('cones_blue_outer.png')
b=cv2.cvtColor(a,cv2.COLOR_RGB2GRAY)
c=cv2.findNonZero(b)
'''

import cv2
import numpy as np
from sys import argv
# first, load original file
print 'converting file',argv[1]
base_img = cv2.imread(argv[1])
base_hsv = cv2.cvtColor(base_img,cv2.COLOR_BGR2HSV)
# next, filter for each color in HSV (can it be done in RGB?) and get an
# img output for each

# create points for blue cones
blueL = np.array([105,245,245])
blueU = np.array([125,255,255])
mask = cv2.inRange(base_hsv,blueL,blueU)
blue_only = cv2.bitwise_and(base_hsv,base_hsv, mask = mask)
blue_only = cv2.cvtColor(blue_only,cv2.COLOR_HSV2RGB)
blue_only = cv2.cvtColor(blue_only,cv2.COLOR_RGB2GRAY)
blue = cv2.findNonZero(blue_only)
print 'No. blue detected:',len(blue)

# create points for yellow cones
yellowL = np.array([15,245,245])
yellowU = np.array([35,255,255])
mask = cv2.inRange(base_hsv,yellowL,yellowU)
yellow_only = cv2.bitwise_and(base_hsv,base_hsv, mask = mask)
yellow_only = cv2.cvtColor(yellow_only,cv2.COLOR_HSV2RGB)
yellow_only = cv2.cvtColor(yellow_only,cv2.COLOR_RGB2GRAY)
yellow = cv2.findNonZero(yellow_only)
print 'No. yellow detected:', len(yellow)

# create points for orange cones
orangeL = np.array([03,245,245])
orangeU = np.array([23,255,255])
mask = cv2.inRange(base_hsv,orangeL,orangeU)
orange_only = cv2.bitwise_and(base_hsv,base_hsv, mask = mask)
orange_only = cv2.cvtColor(orange_only,cv2.COLOR_HSV2RGB)
orange_only = cv2.cvtColor(orange_only,cv2.COLOR_RGB2GRAY)
orange = cv2.findNonZero(orange_only)
print 'No. orange detected:', len(orange)

# at this point, have all cone locations in memory. write to single file.
basename = 'attempt'

f = file(basename+'.csv','w')
# note: key difference in each forloop is str(n)
for icone in blue:
	f.write(str(icone[0][0])+','+str(icone[0][1])+','+str(0)+'\n')

for icone in yellow:
	f.write(str(icone[0][0])+','+str(icone[0][1])+','+str(1)+'\n')

for icone in orange:
	f.write(str(icone[0][0])+','+str(icone[0][1])+','+str(2)+'\n')
f.close()

print 'done!'
