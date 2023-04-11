'''
objective: create listener that will eventually listen only on bluetooth port
'''

import serial
import time
from sys import argv

ser = serial.Serial()
ser.baudrate = 115200
# ser.timeout = 0.1 # amount of time to wait for new data
ser.port = argv[1]

ser.open()
print('Connection established. CTRL+C to exit')
while(True):
    if(ser.inWaiting()>0):
        print(ser.read_all().decode("utf-8")[:-1]) # remove newline char
# while loop
ser.flush()
ser.close()
print('\nExiting...')
