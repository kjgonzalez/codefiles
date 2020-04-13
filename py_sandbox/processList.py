'''
date: 200412
objective: summarize and write process list to file.
edit: don't want to save new list every time. instead: take note of what processes are running,
    when they were first detected, how often they're detected, and when the last time detected was.


'''

import os, time
import pandas as pd
from winsound import Beep
# t0=time.time()
# need to be able to parse large string, but issue is splitting individual columns
# procfile = 'C:\Users\kris\Downloads\proc'
procfile = 'C:/Users/kris/Downloads/process_tracking.csv'
assert os.path.exists(procfile), "file doesn't exist:{}".format(procfile)
db = pd.read_csv(procfile)
db.index = db['Name']

raw = os.popen('tasklist').read()
raw2=raw.strip().split('\n')
seps = [0]+[i for i,char in enumerate(raw2[1]) if(char==' ')] + [len(raw2[1])]
processes = []
for irow in raw2[2:]:
    processes.append(  [irow[seps[i]:seps[i+1]].strip() for i in range(len(seps)-1)]  )

# for each row, check if already exists in main db. if yes, edit row. if no, append row.

def nowstr():
    return time.strftime("%Y%b%d-%H:%M:%S",time.localtime(time.time()))
for iproc in processes:
    name = iproc[0]
    if(name in db.index):
        # update data
        db.loc[name] = list(db.loc[name][:2]) + [nowstr()] + iproc[1:]
    else:
        # add data
        db.loc[name] = [name] + [nowstr(),nowstr()] + iproc[1:]

db.to_csv(procfile,index=False)
