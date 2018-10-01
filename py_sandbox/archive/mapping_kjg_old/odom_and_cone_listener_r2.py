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
		import tf
		import time
		self.rospy = rospy
		self.Odometry = Odometry
		self.np = np
		self.tf = tf
		self.time = time # temp

		# object properties
		self.odomData=0 # put odometry object data here.
		self.newData=False # if new data available, "True"

		# initialize rosnode
		rospy.init_node(NodeName,anonymous=True)
		rospy.Subscriber(RosTopicName,Odometry,self.callback,queue_size = 1)


	def callback(self,data):
		self.odomData=data.pose.pose
		self.newData=True # set flag to true when new data received
		print 'odom,',self.time.time()
		return None
	def getPose(self):
		''' Objective: return processed pose data of car, which is given in
			global coordinates as (x,y,angle) data, in 2D numpy array.
			KJGNOTE: due to frame rotations, true output data for (x,y)
			is (-x,z) data coming in from current loam data.
		General Steps:
			1. get current data from self.odomData
			2. convert quaternion to yaw data (rotation about vertical axis)
			3. return data as np.array([[x,y,yaw]]) (2D numpy array)

		KJGNOTE: for the moment, will just get x,y data, then later get yaw
		(no internet connection at the moment)
		'''

		''' need to use following transformations because of how data is
			currently in incorrect frame.
			desired coordinate system:
				* y is fwd, x is left, z is up. yaw is about z (left=+)
			current coord sys:
				* z is fwd, x is left, y is up, yaw is about y (pitch, left=+)
		'''

		# initialization check
		if(self.odomData==0):
			# odom listener hasn't yet been activated
			return self.np.array([[0,0,0]])
		# post initialiation code
		# print self.odomData
		ax = self.odomData.orientation.x + 0
		ay = self.odomData.orientation.y + 0
		az = self.odomData.orientation.z + 0
		aw = self.odomData.orientation.w + 0
		x = self.odomData.position.x * (-1)
		y = self.odomData.position.z + 0
		rollpitchyaw = self.tf.transformations.euler_from_quaternion((ax,ay,az,aw))

		yaw = rollpitchyaw[1]
		self.newData=False # consider data to be completely read
		return self.np.array([[x,y,yaw]])
# end of object OdoListen

class ConeListen(object):
	''' objective: listen for new cone location data, then add to set to be
	checked

	KJGNOTE: main class is expecting:
	newconesGlobal  / (local)= (x,y,color) global cone data, 2D numpy array, col dominant

	'''
	def __init__(self):



# a=OdoListen()
# import rospy
# # print 'node starting...'
# # rospy.spin()
#
# import time
#
# try:
# 	a=OdoListen()
# 	rospy.spin()
# 	print 'test'
#
# # try:
# # 	while True:
# # 		time.sleep(1)
# # 		# print a.getPose()
# except KeyboardInterrupt:
# 	print 'User Interrupt, ending node'
#
#
# # try:
# # 	a=OdoListen()
# # 	for i in range(100):
# # 		time.sleep(1)
# # 		print 'sleeping...'
# # except KeyboardInterrupt:
# # 	print 'user input, exiting'
# except rospy.ROSInterruptException:
# 	print 'rospy exception'
# 	exit()
#
#
# # print 'almost ready to quit'
# # rospy.spin()





# eof
