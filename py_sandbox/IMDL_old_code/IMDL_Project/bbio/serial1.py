import Adafruit_BBIO.UART as UART
import serial
import time
UART.setup("UART1")
# UART.setup("UART2")
ser = serial.Serial(port = "/dev/ttyO1", baudrate=9600)
ser.close()
ser.open()
print "Serial is open!"
a=[23,1,3,4]

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

b='123,45,6,78,9'
print parseInts(b)

print "starting"

while(1):
		time.sleep(1)
		for i in range(0,len(a)-1):
			ser.write(str(a[i])+',')
		i+=1
		ser.write(str(a[i])+'!')
		kjg= ser.readline()
		kjg=kjg[0:len(kjg)-1]
		print parseInts(kjg)
		

# if the kernel ever gets fixed, enable this code
# UART.cleanup()


