# python code to try and read from serial

import serial
import time
#this needs to be identified
ser = serial.Serial('/dev/ttyO1',9600)

#clear any previous data
ser.flushOutput()
ser.flushInput()
print "starting"

while True:
	print "..."
	print ser.readline()
	
	time.sleep(.050)


# use comm protocol: 
# receive n separate variables from sensor, print them
