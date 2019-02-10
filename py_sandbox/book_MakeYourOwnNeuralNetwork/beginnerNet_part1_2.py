#!/usr/bin/env python3.5
'''
Objective: do a little bit of practice with the book "Make Your Own Neural Network", by Tariq Rashid. basically, this code will be from the first part.
'''

# AROUND PAGE 69
import sys
import numpy as np
import matplotlib.pyplot as plt
from klib import pad
nl='\n'
# just gonna generate a few points to imitate the image seen




def sigmoid(arr):
    return 1./(1+np.exp(-np.array(arr)))

print(pad('From pg63 ',50,'=','R')) #===========================================
# this is an example forward pass of the network
x0=np.array([0.9,0.1,0.8]) # input

w1=np.array([[0.9,0.3,0.4],[0.2,0.8,0.2],[0.1,0.5,0.6]])
w2=np.array([[3,7,5],[6,5,2],[8,1,9]])/10

x1=np.matmul(w1,x0[:,None])
y1=sigmoid(x1)

x2=np.matmul(w2,y1)
y2=sigmoid(x2)

out=np.copy(y2)
# print(x2)

gt=np.array([[.5,.6,.7]]).transpose()
e2=gt-y2
e1=np.matmul(w2.transpose(),e2) # i THINK it's w2, not sure at the moment

print('in:\n',x0[:,None])
print('out:\n',np.round(out,3))
print('will approximate error:')
print('ground truth:'+nl,gt) # nl = newline
print('err2:'+nl,e2)
print('err2:'+nl,e1)
# exit()














#
# def genPts(n=10,center=(0,0),radius=1.0):
#     ''' create n number of (x,y) pts centered at a point, with a given radius) '''
#     assert type(n) ==int,"n must be integer"
#     assert len(center)==2,"center must be (x,y) coordinate tuple"
#     assert float(radius)>0.0,"radius must be greater than zero"
#
#     x=center[0]+(np.random.rand(n)-0.5)*2*float(radius)
#     y=center[1]+(np.random.rand(n)-0.5)*2*float(radius)
#     return np.array([x,y]).transpose()
#
# caterpillars=genPts(center=(1,4))
# ladybirds=genPts(center=(4,1))
#
# # learning parameters
# lr = 0.01
# # initialize angle of guess
# a=0.25 # will just express the angle as a slope
#
# length=5.5
#
# print('iter, estimate, error, d_a, new a')
# for i,ipair in enumerate(np.row_stack((caterpillars,ladybirds))):
#     # import ipdb; ipdb.set_trace()
#     # for each training example, modify variable 'a'
#     estimate=a*ipair[0]
#     err = estimate-ipair[1]
#     d_a=lr*(err/ipair[0])
#     a+=-d_a
#     print('Iter{}: {}, {:.2f}, {:.2f}, {:.2f}, {:.2f}'.format(pad(i,2),np.round(ipair,2),estimate,err,d_a,a) )
#
#
# divline=np.array([[0,0],[length*np.cos(a),length*np.sin(a)]])
# plt.plot(caterpillars[:,0],caterpillars[:,1],'b.')
# plt.plot(ladybirds[:,0],ladybirds[:,1],'r.')
# plt.plot(divline[:,0],divline[:,1],'g-')
# plt.grid()
# plt.show()
