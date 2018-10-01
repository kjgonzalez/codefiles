''' check why pid.py not receiving'''


import rospy
import time
from std_msgs.msg import UInt8


def callback(data):
	print 'received data',data
# def callback
	
rospy.init_node('thing',anonymous=True)
rospy.Subscriber('autonomous_mission',UInt8,callback,queue_size=10)

while(not rospy.is_shutdown()):
	rospy.spin()

