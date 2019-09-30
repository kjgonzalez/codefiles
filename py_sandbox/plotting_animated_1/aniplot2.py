'''
new example that works better than first verison. in this version, update data
instead of using animation library, which seems to be slow.

r2: new objective is to try and condense the code more

sources:

create custom polygon (with own orientation)
https://stackoverflow.com/questions/23345565/is-it-possible-to-control-matplotlib-marker-orientation


'''
import numpy as np

class quickplot(object):
	''' make a simple object that takes in xy data and plots it, then updates
	when called.
	desired methods:
		change x/y data
		change formatting
		redraw / update plot

KJGNOTE: if you want to change the axis limits, use plt.ylim([lower,upper]),
then redraw using fig.canvas.draw()

	'''

	def __init__(self,xdata,ydata,lineformat='b-'):
		import matplotlib.pyplot as _plt
		self._plt = _plt
		_plt.ion()
		self.fig = _plt.figure() # create figure to plot in
		self.ax = self.fig.add_subplot(111) # create single plot area in figure
		# KJGNOTE about subplot: (132)=(rcn), r=rows,c=cols,n=subplot reference
		self.line=self.ax.plot(xdata,ydata,lineformat)[0] # returns tuple, need index
		self.fig.canvas.draw()
		# at this point, object is initialized and ready to plot

	def setxy(self,xdata,ydata):
		''' change x and y data, but mut have matching lengths'''
		if(len(xdata)==len(ydata)):
			self.line.set_xdata(xdata)
			self.line.set_ydata(ydata)

		else:
			print('ERROR: data is not same length. will not update')
	# def getxy(self):
	# 	'''return xy data so that someone may do something with it'''
	# 	return self.line.get_data()
	# def redraw(self):
	# 	'''main function to update once new data is given'''
	# 	self.fig.canvas.draw()
	# 	# self.fig.canvas.flush_events()
	def updatexy(self,xdata,ydata):
		if(len(xdata)==len(ydata)):
			self.line.set_xdata(xdata)
			self.line.set_ydata(ydata)
			self.fig.canvas.draw()
			self.fig.canvas.flush_events()
		else:
			print('ERROR: data is not same length. will not update')
	def close(self):
		self.plt.close()

x=np.linspace(0,6)
y=np.cos(x)

plotme=quickplot(0,0,'r.')
plotme.setxy(x,y)
plotme.redraw()
a=raw_input('test')




# non object way to do it
# x = np.linspace(0, 6*np.pi, 50)
# y = np.sin(x)

# plt.ion() # initialize plot, make interactive
# fig = plt.figure() # create plot object
# ax = fig.add_subplot(111)
# line1, = ax.plot(x, y, 'r.') # Returns a tuple of line objects, thus the comma
# def updatexy(ydata):
# 	''' return ydata with noise
# 	updated functionality:
# 		1. get length
# 		2. add 1 more element
# 		3. return new arrays (x and y)
# 		testing: can this all handle increasing amounts of data
# 		yes, it can handle increased amounts of data
# 	'''
# 	n = len(ydata)
# 	x = np.linspace(0, 6*np.pi, n+1)
# 	ydata = np.sin(x)+np.random.rand(np.size(x))/10
# 	return (x,ydata)
# 	# return y+np.random.rand(np.size(y))/10
#
# for phase in np.linspace(0, 10*np.pi, 500):
# 	time.sleep(0.1)
# 	x,y = updatexy(y)
# 	line1.set_xdata(x)
# 	line1.set_ydata(y) # change the data
# 	fig.canvas.draw()			# redraw the data
# 	fig.canvas.flush_events()	# remove extra changes that were too fast
# 	print(time.time())
