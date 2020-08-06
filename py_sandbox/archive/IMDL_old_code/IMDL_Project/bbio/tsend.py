# send commands out serially to teensy

import Adafruit_BBIO.UART as UART
import serial
import time
UART.setup("UART1")
# UART.setup("UART2")
ser = serial.Serial(port = "/dev/ttyO1", baudrate=115200)
ser.close()
ser.open()

print "starting"

while(1):
	raw=raw_input("Send to Teensy: ")
	ser.write(raw)
	print "Sent: ",raw,"\n"

