'''
Author: Kris Gonzalez
Date Created: 171201
Objective: do some basic serial communication between hermes 
	and rpi via bluetooth. initial config will involve looking 
	at which port each device is connected on. may also need to 
	set up TWO com ports on EACH device (tx & rx), so will be working quite a bit.
'''

import serial
from time import sleep
uniBaudRate = 115200 # revise later
# setup receive port
srx = serial.Serial()
srx.baudrate = uniBaudRate
srx.port = 'COM99' # MUST REVISE !!!!!!!!!!!!!!!!
srx.open()

stx = serial.Serial()
stx.baudrate = uniBaudRate
stx.port = 'COM99' # MUST REVISE !!!!!!!!!!!!!!!!
stx.open()

while True: 
	# will periodically send out message
	stx.write('PC Here')
	if(srx.inWaiting()>0):
		print srx.readline()
	sleep(1)


