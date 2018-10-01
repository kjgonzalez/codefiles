#!/usr/bin/env python
'''
Objective: simulate turtlebot as the car. this 'car' needs to be improved on.

'''

import rospy
import numpy as np
import time
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from path_planning.msg import drive_instructions


class InstructionObject(object):
	''' handle all rospy drive_instructions operations here
	'''

	def __init__(self,topicname='command_path'):
		import rospy
		import numpy as np
		from path_planning.msg import drive_instructions
		self.rospy = rospy
		self.np = np
		self.drive_instructions = drive_instructions
		rospy.Subscriber(topicname,drive_instructions,self.call_instructions,queue_size=10)
		# data variables
		self.steer = 0
		self.speed = 0.0
		self.mission_done = False
		self.flag_newdata = False
	# def init
	def call_instructions(self,data):
		self.steer = data.steering_angle
		self.speed = data.target_speed
		self.mission_done = data.mission_finished
		self.flag_newdata = True
	# def call_instructions
	def getvalues(self):
		self.flag_newdata = False # data has been read
		return (self.steer,self.speed,self.mission_done)
# class InstructionObject

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


class PIDObject(object):
	def __init__(self, kp, ki, kd):
		self.Kp = kp
		self.Ki = ki
		self.Kd = kd
		self.p_error = 0
		self.i_error = 0
		self.d_error = 0
	# def __init__
	def update_error(self,cte):
		# mainly want state data, won't touch covariance (yet)
		# state data: x,y,theta,xvel,yvel,thetavel ?
		pre_cte = self.p_error

		self.p_error  = cte
		self.i_error += cte
		self.d_error  = cte - pre_cte
		print "p_error ", self.p_error
		print "i_error ", self.i_error
		print "d_error ", self.d_error	
		print "pre_cte ", pre_cte	
		#Update the PID error variables given cross track error cte

	# def call_odom
	def output_steering_angle(self):
		#self.flag = False # data has now been accessed
		PID = -self.Kp*self.p_error - self.Ki*self.i_error - self.Kd*self.d_error
		print self.Kp*self.p_error
		print self.Ki*self.i_error
		print self.Kd*self.d_error
		return PID
	# def getstate

rospy.init_node('driving_turtlebot',anonymous=True)
COMMAND = InstructionObject('command_path')
ODOM = OdometryObject('dummy_map_odo')
pub_vel=rospy.Publisher('mobile_base/commands/velocity',Twist,queue_size=10)
PID = PIDObject(0.2, 0.001, 2.0)
print 'Turtlebot driving sim started'

# main while loop
while(not rospy.is_shutdown()):
	if(COMMAND.flag_newdata == True):
		print COMMAND.getvalues()
		# small attempt at p controller for turning
		rot = ODOM.getstate()[5]
		
		real_angle = ODOM.getstate()[2]
		print "real_angle ", real_angle
		planned_angle = COMMAND.getvalues()[0]
		print "planned_angle ", planned_angle

		#Kp_rot = 0.5
		#turnCommand = Kp_rot*float(COMMAND.getvalues()[0])

		cte = real_angle-planned_angle
		PID.update_error(cte)
          	turnCommand = PID.output_steering_angle()		
		print "turnCommand ", turnCommand


		# instead of superimposing commands, will try sending out only one part at at time
		sendme = Twist()
		sendme.linear.x = COMMAND.getvalues()[1]
		sendme.linear.x = 1.0
		sendme.angular.z = turnCommand
		pub_vel.publish(sendme)

		# print 'turn command',turnCommand
	else:
		time.sleep(0.25)

# main while loop
# rospy.spin()
