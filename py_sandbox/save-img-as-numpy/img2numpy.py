'''
objective: play around with alternatives to jpg to determine a valid RGB-D format for storage
update: will just store RGB in img format, and D data in npy format

goals: 
1. load image, convert to numpy array, save numpy array
2. compare numpy file and image file and see which is smaller (and what factor)
3. load numpy file and display in image


NOTES:

* previous work: https://stackoverflow.com/questions/9619199/best-way-to-preserve-numpy-arrays-on-disk


CONCLUSION: just use dtype=np.float32. this is the most time-efficient method,
    while still maintaining reasonable file size
eg: np.save('out1b',np.array(depth,dtype=np.float32))


'''


import numpy as np
import matplotlib.pyplot as plt
import cv2
import matplotlib.image as ims
import time
#img=cv2.imread('orig.png')
#img=plt.imread('orig.png') # use this, cv2 assumes BGR, plt assumes RGB
#plt.imshow(img)
#plt.show()

#print('continuing')

##img2=np.array(img)
##plt.imshow(img2)
##plt.show()
#ims.imsave('other.png',img)

#print('continuing')
#img3=np.load('other.npy')

#plt.imshow(img3)
#plt.show()

print('''#############################################
# new direction: just save a third file for lidar ####''')

# 1. get dimensions
# 2. generate random values
# 3. save to npy / other

img=plt.imread('orig.png')
img=np.array(img)
#print(img.shape)
# x=img.shape
depth=100*np.random.rand(*img.shape[:2]) # generate random lidar values in same shape as one channel

print(depth.shape)
np.save('out1a',depth) # simple method, most direct method

# time check on this one
t0=time.time()
np.save('out1b',np.array(depth,dtype=np.float32))
print('elapsed time: ',time.time()-t0)

# converting to integer doesn't help
# try saving only to first 3 digits
#depth2=np.array(100*depth,dtype='int')
#np.save('new2.npy',depth2)

#print(depth2[:4,:4])

# still not working. try saving as png, but with 1st channel as things greater than zero, and 2nd channel as things less than zero. last channel is all zeros


def arrsave(filename,array):
    ''' Objective: Save float array to png in order to maintain 
        compressed size. files will be saved under dist.
    Assumptions:
    * writing out velodyne data, i.e. float array between 0 and 255 (max) meters.
    * will only save integer value (clipped at 255) and first 2 decimal places
    * layers stored as: [integer, decimal01, AllZeros]. dimensions are identical to image
    '''
    out=np.zeros(img.shape)
    d1=np.array(array,dtype='int') # truncate values
    d2=np.array(array-np.array(d1,dtype='float')) # get fractions
    out[:,:,0]=np.clip(d1/255.0,0.0,1.0) # ensure that first values don't exceed max
    out[:,:,1]=np.array(d2*100.0/255.0) # save first 2 digits
    plt.imsave(filename,out,format='png')
# def arrsave

def arrread(filename):
    ''' Objective: load a custom data format, return array'''
    arr=plt.imread(filename,format='png')
    arr=np.array(arr,dtype='float')
    out=arr[:,:,0]*255.0+arr[:,:,1]/100.0*255.0 # recover values up to 2 decimal places
    return out
# def arrsave


print('original lidar:')
print(depth[:3,:3])

# time check on this one
t0=time.time()
arrsave('out2.dist',depth)
print('elapssed time: ',time.time()-t0)
print('file saved')


depth=arrread('out2.dist')
print('reloaded data:\n',depth[:3,:3])



# eof