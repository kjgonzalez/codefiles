import matplotlib.pyplot as plt
import time
import numpy as np
import matplotlib.pyplot as plt

plt.axis([0, 100, 0, 1])
plt.ion()
plt.show()

for i in range(100):
    y = 10*(np.random.random()+np.random.random())/2
    print type(y)
    plt.scatter(i, int(y))
    plt.draw()
    time.sleep(0.05)
