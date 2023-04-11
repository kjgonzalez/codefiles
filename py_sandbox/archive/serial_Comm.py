#basic interface to communicate with teensy via serial

import serial
import msvcrt

ser=serial.Serial()
ser.baudrate=115200 #revise later
ser.port='COM3'
ser.open()

key=0
while(key!='q'):
    if msvcrt.kbhit():
        key=msvcrt.getch()
        ser.write(key)
    a= ser.read_all().strip()
    if(len(a)>1):
        print(a)

print("exiting program")
ser.close()
