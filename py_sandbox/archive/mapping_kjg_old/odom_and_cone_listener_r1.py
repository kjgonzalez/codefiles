'''
Author: Kris Gonzalez
DateCreated: 180512
Objective: want to create practice subscriber for two main topics:
odometry and cone locations. format of each listed below.

Definitions:
	cs, coordsys = coordinate system
	local = local coordinate system, relative to current car position
	global = global coordinate system, relative to initial car position
	2D numpy array = arrays that are not vectors. practically, they are made by
		typing double brackets, e.g. "np.array([[carX,carY,carAngle]])"

Expected Format:
odometry data: 3-element car pose in global cs. 2D numpy array
cone locations: (N-row by 2 or 3) local cone data. 2D numpy array.

KJGNOTE: cone locations may either have 2 or 3 columns, depending on output of
	rosnode. therefore, must be able to reject 3rd column while performing
	computations, then re-adding as needed. if not, must be able to carry third
	column along through all computations, but ignore those values (unless
	later needed by ConeList class)

	input arguments:
	arg1 = output csv filename prefix. default is out<time>
'''

'''
at this point, below code has reached enough maturity to put everything in an
object. want this object to be initialized, then take in odometry data when
needed and then output when received. the way that this program should work is
to internally await an event to receive data, then update both the internal array
as well as a flag that states there's new data available. after this data is read,
then the flag should be set to complete.

general steps:
make listener object. it's updated frequently, but sets a flag that states
there is an unread message. when the object's dat ais read, the flag is set to
"read" and the object continues waiting.
'''

class OdoListen(object):
	def __init__(self,RosTopicName='integrated_to_init',NodeName='Mapper'):
		# object import modules
		import rospy
		from nav_msgs.msg import Odometry
		import numpy as np
		self.rospy = rospy
		self.Odometry = Odometry
		self.np = np

		# object properties
		self.odomData=0 # put odometry object data here.
		self.newData=False # if new data available, "True"

		# initialize rosnode
		rospy.init_node(NodeName,anonymous=True)
		rospy.Subscriber(RosTopicName,Odometry,self.callback)


	def callback(self,data):
		self.odomData=data.pose.pose
		self.newData=True # set flag to true when new data received
		return None



	def getRand(self):
		return 1
# a=OdoListen('a','b')
# print a.getRand()

import rospy
from nav_msgs.msg import Odometry
from sys import argv
import time
import numpy as np
import tf

if(len(argv)<2):
	filename = 'out'+str(time.time())
else:
	filename=argv[1]
print 'output filename:',filename


# odometry listener ============================================================
odom = 0
def callback_odom(dat):
	''' want to listen for any new odometry data, then immediately report it.
	'''
	src = dat.pose.pose
	x = src.position.x + 0
	y = src.position.y + 0
	z = src.position.z + 0
	# note about angles: given in quaternion values
	ax = src.orientation.x + 0
	ay = src.orientation.y + 0
	az = src.orientation.z + 0
	aw = src.orientation.w + 0

	# # get euler rotations
	# temp = tf.transformations.euler_from_quaternion((ax,ay,az,aw))
	# KJGNOTE: output is in roll/pitch/yaw
	# print "RPY:", temp
	# also want these angles just in case.
	global odom
	odom = np.array([x,y,z,ax,ay,az,aw])
	# import ipdb; ipdb.set_trace()
	# print 'odom_listen:',odom,'||',time.time()
	global f
	endl = '\n'
	com = ','
	f.write(str(time.time())+com)
	# f.write(str(x)+com)
	# f.write(str(y)+com)
	# f.write(str(z)+com)
	# f.write(str(ax)+com)
	# f.write(str(ay)+com)
	# f.write(str(az)+com)
	# f.write(str(aw)+com)
	# f.write(str(temp[0])+com)
	# f.write(str(temp[1])+com)
	# f.write(str(temp[2])+com)
	# get euler rotations
	temp = tf.transformations.euler_from_quaternion((ax,ay,az,aw))

	# expected final values:
	f.write(str(x*-1)+com)
	f.write(str(z)+com)
	f.write(str(temp)) # output in radians
	f.write(endl)

	print 'odom_listen capped:',time.time()
	return None

def listener():
	rospy.init_node('odom_listen',anonymous=True)
	rospy.Subscriber('integrated_to_init',Odometry,callback_odom)
	rospy.spin()


# main code to do stuff
print 'Node starting...'
# while True:
f=file(filename+'.csv','w')
f.write('time,x,y,z,ax,ay,az,aw,roll,pitch,yaw'+'\n')
listener()




# eof
