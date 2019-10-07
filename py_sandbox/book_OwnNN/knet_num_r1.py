'''
Author: Kris Gonzalez
DateCreated: 190320
Objective: Improve final network created to be able to do new things.
KJG191004: want to be able to have as many hidden layers as wanted, so will need
    to generalize this in feed forward, backprop, etc


Overall goals:
    * save model to avoid retraining
    * get more data on model train/test phases
    * add sliding window capability for basic detection, not just classification.

things to add:
STATUS | DESCRIPTION
done   | basic network working based on book
done   | network contained in a class
done   | able to load and save weights
done   | network can be forced to retrain
????   | network can have a desired number of layers
????   | network can be configured as wanted (based on given input)
'''
import numpy as np
import os, argparse, time

class NeuralNetwork:
    def __init__(self,LayerList,learningrate):
        self.inodes = LayerList[0]
        self.hnodes = LayerList[1]
        self.onodes = LayerList[2]
        self.lr = learningrate
        self.wih = np.random.rand(self.hnodes,self.inodes)-0.5 # xx needs to be generalized
        self.who = np.random.rand(self.onodes,self.hnodes)-0.5 # xx needs to be generalized

        # scipy.special.expit replacement
        self.activation_function = lambda x:1/(1+np.exp(-np.array(x)))

    def saveWeights(self,filename='wts.npz'):
        ''' Save weights to binary file. Will use numpy for simplicity and
            convenience.
            '''
        np.savez(filename,wih=self.wih,who=self.who)
        print('weights saved.')

    def loadWeights(self,filename='wts.npz'):
        ''' Load weights from binary file. Using numpy. '''
        z=np.load(filename)
        self.wih=z['wih']
        self.who=z['who']
        print('weights loaded.')

    def train_one(self,inputs_list,targets_list):
        # train network
        # prepare input arguments
        ''' quick note:
        input: (784,1)
        wih: (200,784)
        woh: (10,200)
        hidden_outputs: (200,1)
        final_outputs: (10,1)
        ----
        hidden_outputs = wih @ input >>>>>>>  should be called h0 (hidden outputs 0)
        final_outputs  = woh @ hidden_outputs >> should be called out (output final)

        '''



        inputs = np.array(inputs_list,ndmin=2).T
        targets = np.array(targets_list,ndmin=2).T

        #signals leaving hidden layer
        hidden_outputs = self.activation_function(np.dot(self.wih,inputs)) # used for training

        # estimates to compare with errors
        final_outputs = self.activation_function(np.dot(self.who,hidden_outputs)) # used for training

        # do some backpropagation / SGD solving:
        # error is (target-actual)
        output_errors=targets-final_outputs

        # hidden layer error gets split by weights
        hidden_errors = np.dot(self.who.T,output_errors)

        # update weights for links between hidden and output layers
        # kjg190304: remember, THIS IS THE KEY LINE
        self.who +=self.lr*np.dot( (output_errors * final_outputs * (1.0-final_outputs) ), np.transpose(hidden_outputs) )
        # update weights for links between input and hidden layers
        self.wih +=self.lr*np.dot( (hidden_errors * hidden_outputs *(1.0-hidden_outputs)), np.transpose(inputs))

    def train_full(self,dataset,epochs=1):
        ''' Run complete training phase '''
        for iepoch in range(epochs):
            for idat in dataset:
                nn.train_one(*idat)
            # idat_loop
        # iepoch_loop
        print('training complete')

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

    p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument('--retrain',default=False,action='store_true',help='Force network to retrain, even if weights exist')
    args=p.parse_args()

    # NETWORK INITIALIZATION ===============================
    print('Starting network')
    i_n=784 # affected by input data # xx needs to be generalized
    h_n=200 # this value is arbitrary # xx needs to be generalized
    o_n=10  # affected by output data # xx needs to be generalized
    layers=[i_n,h_n,o_n]
    LR=0.1  # this value is arbitrary
    nn=NeuralNetwork(layers,LR)

    # DATA LOADING =========================================
    print('will load data')
    # format labels and answers as needed to be read by network
    dataset=[]
    for irow in open('../../lib/data/mnist_5k.csv'):
        iraw=irow.strip().split(',')
        ival=int(iraw[0])

        # don't need to reshape, but do need to remap to 0.01-0.99
        iimg=(.98/255)*(np.array(iraw[1:]).astype(float))+.01
        ians=np.zeros(10)+0.01 # initialize all values as "low"
        ians[ival]=0.99 # set location of answer to be the "high" value
        dataset.append([iimg,ians]) # aka inputs and targets
    # forloop
    print('done')
    # split dataset into training and validation
    ntrain=4500
    ds_train=dataset[:ntrain]
    ds_test =dataset[ntrain:]

    # TRAINING PHASE =======================================
    # start of training (note: about 1130samples/second at 100 hidden nodes.
    #   about 54s to train 60k)

    def retrain_fn():
        # simple workaround to retrain in case of various conditions
        t0=time.time()
        nn.train_full(ds_train)
        time_train=time.time()-t0
        print('time to train:',time_train)
        print('number of training samples:',len(ds_train))
        print('samples/second in training:',len(ds_train)/time_train)
        nn.saveWeights()

    if(os.path.exists('wts.npz')):
        if(args.retrain):
            # override weights, retrain
            print('user override. retraining')
            retrain_fn()
        print('loading pretrained model')
        nn.loadWeights()
    else:
        print("weights don't exist, training")
        retrain_fn()
    # TESTING PHASE ========================================
    # at this point, need to actually "score" the networkn=0
    t0=time.time()
    scorecard=[] # append 1 if right, 0 if wrong
    for idat in ds_test:
        answer=np.argmax(idat[1])   # load ground truth answer
        pred_raw=nn.query(idat[0])  # get raw values from network
        predict=np.argmax(pred_raw) # interpret prediction
        scorecard+= [1] if(answer==predict) else [0] # append answer
        # import ipdb;ipdb.set_trace()
    time_test=time.time()-t0
    print('time to test:',time_test)
    print('samples/second in testing:',len(ds_test)/time_test)
    # once the test set has been iterated through, get (%) correct as score:
    print('network performance:',sum(scorecard)/len(scorecard))
    # import ipdb;ipdb.set_trace()

# eof
