'''
objective: try to solve issue of why matplotlib not working properly
'''

import matplotlib.pyplot as plt

import numpy as np

x=np.linspace(0,1)
y=x**2

font = {'fontname':'Bahianita','fontsize':15}
font2 = {'fontname':'Liberation Serif','fontsize':15}

plt.plot(x,y)
plt.title('hello',**font)
plt.xlabel('x-axis',**font2)
plt.ylabel('y-axis',**font2)
# plt.savefig('test.pdf')
plt.show()
