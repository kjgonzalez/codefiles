#!/bin/python

# attempt to contours with shape recognition

import cv2
import numpy as np
from time import sleep
from time import time

cap = cv2.VideoCapture(0) #select video source

while(1):
	_, frame = cap.read()
	cv2.imshow('contours',frame) #video frame



	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
