'''
objective: create listener that will eventually listen only on bluetooth port

KJG181118: so, the following codes are working together:
echo_test_pc.py
_181118_echo_bluetooth.ino
serial_listener_pc.py (this script)

generally, the first two are working fine, but this script is giving lots of
    problems. 
'''

import serial
import time
from sys import argv

ser = serial.Serial()
ser.baudrate = 38400
ser.timeout = 0.1 # amount of time to wait for new data
ser.port = argv[1]

ser.open()
ser.flush()
print('Connection established. baud:'+str(ser.baudrate)+'. CTRL+C to exit')
while(True):
    if(ser.inWaiting()>1):
        # time.sleep(0.4)
        # print(ser.read_all()) # remove newline char

        # inc=ser.read_all()
        inc=ser.readline()
        print(inc)
        print(inc.decode("utf-8")) # remove newline char
# while loop
ser.flush()
ser.close()
print('\nExiting...')


# while(inp != 'q'):
#     ser.write(inp.encode())
#     time.sleep(0.4)
#     print(ser.read_all().decode("utf-8")[:-1]) # remove newline char
#     inp = input('PC: ')
# # while loop
