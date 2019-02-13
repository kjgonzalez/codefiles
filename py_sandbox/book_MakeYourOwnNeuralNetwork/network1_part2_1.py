'''
Author: Kris Gonzalez
DateCreated: 190213
Objective: follow along in "make your own neural network" and make a self-made
	network.
	
NOTES:
	* sigmoid function: y = 1/(1+exp(-x))
'''
import numpy as np

class NeuralNetwork:
	def __init__(self,inputnodes,hiddennodes,outputnodes,learningrate):
		self.inodes = inputnodes
		self.hnodes = hiddennodes
		self.onodes = outputnodes
		self.lr = learningrate
		self.wih = np.random.rand(self.hnodes,self.inodes)-0.5
		self.who = np.random.rand(self.onodes,self.hnodes)-0.5
		self.activation_function = lambda x:1/(1+np.exp(-x)) # scipy.special.expit
	
	def train(self.inputs_list,targets_list):
		# train network
		# prepare input arguments
		inputs = np.array(inputs_list,ndmin=2).T # not sure why T or ndmin
		targets = np.array(targets,ndmin=2).T # not sure why T or ndmin
		
		
		# signals into hidden layer
		hidden_inputs  = np.dot(self.wih,inputs)
		#signals leaving hidden layer
		hidden_outputs = self.activation_function(hidden_inputs)
		
		# signals into output layer
		final_inputs = np.dot(self.who,hidden_outputs)
		final_outputs = self.activation_function(final_inputs)		
		
		
	
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
	i_n=3
	h_n=3
	o_n=3
	LR=0.3
	nn=NeuralNetwork(i_n,h_n,o_n,LR)
	
	print("current output:\n",nn.query([1,0.5,-1.5]))
	

# eof
