# objective: debug a bit of serial to ensure that main.py both
# starts on BBB reboot and sends serial data automatically


import Adafruit_BBIO.UART as UART
import serial
import time
UART.setup("UART1")
# UART.setup("UART2")
ser = serial.Serial(port = "/dev/ttyO1", baudrate=115200)
ser.close()
ser.open()

def parseInts(kjgstr):
	from string import count
	vars=range(count(kjgstr,',')+1)
	i=0;
	prev=0;
	n=len(kjgstr)
	cc=0
	while(i<n):
		if(kjgstr[i]==','):
			vars[cc]=int(kjgstr[prev:i])
			prev=i+1
			cc+=1
		i+=1
	vars[cc]=int(kjgstr[prev:i])
	return vars


print "Starting..."

i=0
while(1):
		time.sleep(0.05)
		tosend=str(i)+','
		print tosend
		ser.write(tosend)
		
# 		print i
		i+=1
		
		if(i==5):
			i=-4
		

# if the kernel ever gets fixed, enable this code
# UART.cleanup()


