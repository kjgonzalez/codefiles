'''
Author: Kris Gonzalez
Objective: to tune turtlebot, emulate path planning, but only send 'move forward'
command, and giving only a straight forward path.
'''



import rospy
import numpy as np
import time
import tf
import math

from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from mapping.msg import Cone
from mapping.msg import ConeArray
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist # for directly outputing move command, turtlebot
from path_planning.msg import drive_instructions
from std_msgs.msg import UInt8
from std_msgs.msg import String

def markers_to_publish(xy_points,color=0,startid=0,markersize=0.5):
	'''
	given a set of points, setup marker array to publish them in a given color
	xy_points = 2D<Nx2> array (numpy preferred) of points
	color = (0:red,1:green,2:blue), color of cones. default is (0:red)
	'''
	allmarkers = MarkerArray()
	counter=0
	for irow in xy_points:
		imarker = Marker()
		imarker.pose.position.x=irow[0]
		imarker.pose.position.y=irow[1]
		imarker.header.frame_id='map'
		imarker.id=counter+startid
		imarker.scale.x=markersize
		imarker.scale.y= markersize
		imarker.scale.z=.25
		imarker.type=3 #0=arrow,1=cube,2=sphere,3=cylinder
		imarker.color.a=1.0
		if(color==0):
			imarker.color.r=1.0
		elif(color==1):
			imarker.color.g=1.0
		elif(color==2):
			imarker.color.b=1.0
		imarker.lifetime.secs=1
		allmarkers.markers.append(imarker)
		counter=counter+1
	return allmarkers
# def markers_to_publish

def GenAngleViz(desangle,car,nPoints=10):
	# return linear set of points to visualize for car desired angle
	dist=5.0
	x2 = car[0]+dist*np.cos(car[2]+desangle)
	y2 = car[1]+dist*np.sin(car[2]+desangle)
	point = np.array([x2,y2])
	xpts = np.linspace(car[0],point[0],nPoints)
	ypts = np.linspace(car[1],point[1],nPoints)
	return np.column_stack((xpts,ypts))
# def genAngleViz

# ROS STUFF
rospy.init_node('path_planner',anonymous = True)

# ROS PUBLISHERS
pub_command = rospy.Publisher('command_path',drive_instructions,queue_size=10)

# start publishing desired straight line

while(not rospy.is_shutdown()):
	# consistently publish the same message (desired angle / speed)
	comm = drive_instructions()
	comm.target_speed = 1.0 # could be slower, but will not change for now
	comm.steering_angle = float(0) # turtlebot should go "straight" (based on odom)

	# data viz
	pub_command.publish(comm)
	time.sleep(0.09) # loop time
