'''
objective: in the end, want to bin 2D data from a set of [x,y,z] values into [r,c,depth] values, for the kitti dataset to project velodyne points into pixel space, but for now will work in 1D.

want to take a vector of float values and bin them into a [0,10] set


fake context: a laser rangefinder mounted on a sliding carriage, goes from 0 
    to 10 meters and measures distances. 30 measurements made. the results are below.
'''

import numpy as np

orig = np.random.rand(2,30) # create a bunch of random values between 0 and 10 with "float indices"
orig[0,:]*=10 # create indices between 0 and 10
orig[1,:]*=30 # create distances measured at each. 
#print(orig)

# next, want to bin them by clumping them into 10 bins 1.0 long, starting at 0
'''bins:
0-1
1-2
2-3
3-4
4-5
5-6
6-7
7-8
8-9
9-10
'''


y_bins = np.arange(-0.5,11) # must encapsulate LHS and RHS of all bins
y_rows=orig[0,:]
z_vals=orig[1,:]
rows = np.digitize(y_rows, y_bins)
#print(rows)
#print('min:{},max:{}'.format(min(rows),max(rows)))
#for i in range(y_rows.size):
    #print(y_bins[rows[i]-1], "<=", y_rows[i], "<", y_bins[rows[i]])

# for each bin, show average

# start w/ bin 1 (0-1)
print('list of distances in each bin:')
for i in range(0,max(rows)): # will start at zero
    print('[{}-{}): {}'.format(y_bins[i],y_bins[i+1],z_vals[i+1==rows]))

print('''
Next example: a laser pointing upwards is now looking at ceiling, measuring distances in 2D
''')

# d = "data"
d = np.random.rand(3,150) # imagine that points were taken in a 10x15 grid (RxC)
d[0,:]*=15 # x values (cols) # 15 cols
d[1,:]*=10 # y values (rows) # 10 rows
d[2,:]*=30 # z values (distances) # values up to 30m

out=np.inf*np.ones((10,15))# want an array of 10 rows, 15 cols
#out=np.zeros((10,15))
#print(out)

# this line provided by christoph wiedemann. for now, may need to use min, not avg.
np.minimum.at(out,( d[1,:].astype(np.int32) , d[0,:].astype(np.int32) ), d[2,:] )

print(np.round(out,0))

print('''
Next example: a laser pointing upwards is now looking at ceiling, measuring distances in 2D
''')










# eof