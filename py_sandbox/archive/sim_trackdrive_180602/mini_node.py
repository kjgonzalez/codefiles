'''
Objective: create a rosbag with a dummy track and course. this node to be used
	in conjunction with gazebo & turtlebot & its teleop
'''


import rospy
import numpy as np
from mapping.msg import Cone
from mapping.msg import ConeArray
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from nav_msgs.msg import Odometry

# original
fname_blue='track_blue_cones.csv'
fname_yell='track_yellow_cones.csv'
fname_oran='track_orange_cones.csv'

#
fname_blue='../sim_acceleration_10721/accel_1_blue.csv'
fname_yell='../sim_acceleration_10721/accel_1_yellow.csv'
fname_oran='../sim_acceleration_10721/accel_1_orange.csv'

#  load track from memory:
blue=[]
f=file(fname_blue)
for irow in f:
	temp=irow.split(',')
	x=float(temp[0])
	y=float(temp[1])
	blue.append([x,y])
f.close()

yellow=[]
f=file(fname_yell)
for irow in f:
	temp=irow.split(',')
	x=float(temp[0])
	y=float(temp[1])
	yellow.append([x,y])
f.close()

orange=[]
f=file(fname_oran)
for irow in f:
	temp=irow.split(',')
	x=float(temp[0])
	y=float(temp[1])
	orange.append([x,y])
f.close()

# splitting up tasks into new forloops, just in case
# 0: BLUE 1: YELLOW 2: ORANGE
color=0
conesmsg=ConeArray()
markersmsg=MarkerArray()
counter=0
for irow in blue:
	icone=Cone()
	icone.posx=irow[0]
	icone.posy=irow[1]
	icone.color=0
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
	imarker.color.b=1.0
	imarker.lifetime.secs=10
	markersmsg.markers.append(imarker)
	counter=counter+1
# at this point, have all blue markers /cones ready to publish

for irow in yellow:
	icone=Cone()
	icone.posx=irow[0]
	icone.posy=irow[1]
	icone.color=1
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
	imarker.color.r=1.0
	imarker.color.g=1.0
	imarker.lifetime.secs=10
	markersmsg.markers.append(imarker)
	counter=counter+1
# now have all yellow markers / cones ready to publish

for irow in orange:
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
	imarker.lifetime.secs=10
	markersmsg.markers.append(imarker)
	counter=counter+1

def callback_odo(data):
	# essentially, just bounce the odo data off with a new frame_id
	data.header.frame_id='map'
	pub_odo.publish(data)

try:
	print 'Starting node...'
	rospy.init_node('sampleTrack',anonymous=True)
	pub_cone=rospy.Publisher('dummy_global_cone',ConeArray,queue_size=5)
	pub_marker=rospy.Publisher('dummy_cone_markers',MarkerArray,queue_size=5)
	pub_odo=rospy.Publisher('dummy_map_odo',Odometry,queue_size=5)
	rospy.Subscriber('odom',Odometry,callback_odo,queue_size=5)
	rate=rospy.Rate(1)
	print 'Publishing track...'
	while not rospy.is_shutdown():
		pub_cone.publish(conesmsg)
		pub_marker.publish(markersmsg)
		rate.sleep()

except rospy.ROSInterruptException:
	print 'Closing node...'
	pass









#eof
