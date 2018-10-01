'''
Author: Kris Gonzalez
Date Created: 180511
Objective: create node to get relative cone positions and absolute car
	position data, then return where cones are in absolute coordinates.

kjgnote: first, will simulate random cone locations. will set overall loop
time of program to 1hz, in order to go slowly.

step 1: generate a constant output of cone locations with some noise.
later on, want to do them out of order as well...?

kjgnote about orientation: all cones lie in x-y plane. y is
forward, x is right, and z is up (out of page). coordinates are to always
be given in x-y-z values.

kjgnote: have buckled and will definitely use np arrays everywhere, not just
within functions. forget the other stuff...

kjgnote: currently, two schools of thought on how to figure out if a cone has
already been seen:
1. lookup method. get a cone in global coordinates, then check euclidian
distance to nearest cone. if within a certain threshold, ignore / add to an
average. if outside threshold, add to list.

2. some sort of kalman filter. take known positions of cones. when car moves,
estimate that they should be. take a measurement, then check again.



'''

# initializations ==============================================================
import time
from random import random
import matplotlib.pyplot as plt

def addnoise(arr,k=1):
		''' add mu=0 centered gauss noise to numpy array given, simulate
			real-world noise.
		arr = numpy array, 2D
		k = scale factor. default is 1
		'''
		import numpy as np
		r=arr.shape[0]
		c=arr.shape[1]
		return arr+(np.random.rand(r,c)-0.5)*k

def cs_transform(oldcoord,pose):
	''' Objective: take old coordinate value(s), return new within new 2D
		coordinate system. will be primarily used for transforming cone local
		coordinates to global coordinates. global coordinate system is relative
		to starting position of car, assuming LOAM is used from lidar data

	oldcoord = numpy array of 2D (x,y) cone data, allows 1 or more cones
	pose = numpy array of (x,y,angle) data. angle is in radians
	return: newcoord = numpy array of (x,y) global cone data

	general steps:
	1. receive a single cone coordinate and pose
	2. put into matrices
	3. transform
	4. return new value as tuple
	'''
	import numpy as np

	# create x_old col vector
	# receiving 2D cone data, col-dominant x/y values
	ones=np.ones((len(oldcoord),1))
	x1=np.column_stack((oldcoord,ones)).transpose()
	angle=(-1.0)*pose[2] # radians. -1 necessary because referring to old cs
	s=np.sin(angle)
	c=np.cos(angle)
	tx=pose[0]
	ty=pose[1]
	T = np.array([[c,s,tx],[-s,c,ty],[0,0,1]])
	# print T
	x2=np.matmul(T,x1)
	# print x2
	# return (float(x2[0]),float(x2[1]))
	return x2[0:2].transpose()

# at this point, have transformed all cones into global coordinates
# now, want to start identifying whether or not a set of cones have already
# been seen or not... although this is probably something already covered
# in kalman filters... ?

'''
at this point, want to simulate the car standing still, but having noise while
looking at some cones. will use function to simulate this and see if data
becomes more accurate over time.

'''


# debugging region =============================================================

