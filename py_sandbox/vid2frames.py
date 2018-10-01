'''
Author: Kris Gonzalez
DateCreated: 180321
Objective: Practice getting frames from a video
General Steps
	1. load video
	2. iterate through all frames, getting a subset of the frames (rounding)
	3. resize each frame
	4. export / save each frame to a subfolder (already created)
	5. complete.
Input Arguments:
	* arg1 = video file
	* arg2 = desired number of frames ('all' for all frames)
	* arg3 = path to place images
'''

# initializations
import numpy as np
import cv2
import os
from sys import argv

# catch argument errors
if(not os.path.exists(argv[1])):
	print 'ERROR: video not found'
	exit()
elif(not argv[2].isdigit() and argv[2] != 'all'):
	print 'ERROR: desiredFrames is not a number or ''all'' '
	exit()
elif(not os.path.exists(argv[3])):
	print 'ERROR: output path not found'
	exit()

# load video

# otherwise, convert arguments to code
videoToLoad = argv[1]
desiredExportLoc = argv[3]

# iterate and put all frames in a single array via rounding (no interpolation)
vid=cv2.VideoCapture(videoToLoad)
nFrames = vid.get(cv2.CAP_PROP_FRAME_COUNT)
if(argv[2].isdigit()):
	desiredFrames = int(argv[2])
else:
	desiredFrames = int(nFrames)
frames=[]
success = True

# will eventually try to catch desired frames in while loop instead of forloop
while success:
	success,iframe = vid.read()
	frames.append(iframe)
print 'counted frames:',len(frames)
print 'cv2 frames:',vid.get(cv2.CAP_PROP_FRAME_COUNT)
nFrames = len(frames)

# select only frames that match criteria, resize, and export
for i in range(0,desiredFrames):
	j=int(round(float(i)/float(desiredFrames+1)*nFrames))
	res=cv2.resize(frames[j],(0,0),fx=1,fy=1)
	fpath = desiredExportLoc+str(i)+'.jpg'
	cv2.imwrite(fpath,res)
	print fpath,'\t frame',j


print 'exiting...'