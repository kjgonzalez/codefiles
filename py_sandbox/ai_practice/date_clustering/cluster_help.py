'''
Objective: setup simple clustering function that will take in a bunch of dates and suggest
    clusters / groups for them.

General Steps:
1. get list
2. load first img
3. load next image, get date difference (days)
4. if less than threshold, same group. else, diff
5. go to 3., repeat till done

reminder: sort numpy array by column: a[a[:,1].argsort()]

# todo: create

'''


# for test data, will assume list of dates already exist as second-based timestamps

import time
import numpy as np # help with keeping rows of data in order
from klib import listContents as lc

# dat=[irow.split(',')[1]) for irow in open('test_data.txt')]
data=[]

def yday(time_in_s):
    # return year-to-day value
    return int(time.localtime(time_in_s).tm_yday)

with open('test_data.txt') as fread:
    for irow in fread:
        iname=irow.split(',')[0][:6]
        itime=yday(float(irow.split(',')[1])) # raw time number
        igroup=0 # initialize groups
        data.append([iname,itime,igroup])

dat=np.array(data,dtype='object')
# sort data by earliest date, even though it should already be in that order
dat=dat[dat[:,1].argsort()]

# print('Sample, 1st 3 lines:')
# print(dat[:3])


# threshold value for new groups
thresh=2

ind_group=0 # initialize group index

# len(dat)-1
print('first row:')
print(dat[0])
print('continuing...')
for i in range(1,len(dat)):
    # will start evaluating at 2nd value in list, not 1st (0'th)
    diff = dat[i,1]-dat[i-1,1]
    print(dat[i],diff)
    if(diff>thresh):
        # assume not part of group. increment for next
        ind_group+=1
        print("next img above dist threshold, new group")
    dat[i,2]=ind_group # add img to "current" group

print('all results:')
[print(irow) for irow in dat[:10]]
print(dat[-1])

print('groups and their counts:')
print(lc(dat[:,2],True))



# eof
