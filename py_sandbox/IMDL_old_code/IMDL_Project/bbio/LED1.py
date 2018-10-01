#!/bin/python

import ledControl as led
from time import sleep

for i in range(4):
	led.init(i)

i=0
while(1):
	led.on(i)
	sleep(0.3)
	led.off(i)
	i+=1
	if(i==4):
		i=0
