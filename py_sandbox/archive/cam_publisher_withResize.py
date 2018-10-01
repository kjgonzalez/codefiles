'''
Author: Kris Gonzalez
Date Created: 180323
Objective: generate your own ros node in order to figure out how you can 
	publish usb camera data
Input Arguments: 
arg1 = video source
arg2 = topic name

'''

import rospy
from std_msgs.msg import String # type for text topic
from sensor_msgs.msg import Image # type for video stream topic
import time
import cv2
from cv_bridge import CvBridge, CvBridgeError #convert cv2<>rosimg
from sys import argv
stream=cv2.VideoCapture(int(argv[1]))

def vidpub(cv2_frame):
	try:
		pb=rospy.Publisher(argv[2],Image, queue_size=10)
		#anonymous allows ros to select unique node name
		rospy.init_node('camsrc',anonymous=True)
		if(not rospy.is_shutdown()):
			# FIRST, MUST CONVERT CV2 TO ROS_IMG
			ros_frame = CvBridge().cv2_to_imgmsg(cv2_frame)
			#rospy.loginfo(ros_frame)
			pb.publish(ros_frame)
			#rate.sleep()
			#print 'publishing'
			return True
	except KeyboardInterrupt:
		return False

# attempt to combine ros and cv2 here
ret=stream.isOpened()

# resize to maximum possible video resolution
streamw = 3 # frame width, aka cv2.CAP_PROP_FRAME_WIDTH
streamh = 4 # frame height, aka cv2.CAP_PROP_FRAME_HEIGHT
stream.set(streamw,10000) # set to high number, and let program auto-select max
stream.set(streamh	,10000) # set to high number, and let program auto-select max
# at this point, Intel RealSense D435 would have max resolution of 1920x1080



print 'streaming'
while(ret):
	try:
		ret,img=stream.read()
		ret=vidpub(img)
	except KeyboardInterrupt: 
		print 'Closing script...'
		ret=False
print '\nVideo stream ended\n'
stream.release()
