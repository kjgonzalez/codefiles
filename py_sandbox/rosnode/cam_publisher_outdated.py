'''
Author: Kris Gonzalez
Date Created: 180323
Objective: generate your own ros node in order to figure out how you can
	publish usb camera data
'''

import rospy
from std_msgs.msg import String # type for text topic
from sensor_msgs.msg import Image # type for video stream topic
import time
import cv2
from cv_bridge import CvBridge, CvBridgeError #convert cv2>>rosimg
from sys import argv

if(len(argv)>1):
	vidsrc = int(argv[1])
else:
	vidsrc = 0
stream=cv2.VideoCapture(vidsrc)

def vidpub(cv2_frame):
	try:
		pb=rospy.Publisher('vstream',Image, queue_size=10)
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
