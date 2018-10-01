'''
objective: create 2 layer neural network to learn and predict the output of the xor function

basic table:

a|b|output
==========
0|0|0
0|1|1
1|0|1
1|1|0

can also be called a simple perceptron / feed forward neural network
'''


import numpy as np
import time # mainly just to measure time to train etc


# want to define hidden neurons
n_hidden = 10 # number of hidden neurons, 10 values (0,1's)
n_in = 10 # number of inputs
n_out = 10

# sample data
n_samples = 300 # number of samples to generate

# hyperparameters
learning_rate = 0.01 # how fast network should adjust parameters
momentum = 0.9 #
# overall, trying to lower loss function "cross entropy"


# now want to seed random number generator
# "non deterministic seeding"
np.random.seed(0) # helps ensure the same set of random numbers comes out to help with verification

# want to define an activation function, traditional is sigmoid function
def sigmoid(x):
    # aka activation function. this is for one of the two layers
    # turns numbers into probabilities
    return 1.0/(1.0+np.exp(-x))
# each time input data hits a neuron / layer, a number gets turned into a probability
#  now, will use two activation functions because xor specifically the tangent function is easier

def tanh_prime(x):
    # second activation function that just happens to help well with xor function
    return 1-np.tanh(x)**2

# want to define training function
def train(x,t,v,W,bv,bw):
    '''
    x: input data
    t: transpose (help with matrix mult)
    V, W: layers of network
    bv,bw: biases to help with making more accurate predictions
    '''
    # forward propagation. matmult + biases
    A = np.dot(x,V) + bv
    Z = np.tanh(A)

    # next, need 2nd activation function (sigmoid)
    B = np.dot(Z,W) + bw
    Y = sigmoid(B)
    # w/ ff neural network, but now need backward propagation. update weights one way, then back

    # back propagation. E* represents error
    Ew = Y - t
    Ev = tanh_prime(A) * np.dot(W,Ew) # "two deltas that we're getting"
    # ultimately, want Ev value to predict loss, and thus need to compare
    # predicted loss with actual loss and want to minimize loss with this.

    # predict our loss. d* represents deltas
    dW = np.outer(Z,Ew) # two deltas to help predict loss
    dV = np.outer(x,Ev)

    # cross entropy as loss function, because this is classifiction
    loss = -np.mean( t * np.log(Y) + (1-t) * np.log(1-Y) )

    return loss, (dV,dW,Ev,Ew)

def predict(x,V,W,bv,bw):
    ''' want to do a prediction step to estimate end result. will use variables
        that have already been calculated.
    '''
    A = np.dot(x,V) + bv
    B = np.dot(np.tanh(A),W) + bw # final values calculating in our network.
    return (sigmoid(B) > 0.5).astype(int) # result is the prediction, 0 or 1

# time to create layers
V = np.random.normal(scale=0.1, size=(n_in, n_hidden))
W = np.random.normal(scale=0.1, size=(n_hidden,n_out))

# need to initialize biases
bv = np.zeros(n_hidden)
bw = np.zeros(n_out)

# need to generate data which will be an input array of all values
params = [V,W,bv,bw]

# generate data
X = np.random.binomial( 1,0.5,(n_samples,n_in) )
T = X^1 # supposedly the "transpose" but that's weird

# Training Time. will train for 100 epochs
for epoch in range(100):
    err = []
    upd = [0]*len(params)
    t0 = time.clock() # want to time how long this neural network will train (or whatever)

    # for each data point, update our weights of our network
    # objective is to find the xor value of ones and zeroes
    # for each data point, want to update our weights
    for i in range(X.shape[0]):
        loss,grad = train(X[i],T[i],*params)

        # these two loops will help us predict our error
        for j in range(len(params)):
            params[j] -=upd[j]
        for j in range(len(params)):
            upd[j] = learning_rate*grad[j] +momentum*upd[j]

        err.append(loss)
    print('Epoch: %d, Loss: %.8f, Time: %fs' %(epoch,np.mean(err),time.clock()-t0))

# try to predict something
x = np.random.binomial(1,0.5,n_in)
print('XOR prediction')
print(x)
print(predict(x,*params))






# eof
