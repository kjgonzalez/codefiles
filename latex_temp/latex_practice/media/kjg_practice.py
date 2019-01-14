##
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0,5)
y=np.sin(x)
plt.plot(x,y)
plt.grid()
plt.savefig('test.pdf')

