'''
objective: quick test to see how to display a line with the marker type
'''

import rospy
import time
import numpy as np
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import Point


rospy.init_node('thing',anonymous=True)
pub = rospy.Publisher('markers',MarkerArray,queue_size=10)

p_arr=[]
for i in np.linspace(0,6,10):
	p = Point()
	p.x=i
	p.y=np.sin(i)
	p_arr.append(p)
counter=0
test = Marker()
test.header.frame_id = 'map'
test.id=0
test.scale.x=0.5
test.lifetime.secs=1
test.color.r=1.0
test.color.b=1.0
test.color.a=1.0
test.type=4
test.points=p_arr

# ###################################
start = Marker()
start.header.frame_id = 'map'
start.id=1
start.pose.position.x = 0
start.pose.position.x = 0
start.scale.x=0.5
start.scale.y=0.5
start.scale.z=0.5
start.lifetime.secs=1
start.color.g=1.0
start.color.a=1.0
start.type=3

# ###############################
together = MarkerArray()
together.markers.append(test)
together.markers.append(start)


while (not rospy.is_shutdown()):
	# pub.publish(allmarkers)
	pub.publish(together)
	time.sleep(1)
# while


# eof
