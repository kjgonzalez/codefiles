'''
Objective: do a little bit of practice with the book "Make Your Own Neural Network", by Tariq Rashid. basically, this code will be from the first part.
'''

# PAGE 19
import numpy as np
import matplotlib.pyplot as plt


# just gonna generate a few points to imitate the image seen

def genPts(n=10,center=(0,0),radius=1.0):
    ''' create n number of (x,y) pts centered at a point, with a given radius) '''
    assert type(n) ==int,"n must be integer"
    assert len(center)==2,"center must be (x,y) coordinate tuple"
    assert float(radius)>0.0,"radius must be greater than zero"

    x=center[0]+(np.random.rand(n)-0.5)*2*float(radius)
    y=center[1]+(np.random.rand(n)-0.5)*2*float(radius)
    return np.array([x,y]).transpose()

caterpillars=genPts(center=(1,4))
ladybirds=genPts(center=(4,1))

# learning parameters
lr = 0.01
# initialize angle of guess
a=0.25 # will just express the angle as a slope

length=5.5

print('iter, estimate, error, d_a, new a')
for i,ipair in enumerate(np.row_stack((caterpillars,ladybirds))):
    # import ipdb; ipdb.set_trace()
    # for each training example, modify variable 'a'
    estimate=a*ipair[0]
    err = estimate-ipair[1]
    d_a=lr*(err/ipair[0])
    a+=-d_a
    print('Iter{}: {}, {:.2f}, {:.2f}, {:.2f}, {:.2f}'.format(i,np.round(ipair,2),estimate,err,d_a,a) )


divline=np.array([[0,0],[length*np.cos(a),length*np.sin(a)]])
plt.plot(caterpillars[:,0],caterpillars[:,1],'b.')
plt.plot(ladybirds[:,0],ladybirds[:,1],'r.')
plt.plot(divline[:,0],divline[:,1],'g-')
plt.grid()
plt.show()
