#!/bin/python

import ledControl as led

for i in range(3):
	led.cleanup(i)

print "done"
