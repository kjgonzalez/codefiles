'''
Author: Kris Gonzalez
DateCreated: 190213
Objective: follow along in "make your own neural network" and make a self-made
    network.
    
NOTES:
    * sigmoid function: y = 1/(1+exp(-x))
'''
import numpy as np
import matplotlib.pyplot as plt
import scipy.special

class NeuralNetwork:
    def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        self.lr = learningrate
        self.wih = np.random.rand(self.hnodes,self.inodes)-0.5
        self.who = np.random.rand(self.onodes,self.hnodes)-0.5
        # self.activation_function = lambda x:1/(1+np.exp(-x)) # scipy.special.expit
        self.activation_function = lambda x: scipy.special.expit(x)

    def train(self,inputs_list,targets_list):
        # train network
        # prepare input arguments
        inputs = np.array(inputs_list,ndmin=2).T # not sure why T or ndmin
        targets = np.array(targets_list,ndmin=2).T # not sure why T or ndmin
        
        
        # signals into hidden layer
        hidden_inputs  = np.dot(self.wih,inputs)
        #signals leaving hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # signals into output layer
        final_inputs = np.dot(self.who,hidden_outputs)
        final_outputs = self.activation_function(final_inputs)		
        
        # error is (target-actual)
        output_errors=targets-final_outputs
        
        # hidden layer error gets split by weights
        hidden_errors = np.dot(self.who.T,output_errors)
        
        # update weights for links between hidden and output layers
        # kjg190304: remember, THIS IS THE KEY LINE
        self.who +=self.lr*np.dot( (output_errors * final_outputs * (1.0-final_outputs) ), np.transpose(hidden_outputs) )
        # update weights for links between input and hidden layers
        self.wih +=self.lr*np.dot( (hidden_errors * hidden_outputs *(1.0-hidden_outputs)), np.transpose(inputs)) 

    def query(self,inputs_list):
        # test network on something
        
        # prepare input arguments
        inputs = np.array(inputs_list,ndmin=2).T # not sure why T or ndmin
        
        # signals into hidden layer
        
        hidden_inputs  = np.dot(self.wih,inputs)
        #signals leaving hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)
        
        # signals into output layer
        final_inputs = np.dot(self.who,hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs
        
# class NeuralNetwork


# run if main program
if(__name__=='__main__'):
    print('Starting network')
    i_n=784
    h_n=100
    o_n=10
    LR=0.3
    nn=NeuralNetwork(i_n,h_n,o_n,LR)
    #print("current output:\n",nn.query([1,0.5,-1.5]))
    
    print('will load data')
    # format labels and answers as needed to be read by network
    dataset=[]
    for irow in open('mnist_train_100.csv'):
        iraw=irow.strip().split(',')
        ival=int(iraw[0])
        iimg=np.array(iraw[1:]).astype(float) # don't need to reshape
        ians=np.zeros(10)+0.01 # initialize all values as "low"
        ians[ival]=0.99 # set location of answer to be the "high" value
        dataset.append([iimg,ians]) # aka inputs and targets
    # forloop
    print('done')

    for idat in dataset[:1]:
        nn.train(*idat)




# eof
