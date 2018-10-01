'''
Author: Kris Gonzalez
Objective: do a step response to better understand behavior of turtlebot when
	turning.
General Steps:
1. set desired angle0
2. drive forward at desangle for N seconds
3. set desired angle1
4. drive forward at desangle for N seconds
5. repeat, always recording des angle, actual, and error
'''
import rospy
import numpy as np
import time
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from path_planning.msg import drive_instructions
from std_msgs.msg import Float32

class OdometryObject(object):
	''' Objective: simplify where car state information is saved. this object
		handles everything that must be done to obtain odometry data.
	'''
	def __init__(self,topicname):
		import rospy
		from nav_msgs.msg import Odometry
		import numpy as np
		import tf
		self.rospy = rospy
		self.np = np
		self.tf = tf
		self.Odometry = Odometry
		#simplified, 6-value vector (x,y,theta,vx,vy,vtheta)
		self._carstate_ = np.linspace(0,0,6) # underscore = 'hidden'
		self._raw_ = Odometry() #all odometry data, as-is
		self.flag = False # flag for when new data available
		rospy.Subscriber(topicname,Odometry,self.call_odom,queue_size=10)
	# def __init__
	def call_odom(self,data):
		# mainly want state data, won't touch covariance (yet)
		# state data: x,y,theta,xvel,yvel,thetavel ?
		self.flag=True
		self._raw_ = data
		ax = data.pose.pose.orientation.x + 0.0 # ensure float
		ay = data.pose.pose.orientation.y + 0.0
		az = data.pose.pose.orientation.z + 0.0
		aw = data.pose.pose.orientation.w + 0.0
		x = data.pose.pose.position.x + 0.0
		y = data.pose.pose.position.y + 0.0
		vx = data.twist.twist.linear.x
		vy = data.twist.twist.linear.y
		vtheta = data.twist.twist.angular.z
		rpy = self.tf.transformations.euler_from_quaternion((ax,ay,az,aw))
		self._carstate_=np.array([x,y,rpy[2],vx,vy,vtheta])
	# def call_odom
	def getstate(self):
		self.flag = False # data has now been accessed
		return self._carstate_
	# def getstate
	def getraw(self):
		self.flag = False # data has now been accessed
		return self._raw_
	# def getraw
# class OdometryObject

rospy.init_node('step_response_turtlebot',anonymous=True)
ODOM = OdometryObject('dummy_map_odo')
pub_vel=rospy.Publisher('mobile_base/commands/velocity',Twist,queue_size=10)
pub_des=rospy.Publisher('vals/des',Float32,queue_size=10)
pub_act=rospy.Publisher('vals/act',Float32,queue_size=10)
pub_err=rospy.Publisher('vals/err',Float32,queue_size=10)

while(ODOM.flag==False): # new data not available yet
	print 'waiting for odometry data',time.time()
	time.sleep(0.5)
print 'starting'
angle0=0.0
angle1=np.radians(45.0)
desangle=angle0
t0 = time.time()
tswitch = 10.0

try:
	while(not rospy.is_shutdown()):
		car=ODOM.getstate()
		# print 'actual angle:', car[2]
		# print 'des angle:',desangle
		# print 'error:',desangle-car[2]

		fpub=Float32()
		# publish desired
		fpub.data = np.degrees(desangle)
		pub_des.publish(fpub)

		# publish actual
		fpub.data = np.degrees(car[2])
		pub_act.publish(fpub)

		# publish error
		err_angle = np.degrees(desangle-car[2])
		fpub.data=err_angle
		pub_err.publish(fpub)

		# minor controller
		Kp = 0.01
		comm_turn = Kp*err_angle

		# drive forward
		sendme = Twist()
		sendme.linear.x = 2.0
		sendme.angular.z = comm_turn
		pub_vel.publish(sendme)
		# print 'elapsed:',time.time()-t0


		if(time.time()-t0>=tswitch):
			# toggle between desired, and reset timer
			if(desangle==angle0):
				desangle=angle1
			else:
				desangle=angle0
			t0=time.time()
		time.sleep(0.001)
except ROSInterruptException: pass
#eof