class ConeList(object):
	''' class to handle cone list, maintenance, etc. will use numpy to speed up
		operations and provide compatability with other code. cone data is
		assumed to always be in global coordinates. local cone data requires the
		car's global pose.

	desired functions:
	 	evaluate global cone values
		evaluate local cone values
		get ConeList
		reset conelist (?)

	'''

	def __init__(self,threshold):
		''' intialize data about object. will assume that object is created when
			nothing has been identified yet, and cones are evaluated later.
		self._cones = main cone list. 2D numpy array, col dominant
		self.thresh = acceptable level of noise that is ignored. used for
			differentiating between what is a new cone and old cone in the
			lookup strategy / method.
		'''
		import numpy as np
		self.np = np
		self._cones='init'
		self.thresh = threshold
		# threshold defines how much noise is allowed for differentiating betwe

	def getlist(self):
		if(type(self._cones) == type('')):
			# no data has been yet given return zero list
			return self.np.array([])
		else:
			return self._cones

	def localToGlobal(self,oldcoord,pose):
		''' Objective: take old coordinate value(s), return new within new 2D
			coordinate system. will be primarily used for transforming cone local
			coordinates to global coordinates. global coordinate system is relative
			to starting position of car, assuming LOAM is used from lidar data
		NOTE: in this context, 2D means numpy array has 2 non-empty dimensions,
			wherever this is stated.

		oldcoord = numpy array of 2D (x,y) cone data, allows 1 or more cones
		pose = numpy array of (x,y,angle) data. angle is in radians
		(return) = (x,y) global cone data. 2D numpy array, col dominant

		general steps:
		1. receive a single cone coordinate and pose
		2. put into matrices
		3. transform
		4. return new value as tuple
		'''
		# create x_old col vector
		# receiving 2D cone data, col-dominant x/y values

		ones=self.np.ones((len(oldcoord),1))
		x1=self.np.column_stack((oldcoord,ones)).transpose()
		angle=(-1.0)*pose[2] # radians. -1 necessary because referring to old cs
		s=self.np.sin(angle)
		c=self.np.cos(angle)
		tx=pose[0]
		ty=pose[1]
		T = self.np.array([[c,s,tx],[-s,c,ty],[0,0,1]])
		# print T
		x2=self.np.matmul(T,x1)
		# print x2
		# return (float(x2[0]),float(x2[1]))
		return x2[0:2].transpose()

	def eval_globalcones(self,newconesGlobal):
		''' will follow lookup strategy here. given a set of global cone data,
			need to evaluate whether the cones have already been detected.

		newconesGlobal = (x,y) global cone data, 2D numpy array, col dominant
		(return) = how many cones have been accepted into array, scalar integer

		general steps, following lookup method:
		1. take each iNEWcone
		2. compare xy location with known jOLDcone list
		3. if euclidian distance  is below a threshold, accept iNEWcone into
			array. if it is over that threshold, reject cone. add to counter
		4. when complete, return number of cones accepted.
		basic steps:
			D = zeros(len(K),len(U))
			for ik in len(K):
				for ju in len(U):
					D[ik,ju] = 2norm(K[ik,:],U[ju,:])
			for i in len(D[0,:]):
				if(min(D[:,j]) > threshold):
					K=np.row_stack(K,U[j,:])
		'''

		# initial run of object, meaning it has no data yet. add here
		if(type(self._cones)==type('')):
			self._cones = self.np.matmul(self.np.identity(len(newconesGlobal)),newconesGlobal)
			# print 'would return here value of',len(newconesGlobal)
			return len(newconesGlobal)
		# end initial run section

		U = newconesGlobal # make easier to refer to new cone array
		K = self._cones     # make easier to refer to old cone array
		l_k = K.shape[0]   # ease of use
		l_u = U.shape[0]   # ease of use
		D = self.np.zeros((l_k,l_u)) # initialize. requires tuple
		norm = self.np.linalg.norm
		# import ipdb; ipdb.set_trace()
		# this nested forloop should be improved if possible
		for ik in range(len(K)):
			for ju in range(len(U)):
				D[ik,ju] = norm(K[ik,:] - U[ju,:])
		# at this point, have list of cone locations
		addedCounter=0
		for jcol in range(D.shape[1]): # for all columns in D
			if( min(D[:,jcol]) > self.thresh ):
				# distance from other cones is greater than allowable range. add to stack
				addedCounter=addedCounter+1
				self._cones = self.np.row_stack((self._cones,U[jcol,:])) # can be improved
		# print 'able to add this many new items',addedCounter
		return addedCounter

	def eval_localcones(self,newconesLocal,carPose):
		''' given a set of local cone data, need to evaluate whether the cones
			are part of global set. this method combines two other methods:
			convert new cone data to global coordinates, then run
			eval_globalcones and return result here.
		newconesLocal = numpy 2D array of (x,y) local cone data, column dominant
		carPose = numpy 2D array of (x,y,angle) car data
		(return) = how many cones have been accepted into array, scalar integer

		'''
		newconesGlobal = self.localToGlobal(newconesLocal,carPose)
		return self.eval_globalcones(newconesGlobal)


