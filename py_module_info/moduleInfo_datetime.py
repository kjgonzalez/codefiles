'''
understand basics of datetime, especially how to quickly convert and modify dates
'''

import datetime as dt
from datetime import datetime as dt2

print('date:',dt.date(2020,10,9))
print('time:',dt.time(23,15,11))
print('now:',dt2.now())
print('yesterday:',dt2.now()-dt.timedelta(1))
res = dt.date(2021,10,3).strftime('%Y%m%d')
print('date2:',res)

res = dt.date(2020,10,9)-dt.date(2019,9,9)

print('diff:',res)
print('from string:',dt2.strptime('20201009','%Y%m%d'))