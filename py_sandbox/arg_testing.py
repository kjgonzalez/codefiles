'''
Objective: check argv and see if it can crash if improper arguments are given

things to test: 
number of arguments given
type of arguments (data type)
'''

from sys import argv
import os

# kjgnote: argv[0] is always the filename of the program. do not use this

print 'testing'

print 'if you see this, didn''t work'



# step 1: test if video exists




desvid = argv[1]
print 'vid exists?',os.path.exists(desvid)

# step 2: test if frames is a number
desFrames = int(argv[2])
print 'frames?',desFrames

# step 3: test if output exists
desOutput = argv[3]
print 'output?',os.path.exists(desOutput)


