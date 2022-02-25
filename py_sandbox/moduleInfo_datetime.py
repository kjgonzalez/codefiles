'''
understand basics of datetime, especially how to quickly convert and modify dates
'''

import datetime as dt
from datetime import datetime as dt2

print('date:',dt.date(2020,10,9))
print('time:',dt.time(23,15,11))
print('now:',dt2.now())
print('yesterday:',dt2.now()-dt.timedelta(1))
