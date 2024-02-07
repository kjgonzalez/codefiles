'''
objective: make a barebones example of a genetic algo.
created: 231212
note: not sure of the exact nature / name of this algorithm. later, should try to refine this into better examples

also, in the future, would like to cover:
* conventional neuroevolution
* NEAT - network-shape-adjusting algo

'''

import numpy as np
import random

def world(x,y,z):
    return 6*x**3+9*y**2+90*z
def performance(x,y,z,goal=25):
    ''' approximate loss function '''
    return world(x,y,z)-goal

def fitness(x,y,z):
    return abs(performance(x,y,z)) # want this to be minimized... idk why we want the bigger value

# initialize overall pool
getrand = lambda: random.uniform(0, 10000)
solutions = []

for s in range(1000):
    solutions.append([getrand(),getrand(),getrand()])

# start of epochs. if find a good enough solution, break out early
for i in range(10000):
    # show current status
    rankedsolutions = []
    for s in solutions:
        rankedsolutions.append([fitness(*s),s]) # rank by best score (lowest)
        rankedsolutions.sort()
    print(f'=== Gen {i} best ===')
    print(' ',rankedsolutions[0])

    if(rankedsolutions[0][0]<0.001):
        break
    # keep best candidates
    bestsolutions = rankedsolutions[:100]
    elements=[]
    bestxs = []
    bestys = []
    bestzs = []
    for score,s in bestsolutions:
        bestxs.append(s[0])
        bestys.append(s[1])
        bestzs.append(s[2])

    newgen = []
    # generate new candidates
    for i in range(1000):
        newgen.append([
            random.choice(bestxs) * random.uniform(0.99,1.01), # some slight mutation needed
             random.choice(bestys) * random.uniform(0.99,1.01),
            random.choice(bestzs) * random.uniform(0.99,1.01)
        ])
    solutions = newgen

print('ngens:',i)
print('final answer:')
print(rankedsolutions[0])
print(world(*rankedsolutions[0][1]))
