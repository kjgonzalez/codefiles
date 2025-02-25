'''
Implement own code to follow examples from Robotics, Vision and Control by Peter Corke
'''


import numpy as np
import matplotlib.pyplot as plt

def pdf_normal(x,mean=0,std=1):
    return np.exp(-(x-mean)**2/(2*std**2))/(2*np.pi*std**2)**0.5

def gen_pdf_data(mean,var):
    lim = var**0.5*4
    x = np.linspace(mean-lim,mean+lim,100)
    y = pdf_normal(x,mean,var**0.5)
    return x,y

def example1_6p4a():
    '''
    Fig 6.4a, initial PDF has a mean value of xhat_k = 2 and variance P_k = 0.25. odometry is 2,
      variance V = 0. recall: std**2 = variance
    '''
    x = 2 # nominal / mean value
    p = 0.25 # variance "matrix"
    d = 2 # odometry value
    v = 0 # odometry variance
    x2 = x+d
    p2 = p + v
    # plot everything
    pp:plt.Axes
    f, pp = plt.subplots()
    pp.plot(*gen_pdf_data(x,p),'-b')
    pp.plot(*gen_pdf_data(x2,p2),':r')
    pp.grid()
    plt.show()

def example1_6p4b():
    x = 2 # nominal / mean value
    p = 0.25 # variance "matrix"
    d = 2 # odometry value
    v = 0.5 # odometry variance
    x2 = x+d
    p2 = p + v
    # plot everything
    pp:plt.Axes
    f, pp = plt.subplots()
    pp.plot(*gen_pdf_data(x,p),'-b')
    pp.plot(*gen_pdf_data(x2,p2),':r')
    pp.set_ylim([0,1])
    pp.grid()
    plt.show()










if(__name__ == '__main__'):
    print('hi')
    # example1_6p4a()
    example1_6p4b()



# eof
