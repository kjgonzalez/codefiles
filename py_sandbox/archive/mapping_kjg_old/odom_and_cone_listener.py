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
import rospy
from nav_msgs.msg import Odometry
from sys import argv
import time
import numpy as np

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
	global odom
	odom = np.array([x,y,z,ax,ay,az,aw])
	# print 'odom_listen:',odom,'||',time.time()
	global f
	endl = '\n'
	com = ','
	f.write(str(time.time())+com)
	f.write(str(x)+com)
	f.write(str(y)+com)
	f.write(str(z)+com)
	f.write(str(ax)+com)
	f.write(str(ay)+com)
	f.write(str(az)+com)
	f.write(str(aw)+com)
	f.write(endl)

	print 'odom_listen capped:',time.time()
	return None

def listener():
	rospy.init_node('odom_listen',anonymous=True)
	rospy.Subscriber('integrated_to_init',Odometry,callback_odom)
	rospy.spin()


print 'Node starting...'
# while True:
f=file(filename+'.csv','w')
f.write('time,x,y,z,ax,ay,az,aw'+'\n')
listener()




# eof
