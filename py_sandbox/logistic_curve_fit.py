'''
test
'''

import numpy as np
np.random.seed(0) # keep randomness ... constant
import matplotlib.pyplot as plt

def logistic(xdata,L=1,k=1.0,x0=0):
    '''
    L = maximum load / capacity of system
    k = growth rate
    x0 = inflection point, midpoint
    '''
    return L/(1+np.exp( -k*(xdata-x0) ))

def dPdt(P,Rate,Load):
    return Rate*P(1-P/Load)

x=np.linspace(20,40,100)
print(x.mean())
ypure = logistic(x,k=.25,x0=x.mean())
yreal = ypure + (np.random.rand(*x.shape))*.05



dyreal = yreal[1:]-yreal[:-1]
dx=x[1:]

# f,p=plt.subplots(2,2)
# p=np.reshape(p,4)
# p[0].plot(x,ypure)
# p[0].plot(x,yreal)
# p[0].grid()
#
# p[1].plot(dx,dyreal)
# p[1].grid()
# plt.show()



import matplotlib.pyplot as plt
import numpy as np


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

wide = .99
data = [men_means,women_means,men_means,women_means,men_means]
width = wide/len(data)
x = np.arange(len(labels))  # the label locations

fig, ax = plt.subplots()
# ax.bar(midpoint of each bar, height, width of each bar)
rects = []
for i,idat in enumerate(data):
    rects.append(   ax.bar(x-wide+width/2+(i+3)*width, idat,width)   )


# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ticklocs=x
print(ticklocs)
ax.set_xticks(ticklocs)
ax.set_xticklabels(labels)

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

for irect in rects:
    autolabel(irect)

fig.tight_layout()

plt.show()
exit()

yerr = (np.random.rand(*x.shape))*.05
y=logistic(x,k=.25,x0=30)

y1=y+yerr
x1=-np.log((y1.max()*1.001-y1)/y1)

'''
wanna also plot by numerical approximation
dP/dt = rate*P*(1-P/Capacity), P = current population
dy/dx = rate*y*(1-y/YMAX)
'''
x_init = x[0]
y_init = y[0]
yapprox=[y_init]
xarr = np.linspace(5,80,1000)
dx = xarr[1]-xarr[0]
rate=.25
K = 1

for i in range(len(xarr[:-1])):
    yapprox.append( rate*yapprox[-1]*(1-yapprox[-1]/K)*dx +yapprox[-1])
yapprox=np.array(yapprox)
dy3 = (yapprox[1:]-yapprox[:-1])*10

p[1].plot(xarr[1:],dy3)
p[2].plot(x,y)
p[2].plot(x,y1)
p[0].plot(xarr,yapprox)
p[3].plot(x[:30],x1[:30])
plt.show()
