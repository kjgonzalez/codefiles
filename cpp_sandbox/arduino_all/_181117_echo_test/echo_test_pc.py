'''
Author: Kris Gonzalez
Created: 181117
Objective: test serial communication between pc & arduino. see *.ino file for
    more information

kjgnote: this is EXTREMELY simple way of receiving data. not recommended,
    because of artificial and lengthy delay. however, this should be enough
    to correctly transmit and receive data.

How to run this script:
>> python3 echo_test_pc.py SERIAL_PORT

SERIAL_PORT: user given name of port where board is connected
examples: '/dev/ttyACM2', 'COM0'
# NOTE: in windows, this may be COM*. linux: /dev/tty*

possible ways to list ubuntu serial ports: 
>> dmesg | grep tty
>> ls /dev/tty* | grep AC

'''

import serial
import time
from sys import argv

ser = serial.Serial()
ser.baudrate = 9600 # very slow
# ser.timeout = 0.1 # amount of time to wait for new data
ser.port = argv[1]

ser.open()
inp=''
print('Connection established. Press "q" to exit')
while(inp != 'q'):
    inp = input('PC: ')
    if(inp!='q'):
        ser.write(inp.encode())
        time.sleep(0.4)
        print(ser.read_all().decode("utf-8")[:-1]) # remove newline char
ser.close()
print('\nExiting...')
