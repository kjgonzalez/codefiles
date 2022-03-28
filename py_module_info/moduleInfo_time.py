'''
want to slightly better understand time module

format help:
%Y  Year with century as a decimal number.
%m  Month as a decimal number [01,12].
%d  Day of the month as a decimal number [01,31].
%H  Hour (24-hour clock) as a decimal number [00,23].
%M  Minute as a decimal number [00,59].
%S  Second as a decimal number [00,61].
%z  Time zone offset from UTC.
%a  Locale's abbreviated weekday name.
%A  Locale's full weekday name.
%b  Locale's abbreviated month name.
%B  Locale's full month name.
%c  Locale's appropriate date and time representation.
%I  Hour (12-hour clock) as a decimal number [01,12].
%p  Locale's equivalent of either AM or PM.
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
