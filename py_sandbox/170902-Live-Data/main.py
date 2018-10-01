'''KJG170903: 
	next, try adding in arrow key inputs (or letters) and seeing if the forloop can be changed to an if statement (like, if new data available, update graph)

'''
import numpy as np
import matplotlib.pyplot as plt

n = 1000
width=20

plt.axis([0, n, 0, 1])
plt.ion()
x=[]
y=[]

for i in range(n):
	# 'acquire' data
	x.append(i)
	y.append(np.random.random())
	# reset graph and format
	plt.clf() #kjg test: clear figure first before plotting
	# detail plot
	plt.subplot(211) # initial attempt, subplots
	plt.axis([max(0,i-width), i,0,1])
	plt.plot(x, y)
	# total plot
	plt.subplot(212)
	plt.plot(x,y)
	plt.pause(0.05)

while True:
	plt.pause(0.05)