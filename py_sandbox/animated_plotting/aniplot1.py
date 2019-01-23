'''
new example that works better than first verison. in this version, update data
instead of using animation library, which seems to be slow.
'''

import matplotlib.pyplot as plt
import numpy as np
import time
x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion() # initialize plot, make interactive

fig = plt.figure() # create plot object
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r.') # Returns a tuple of line objects, thus the comma
def updatey(ydata):
	''' return ydata with noise'''
	return y+np.random.rand(np.size(y))/10
for phase in np.linspace(0, 10*np.pi, 500):
	line1.set_ydata(updatey(y))
	fig.canvas.draw()
	fig.canvas.flush_events()
	print(time.time())
