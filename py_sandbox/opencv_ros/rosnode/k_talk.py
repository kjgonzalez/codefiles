'''
Author: Kris Gonzalez
Date Created: 180323
Objective: generate your own ros node in order to figure out how you can 
	publish webcam data
'''

import rospy
from std_msgs.msg import String # type for text topic
from sensor_msgs.msg import Image # type for video stream topic
import time
import cv2
from cv_bridge import CvBridge, CvBridgeError #convert cv2>>rosimg

stream=cv2.VideoCapture(1)

#def talker():
    #pub = rospy.Publisher('chatter', String, queue_size=10)
    #rospy.init_node('talker', anonymous=True)
    #rate = rospy.Rate(10) # 10hz
    #while not rospy.is_shutdown():
        #hello_str = "hello world %s" % rospy.get_time()
        #rospy.loginfo(hello_str)
        #pub.publish(hello_str)
        #rate.sleep()

#def talk2():
	#pub = rospy.Publisher('chatter', String, queue_size=10)
	#rospy.init_node('talker', anonymous=True)
	#if(not rospy.is_shutdown()):
		#hello_str = "hello world %s" % rospy.get_time()
		#rospy.loginfo(hello_str)
		#pub.publish(hello_str)
def vidpub(cv2_frame):
	try:
		pb=rospy.Publisher('vstream',Image, queue_size=10)
		rospy.init_node('camsrc',anonymous=True)
		#rate = rospy.Rate(10) # 10hz
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
		#time.sleep(1./30)
		ret,img=stream.read()
		#cv2.imshow('.',img)
		#print 'here'
		ret=vidpub(img)
		#try:
			##talk2()
			#vidpub(img)
		#except rospy.ROSInterruptException:
			#if(cv2.waitKey(1) & 0xFF ==ord('q')):
				#ret=False
				#print 'exiting 2'
				#break;break;
			#print 'rospy.ROSInterruptException error caught'
			#pass
	except KeyboardInterrupt: 
		print 'Closing script...'
		ret=False
print '\nVideo stream ended\n'
stream.release()
#cv2.destroyAllWindows()