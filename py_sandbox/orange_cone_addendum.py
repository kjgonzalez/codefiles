#!/usr/bin/env python
# ALWAYS INCLUDE THE ABOVE IN ALL PYTHON ROS CODE FILES!!!
'''
Author: Kris Gonzalez
Objective: add orange cones to simulation in order to pretend they're in track
topic is: /dummy_cone_markers
lowest ID number should be 300
xy locs:
LHS:[91,45]
RHS:[93,39.5]
'''

import rospy
import time
import numpy as np
from std_msgs.msg import UInt8 # message type for mission statu
from mapping.msg import Cone
from mapping.msg import ConeArray
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray

orangecones = [[91.,45.],[93.,39.5]]

conesmsg=ConeArray()
markersmsg=MarkerArray()
counter=300
# 0: BLUE 1: YELLOW 2: ORANGE
for irow in orangecones:
	icone=Cone()
	icone.posx=irow[0]
	icone.posy=irow[1]
	icone.color=2
	conesmsg.cones.append(icone)
	imarker=Marker()
	imarker.pose.position.x=irow[0]
	imarker.pose.position.y=irow[1]
	imarker.header.frame_id='map'
	imarker.id=counter
	imarker.scale.x=.5
	imarker.scale.y=.5
	imarker.scale.z=.5
	imarker.type=3
	imarker.color.a=1.0
	imarker.color.r=0.82
	imarker.color.g=0.45
	imarker.color.b=0.13

	markersmsg.markers.append(imarker)
	counter=counter+1
# at this point, have all blue markers /cones ready to publish

# MAIN SETUP ==================================================
rospy.init_node('orange_publisher',anonymous=True)
pub_cone = rospy.Publisher('dummy_global_cone',ConeArray,queue_size=10)
pub_marker = rospy.Publisher('dummy_cone_markers',MarkerArray,queue_size=10)
rate = rospy.Rate(20)

# MAIN LOOP ===================================================
try:
	# i = 0
	while(not rospy.is_shutdown()):
		print 'publishing orange cones',time.time()
		pub_cone.publish(conesmsg)
		pub_marker.publish(markersmsg)
		rate.sleep()

except rospy.ROSInterruptException: pass
# eof
