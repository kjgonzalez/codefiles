'''
want to slightly better understand time module
'''


import time

# wait a given number of seconds:
time.sleep(0.01)

# raw time in seconds
now = time.time()
print('raw:',now)

# time as a tuple
print('tuple:',time.localtime(now))

# convert that time to a string (string FROM time, strftime)
format="%Y%b%d-%H%M%S"
nowstr = time.strftime(format,time.localtime(now))
print('string:',nowstr)

# convert string to tuple, then to raw
now2=time.mktime(time.strptime(nowstr,format))
print('back to raw, some data lost:',now2)
