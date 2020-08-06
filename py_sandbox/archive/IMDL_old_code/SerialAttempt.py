# python code to try and read from serial

# import serial
# ser = serial.Serial('/dev/ttyACM0',9600)

# ser.flushOutput()
# ser.flushInput()

# parse a string, ',' separator, null terminated
def parseInts(kjgstr):
	from string import count
	vars=range(count(kjgstr,',')+1)
	i=0;
	prev=0;
	n=len(kjgstr)
	cc=0
	while(i<n):
		if(kjgstr[i]==','):
			print cc
			vars[cc]=int(kjgstr[prev:i])
			prev=i+1
			cc+=1
		i+=1
	vars[cc]=int(kjgstr[prev:i])
	return vars

print parseInts(a)


# while(notDone):
	# s.find(a[i:],',',)



# while True:
# 	a = ser.readline()
# 	a=a[0:len(a)-1]

# 	n=len(a)
# 	notdone=1
# 	while(notdone):



# 	# print type(a), len(a), ",",a[0:4]

# 	print a



# use comm protocol: 
# receive n separate variables from sensor, print them