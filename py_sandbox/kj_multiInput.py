'''
Author: Kris Gonzalez
CreateDate: 171103
Objective: Output different values depending on what key combinations are pressed.
main keys: W,A,S,D
key combos: 
<none>= 0
W = N,  2
A = W,  4
S = S,  8
D = E,  6
WA= NW, 1
AS= SW, 7
SD= SE, 9
WD= NW, 3
<else>= 0

NOTE: keypad:
1 2 3
4 5 6
7 8 9
  0

General Commands to bluetooth (robocar): 
w = fwd
a = left
s = back
d = right
<can combine for compass-like directions>

<future implementation>: auto/manual, 

'''

# INITIALIZATION ###########################################
# Tkinter setup #
from Tkinter import *
root = Tk() 		# setup root frame
var = StringVar()	# create tk string var
var.set('0')		# initial value
a_label = Label(root,textvariable = var ).pack() # create label object
history = []			# create empty list
v_dir = ''

# Serial Port #
import serial
ser = serial.Serial()
ser.baudrate = 38400	# default baudrate
ser.port = 'COM4'		#outgoing bluetooth port

# Functions #
def keyup(e):			# define f'n
	# print e.char		# when a key is un-pressed, print to screen
	if  e.char in history :	# if the key being unpressed is in history...
		history.pop(history.index(e.char)) #remove it from the list
		# NOTE: LIST IS NOW UPDATED
		v_dir = direction(history)
		var.set(v_dir)	# convert current state of history into string 
		# here, would send the updated command to the serial port.
		
# keyup

def keydown(e):			# define f'n
	if not e.char in history :	# if key isn't alrdy in list...
		history.append(e.char)	# add key to END(!) of list
		# NOTE: LIST IS NOW UPDATED
		v_dir = direction(history)
		var.set(v_dir)		# convert current state of list into string
		# here, would send updated command to the serial port
		
# keydown

def direction(e):
	''' Take in list of currently pressed keys, return direction. General
		steps: 
		1. receive list
		2. check if list has more than two elements
		3. check which two elements active
		4. return direction
		NOTE: keypad:
		1 2 3
		4 5 6
		7 8 9
		  0		'''
	if(len(e)==1):
		# only one button pressed
		if('w' in e):
			return '2'				# NORTH
		elif('a' in e):
			return '4'				# WEST
		elif('s' in e):
			return '8'				# SOUTH
		elif('d' in e):
			return '6'				# EAST
		else:
			return '0'
	elif(len(e)==2):
		if('w' in e and 'a' in e):
			return '1'				# NWEST
		elif('w' in e and 'd' in e):
			return '3'				# NEAST
		elif('s' in e and 'a' in e):
			return '7'				# SWEST
		elif('s' in e and 'd' in e):
			return '9'				# SEAST
		else:
			return '0'
	else:
		return '0'

# MAIN PROGRAM ################
frame = Frame(root, width=200, height=200)	#create frame in main window
frame.bind("<KeyPress>", keydown)	# bind "keydown" fn to keyPRESS
frame.bind("<KeyRelease>", keyup)	# bind "keyup" fn to keyRELEASE
frame.pack()			# activate frame
frame.focus_set()		# set frame in focus
root.mainloop()			# activate whole program


