'''
Author: Kris Gonzalez
Created: 181117
Objective: test serial communication between pc & arduino. see *.ino file for
    more information

kjgnote: this is EXTREMELY simple way of receiving data. not recommended,
    because of artificial and lengthy delay. however, this should be enough
    to correctly transmit and receive data.

How to run this script:
>> python3 echo_test_pc.py
'''

import serial
import time
ser = serial.Serial()
ser.baudrate = 9600 # very slow
# ser.timeout = 0.1 # amount of time to wait for new data
ser.port = '/dev/ttyACM2'
# NOTE: in windows, this may be COM*. linux: /dev/tty*

ser.open()
inp=''

while(inp != 'q'):
    inp = input('PC: ')
    if(inp!='q'):
        ser.write(inp.encode())
        time.sleep(0.4)
        print(ser.read_all().decode("utf-8")[:-1]) # remove newline char
ser.close()
print('\nExiting...')
