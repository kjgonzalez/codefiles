import matplotlib.pyplot as plt
import time
import numpy as np
import matplotlib.pyplot as plt
import serial
from string import count

'''
	1. open port
	2. receive raw data
	3. parse raw data
	4. plot points
	5. repeat 4
'''

# initialize plot
plt.axis([0, 100, 0, 255]) 
plt.ion()
plt.show()

def parseInts(kjgstr):
	vars=range(count(kjgstr,',')+1)
	i=0;
	prev=0;
	n=len(kjgstr)
	cc=0
	while(i<n):
		if(kjgstr[i]==','):
			print cc
			vars[cc]=int(kjgstr[prev:i])
			prev=i+1
			cc+=1
		i+=1
	vars[cc]=int(kjgstr[prev:i])
	return vars

# open port
ser = serial.Serial('/dev/ttyACM0',115200)
ser.flushOutput()
ser.flushInput()

plotmax=0;
plotmin=0;
latestVar=100
firstVar=0
# for i in range(100):

i=0
while(1):

	# print "reading"
	# receive raw data
	raw = ser.readline()
	# parse raw data
	y=parseInts(raw)

	# plot points
	if(y[0]>plotmax):
		plotmax=y[0]*1.1
	if(y[0]<0):
		plotmin=y[0]*1.1
	if(i>100):
		latestVar=i
		firstVar=i-100
	plt.axis([firstVar, latestVar, plotmin, plotmax])

	plt.scatter(i, y[0])
	plt.draw()
	i+=1
	# time.sleep(0.05)



