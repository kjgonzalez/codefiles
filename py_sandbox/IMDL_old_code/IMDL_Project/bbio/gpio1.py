#!/bin/python

# objective: do some basic gpio with adafruit libraries

import time
import Adafruit_BBIO.GPIO as gpio
import cv2
print "Starting"

gpio.cleanup()
# good pins: 3,4,7,8,14,15,17,18,19
# will use: 7,8,14,15,17

pin_green = "P8_7"
pin_yellow = "P8_8"
pin_red = "P8_14"
pin_blue = "P8_15"
pin_button = "P8_17"
cols=[pin_green,pin_yellow,pin_red,pin_blue]

gpio.setup(pin_green,1)
gpio.setup(pin_yellow,1)
gpio.setup(pin_red,1)
gpio.setup(pin_blue,1)
gpio.setup(pin_button,0)
gpio.add_event_detect(pin_button,gpio.BOTH)
rdy=0;
while(not rdy):
	if(gpio.event_detected(pin_button)):
		rdy=1
	time.sleep(0.5)
	



for j in range(0,2):
	for i in range(0,4):
		gpio.output(cols[i],1)
		time.sleep(.25)
		gpio.output(cols[i],0)

gpio.cleanup()
print "done"





