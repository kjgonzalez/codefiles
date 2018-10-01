#!/usr/bin/env python
# ALWAYS INCLUDE THE ABOVE IN ALL PYTHON ROS CODE FILES!!!
'''
Author: Kris Gonzalez
Objective: mini debugging for cycling through mission profiles, to affect
	behavior of path planner node.

copied from path planner:
NOTE: // AMI States (per driving/src/driving.hpp)
#define MANUAL     0
#define ACCEL      1
#define SKIDPAD    2
#define TRACKDRIVE 3
#define BRAKETEST  4
#define INSPECTION 5
type: std_msgs::UInt8 "autonomous_mission" (per driving/src/driving.cpp)


'''

import rospy
import time
from std_msgs.msg import UInt8 # message type for mission statu


# MAIN SETUP ==================================================
rospy.init_node('mission_publisher',anonymous=True)
pub_status = rospy.Publisher('autonomous_mission',UInt8,queue_size=2)
rate = rospy.Rate(0.25) # want to change every 4 seconds

# MAIN LOOP ===================================================
try:
	i = 0
	while(not rospy.is_shutdown()):
		print 'current mission:',i
		sendme = UInt8()
		sendme.data = i
		pub_status.publish(sendme)
		i=i+1
		if(i>5):i=0
		rate.sleep()
except rospy.ROSInterruptException: pass

# eof
