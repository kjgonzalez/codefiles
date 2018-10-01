#!/usr/bin/env python
'''
Author: Kris Gonzalez
DateCreated: 180324
Objective: Will create first subscriber node that takes in video from a 
	ros topic. primary purpose is only to receive and display camera data.

'''

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import time
import cv2
from cv_bridge import CvBridge,CvBridgeError # convert cv2<>rosimg
from sys import argv

'''
EXPECTED ARGUMENTS:
arg1 = topic to listen for
'''

#cap = cv2.VideoCapture(int(argv[1])) # need to give source, have multiple cams
#newdata=False

def newFrame(ros_frame):
	#global cv2_frame
	#global newdata
	#newdata=True
	# perhaps the message is the img that is received
	#print 'i got data'
	cv2_frame = CvBridge().imgmsg_to_cv2(ros_frame)
	cv2.imshow('',cv2_frame);cv2.waitKey(0)

def listen2():
	try:
		rospy.init_node('cam_sub',anonymous=True)  # init node with name
		rospy.Subscriber(argv[1], Image, newFrame) #subscribe node to topic
		return True
	except KeyboardInterrupt:
		print 'exiting...'
		return False
		exit()
try:
	userContinue=True
	while( not rospy.is_shutdown() and userContinue):
		userContinue=listen2()
		#if(newdata):
			#newdata=False
			#cv2.imshow('',cv2_frame)
			#if cv2.waitKey(1) & 0xFF == ord('q'):
				#cv2.destroyAllWindows()
		#print 'waiting...'

except KeyboardInterrupt:
	print 'ending'
	cv2.destroyAllWindows()
	#exit()