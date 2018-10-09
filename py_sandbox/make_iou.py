'''
objective: create simple iou (intersection over
    union) calculator. later, may improve with
    ability to automatically find nearest box, etc.
'''

import numpy as np

# format of bboxes: (x1,y1,x2,y2)
b1 = np.array([2,2,6,6]) # area = 4x4 = 16
b2 = np.array([4,4,8,8]) # area = 4x4 = 16

# intersection should be 2x2=4
# union should be 28

# def getIOU(b1,b2):
#     # will assume that box format is (x1,y1,x2,y2), and *1<*2.
#     # get intersection

b=np.row_stack([b1,b2])
print b

left=np.max(b[:,:2],0) # get rightmost left side x and y
right=np.min(b[:,2:],0) # get leftmost right side for x and y


leftx=max(b1[0],b2[0])
rightx=min(b1[2],b2[2])
dx=max(0,rightx-leftx)
print dx

lefty=max(b1[1],b2[1])
righty=min(b1[3],b2[3])
dy=max(0,righty-lefty)
print dy

inter = dx*dy
print 'inter:',inter
a1=np.product(b1[2:]-b1[:2])
a2=np.product(b2[2:]-b2[:2])
union = a1+a2-inter
print 'union:',union