# debugging region end =========================================================


# at this point, have an initial method in order to find all cones. next,
# build here the listener for the odometry data.

# KJGNOTE: will instead develop listener in separate file, then integrate












# component testing ============================================================


import numpy as lala
conesLocal=lala.array([
[-2,1],[-2,3],[-2,5],[-2,7],[-2,9],[-2,11],
[2,1],[2,3],[2,5],[2,7],[2,9],[2,11]  ])

carPose = lala.array([3,4,lala.radians(0)])
carGlobal = carPose[0:2]
carLocal = lala.array([0,0])
# note about carPose:
#	value0 = x location
#	value1 = y location
#	value2 = car angle relative to starting position, radians

noise=.1 # note: this is an actual value in meters of noise in both x and y


# try out the object here
# allcones=ConeList(noise*1.5)
# print 'init number of cones',allcones.getlist(),'// len:',len(allcones.getlist())
#
# # at this point, have no cones in array
# print 'first run:',allcones.eval_localcones(conesLocal,carPose)
# # because this is the first run of eval, all are added.
#
# # next run, eval same cones, but already in global coordinates
# conesGlobal=cs_transform(conesLocal,carPose)
# print 'next, same in global',allcones.eval_globalcones(conesGlobal)
#
# # next run, actually evaluate same cones, but with new data
# conesG_noise=addnoise(conesGlobal,noise)
# print 'same cones, noise:',allcones.eval_globalcones(conesG_noise)
#
# # now actually add a new cone to array
# newconeLocal = lala.array([[5,1]])
# print 'one new cone: ',allcones.eval_localcones(newconeLocal,carPose)
# print 'curr cones:',allcones.getlist(),'// len:',len(allcones.getlist())
# # import ipdb; ipdb.set_trace()
#
# conesLocal2=conesLocal # noise is added here
# conesGlobal=cs_transform(conesLocal,carPose)

# initialize plot
plt.ion()
fig=plt.figure()
flocal=fig.add_subplot(121)
plt.grid() # turn on grid
plt.xlim(-10,10)
plt.ylim(-1,19)
flocal.set_aspect(1)
pcarL,=flocal.plot(carLocal[0],carLocal[1],'k^')
pcarL.set_markersize(15)
pconesL,=flocal.plot(conesLocal2[:,0],conesLocal2[:,1],'bo')
pconesL.set_markersize(10)

fglobal=fig.add_subplot(122)
plt.grid()
plt.xlim(-10,10)
plt.ylim(-20,20)
fglobal.set_aspect(1)
pcarG,=fglobal.plot(carGlobal[0],carGlobal[1],'k',marker=(3,1,lala.degrees(carPose[2])))
# kjgnote: marker argument allows user to rotate marker orientation easily
pcarG.set_markersize(15)
pconesG,=fglobal.plot(conesGlobal[:,0],conesGlobal[:,1],'bo')
pconesG.set_markersize(10)

if True: # using if True to just get thru code quickly while debugging class
	# update local plot
	conesLocal2=addnoise(conesLocal,noise)
	pconesL.set_xdata(conesLocal2[:,0])
	pconesL.set_ydata(conesLocal2[:,1])
	# update global plot
	conesGlobal=cs_transform(conesLocal2,carPose)
	pconesG.set_xdata(conesGlobal[:,0])
	pconesG.set_ydata(conesGlobal[:,1])
	fig.canvas.draw()
	time.sleep(0.3)
















#eof
