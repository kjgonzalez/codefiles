#!/usr/bin/env python

'''
try having commandline arguments in the launch file
'''


import rospy
from sys import argv


rospy.init_node('args_node')
print 'all input arguments',len(argv)
for i in argv:
	print i

print 'done'
