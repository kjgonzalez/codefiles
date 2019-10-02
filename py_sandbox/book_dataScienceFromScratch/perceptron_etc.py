'''
datecreated: 191002
objective: perceptron and basic neural network based on ch18, p228-235. recall
    that a perceptron "approximates a single neuron with n binary inputs"

NOTE: perceptrons only have single linear operation, can't approximate
    non-linear behavior
'''

import numpy as np

def step_function(x):
    return 1.0 if x>=0 else 0.0 # note: not sure why x=0 == 1...?
def sigmoid(x):
    return 1.0/(1+np.exp(-x))
def perceptron_out(weights,bias,x):
    wts=np.array(weights)
    bi=np.array(bias)
    xx=np.array(x)
    calculation = wts@xx+bias
    return step_function(calculation)

def neuronOut(weights,input):
    ''' automatically integrate bias into weights '''
    wts=np.array(weights)
    inp=np.array(input)
    return sigmoid(  wts[:-1]@inp+wts[-1]  )
and_weights=[2,2]
and_bias=-3

and_wt2=[2,2,-3] # includes bias

inputs=[[0,0],[0,1],[1,0],[1,1]]

print('approximating an AND gate:')
for inps in inputs:
    print(inps,':',neuronOut(and_wt2,inps))

''' at this point, want to try feed forward, then later backpropagation '''

def feedforward(neural_network,input):
    inp=input.copy()
    outputs=[]
    for ilayer in neural_network:
        output=np.array([neuronOut(ineuron,inp) for ineuron in ilayer])
        outputs.append(output)
        inp=output.copy()
    return outputs
# eof
xor_net=[
[[20,20,-30],
[20,20,-10]],
[[-60,60,-30]]
]

print(feedforward(xor_net,[0,0])[-1][0])
print(feedforward(xor_net,[1,0])[-1][0])
print(feedforward(xor_net,[0,1])[-1][0])
print(feedforward(xor_net,[1,1])[-1][0])
