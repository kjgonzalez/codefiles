'''
Author: Kris Gonzalez
Date Created: 180509
Objective: make simple python script to monitor network download / upload speed

note: in the future, may care about which network
	connection am looking at. for now, will stick to
	ethernet.

possible network connections at sample house:
    Ethernet
    Ethernet 3
    Local Area Connection* 1
    Local Area Connection* 2
    Ethernet 2
    Wi-Fi
    Loopback Pseudo-Interface 1
'''

import psutil
import time
from sys import argv
''' argument inputs:
arg1: cycle period (float)
arg2: number of cycles (int)
arg3: internet source (str)
'''



def getData(source='Ethernet'):
	''' take a snapshot and get absolute values for time, download, upload'''
	data = psutil.net_io_counters(pernic=True)[source]
	return(float(time.time()),float(data.bytes_recv),float(data.bytes_sent))

def calculateRate(dt,source):
	''' given a waiting time (dt [s]), calculate download / upload rates '''
	dat0 = getData(source)
	time.sleep(dt)
	dat1 = getData(source)

	t0 = dat0[0]
	t1 = dat1[0]
	d0 = dat0[1]
	d1 = dat1[1]
	u0 = dat0[2]
	u1 = dat1[2]

	# t0=1.0
	# t1=2.0
	# d0=5.0
	# d1=7.0
	# u0=4.0
	# u1=7.0
	rateDn = round((d1-d0)/(t1-t0)/1024.,1) # results are in Kbps (Kilobits/second)
	rateUp = round((u1-u0)/(t1-t0)/1024.,1) # results are in Kbps (Kilobits/second)
	return (rateDn,rateUp)

if(len(argv)<2):
	print('no "internet source" input arg, using default values')
	s = 1.0
	n = 100
	source='Ethernet'

else:
	s = float(argv[1])
	n = int(argv[2])
	source = argv[3]
	print('Collecting data every',s,'seconds,', n,'times, from',source,'. tuple of (down,up) speeds in Kb/s')

for i in range(n):
	print(calculateRate(s,source))
