'''
datecreated: 191002
objective: perceptron and basic neural network based on ch18, p228-235. recall
    that a perceptron "approximates a single neuron with n binary inputs"

NOTE: perceptrons only have single linear operation, can't approximate
    non-linear behavior
'''

import numpy as np

# alright, want to make a class out of this at some point

# class MLP:
#     ''' new, second attempt at basic NN (see book_OwnNN) '''
#     def __init__(self):
#         ''' initialize network '''
#     def afn(self,x):
#         ''' activation function: sigmoid '''
#         return 1.0/(1+np.exp(-x))
#
#     def loadWeights(self):
#         pass
#     def neuronOut(self,weights,input):
#         ''' automatically integrate bias into weights '''
#         wts=np.array(weights)
#         inp=np.array(input)
#         return self.afn(  wts[:-1]@inp+wts[-1]  )
#     def feedforward(self,neural_network,input):
#         ''' perform one pass forward through network '''
#         inp=input.copy()
#         outputs=[]
#         for ilayer in neural_network:
#             # for each layer, apply weights
#             output=np.array([neuronOut(ineuron,inp) for ineuron in ilayer])
#             outputs.append(output)
#             inp=output.copy()
#         return outputs





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

xor_net=[
[[20,20,-30],
[20,20,-10]],
[[-60,60,-30]]
]

print(feedforward(xor_net,[0,0])[-1][0])
print(feedforward(xor_net,[1,0])[-1][0])
print(feedforward(xor_net,[0,1])[-1][0])
print(feedforward(xor_net,[1,1])[-1][0])


# now, at some point, want to be able to train this, so will use backpropagation

def sqerror_gradients(neural_net,input,target):
    '''
    Given a neural network, an input vector, and a target vector,
    make a prediction and compute the gradient of the squared error
    loss with respect to the neuron weights.
    '''

    # forward pass
    outputs, hidden_outputs = feed_forward(network, input_vector)
    # gradients with respect to output neuron pre-activation outputs
    output_deltas = [output * (1 - output) * (output - target)
        for output, target in zip(outputs, target_vector)]
    # gradients with respect to output neuron weights
    output_grads = [[output_deltas[i] * hidden_output
        for hidden_output in hidden_outputs + [1]]
            for i, output_neuron in enumerate(network[-1])]
    # gradients with respect to hidden neuron pre-activation outputs
    hidden_deltas = [hidden_output * (1 - hidden_output) *
        dot(output_deltas, [n[i] for n in network[-1]])
            for i, hidden_output in enumerate(hidden_outputs)]
    # gradients with respect to hidden neuron weights
    hidden_grads = [[hidden_deltas[i] * input for input in input_vector + [1]]
        for i, hidden_neuron in enumerate(network[0])]
    return [hidden_grads, output_grads]





# eof
