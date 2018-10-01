'''
Author: Kris Gonzalez
DateCreated: 180614
Objective: quick node that simply transforms odometry frame of turtlebot from
'odom' to 'map', in order to use live simulation with other items.

command to run this node (currently):
>> python turtlebot_odom_frame_switch.py

'''

import rospy
from nav_msgs.msg import Odometry
import time

def call_odom(data):
	new_odom=data
	new_odom.header.frame_id='map'
	pub_odom.publish(new_odom)

# main start =======
rospy.init_node('turtlebot_odom_correcter',anonymous = True)
rospy.Subscriber('odom',Odometry,call_odom,queue_size=2)
pub_odom = rospy.Publisher('odom_map',Odometry,queue_size=2)
rate = rospy.Rate(1) #Hz
try:
	while(not rospy.is_shutdown()):
		print 'turtlebot_odom_correcter: publishing',time.time()
		rate.sleep()
except rospy.ROSInterruptException:
	pass # end gracefully
