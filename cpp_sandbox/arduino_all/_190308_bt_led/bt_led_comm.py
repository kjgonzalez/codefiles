'''
Author: Kris Gonzalez
Created: 2017-Nov-02
Modified: 190308
Objective: Python counterpart for bluetooth usage. overall behavior will 
    include sending commands TO bluetooth. This demo simply takes in 
    keyboard input in real-time and sends it in the following manner:
    python script >> bluetooth HC05 >> teensy >> serial monitor

ASSUMPTIONS: 
    * only runs on Windows
    * MUST be on python3 (otherwise have bytes/str type issue)
    * HAS BEEN PROVEN TO WORK (KJG190308)
    * see *.ino file for all instructions
'''

import msvcrt # only works on windows (for now, perhaps replaceable with tkinter)
import serial

ser=serial.Serial()
ser.baudrate=38400
ser.port='COM4' #may be different value, but not same as teensy serial
ser.open()

print('Port successfully opened. Ready for input ("q" to exit):')
key=0 # MUST initialize
while(key!=b'q'):
	if msvcrt.kbhit():
		key=msvcrt.getch()
		# ser.write(key+b'\r\n') # MUST include CR+LF, must be bytes type
		ser.write(key)
		print(key) #just to know what was sent

ser.close() # not required, but including for completeness
#eof