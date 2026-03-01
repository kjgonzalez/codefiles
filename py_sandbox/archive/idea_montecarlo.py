'''
basic intro to monte carlo simulation

1. define where randomness is located and the probability density function
2. loop until error acceptable
    a. run simulation with randomly selected values for each unknown
    b. get results, add to result vector
    c. if result vector average / stdev changes above a specific threshold, repeat. else, end
3. return relevant expected value (average of all results)

note: comparing difference in average still seems to cause variation. perhaps difference in stdev? this squares the
    errors, and therefore could have higher variation. need clearer end criteria.
'''

import numpy as np
import random


# EXAMPLE 1 ==========================================================
print("Example 1:","="*30)
print("Average value of rolling 2 d6 dice")
''' 
Theoretically, would need to roll up to 6x6x1000 (36k) rolls to get good sample, but might be able to roll less and 
    still get approximate result.
1. Outcome is defined as val = r1+r2, where r1 and r2 are stochastic vars with uniform distribution
2. will roll each die, add value, stop when change in average value is below envelope -> value has "settled"
'''

envelope = 1e-4
maxit = 36000
minit = 36 # arbitrarily choosing 0.1% of max theoretical...?
itercount = 0

d6 = lambda:random.randint(1,6)

x = [] # output
prev_avg = -1e6
done=False
while(not done):
    res = d6()+d6()
    x.append(res)
    curr_avg = np.mean(x)
    #if(len(x)<3):
    #    curr_avg = np.mean(x)
    #else:
    #    curr_avg = np.std(x)
    if((abs(curr_avg-prev_avg)<envelope and itercount>minit) or itercount>maxit):
        done=True
    else:
        itercount+=1
        prev_avg = curr_avg

x = np.array(x)
print('theoretical max # rolls:',maxit)
print(f'n iters: {len(x)} ({100*len(x)/maxit:0.2f}% of theoretical)',)
print('avg:',x.mean())
print('std:',x.std())
print('min:',x.min())
print('max:',x.max())
print('sample 10 values:',x[:10])
# EXAMPLE 2 ==========================================================
print("Example 2:","="*30)
print("Chance of throwing a dart on bullseye (point2D(gauss,gauss))")
''' 
Will assume that thrower has some experience and tends to have normal distribution of performance. distrib is 
    "tighter" (lower stdev) in horizontal "x" direction, higher in vertical "y" direction (e.g. from parabolic curve)
1. outcome is defined as dist_from_cent = norm2(<xloc,yloc>), with bullseye at origin, a bullseye defined as 
    2cm radius circle, entire board defined as 20cm radius circle. xloc is gauss(avg=0,std=10), yloc is 
    gauss(avg=0,std=15). 
    a. if split board up into polar coordinates, 1cm radius and 5 deg slice, would want at least (20/1)*(360/5)*100 =
          144000 samples, maybe even x10 that
2. will calculate xloc & yloc, get distance, n_bullseye, and r_bullseye. then, stop when distance is below envelope
    2a. will then count number of times value was less than 2.0
    
note: when set envelope to reference change in dist_from_center, r_bullseye still has high variation. will 
    instead set envelope to reference change in r_bullseye
'''

envelope = 1e-5
maxit = 144000
minit = 1440 # arbitrarily choosing 1% of max theoretical...?
itercount = 0

xsigma,ysigma = 10,15
xloc = lambda:random.gauss(0,xsigma)
yloc = lambda:random.gauss(0,ysigma)

x = [] # output
prev_avg = -1e6
done=False
while(not done):
    res = np.linalg.norm((xloc(),yloc())) # dist from center
    x.append(res)
    tmp =np.array(x)
    curr_avg = (tmp<=2.0).sum() / len(tmp)
    if((abs(curr_avg-prev_avg)<envelope and itercount>minit) or itercount>maxit):
        done=True
    else:
        itercount+=1
        prev_avg = curr_avg

x = np.array(x)
print(f'xloc=gauss(sigma={xsigma}), yloc=gauss(sigma={ysigma})')
print('theoretical max # throws:',maxit)
print(f'n iters: {len(x)} ({100*len(x)/maxit:0.2f}% of theoretical)',)
print('avg:',x.mean())
print('std:',x.std())
print('min:',x.min())
print('max:',x.max())
print('sample 10 values:',x[:10].round(2))
n_bullseye = sum([i<2 for i in x])
print(f'bullseye hit rate: {n_bullseye} / {len(x)} = {n_bullseye/len(x)*100:0.2f}%')

print('done')

# note: sample output:
'''
Example 1: ==============================
Average value of rolling 2 d6 dice
theoretical max # rolls: 36000
n iters: 56 (0.16% of theoretical)
avg: 7.0
std: 2.3375811674219387
min: 2
max: 12
sample 10 values: [ 4  2  6  8  9  6  5  4  8 10]
Example 2: ==============================
Chance of throwing a dart on bullseye (point2D(gauss,gauss))
xloc=gauss(sigma=10), yloc=gauss(sigma=15)
theoretical max # throws: 144000
n iters: 1442 (1.00% of theoretical)
avg: 16.31097695299068
std: 8.983116125942619
min: 0.43579919195363365
max: 62.7752344278024
sample 10 values: [22.98 15.96 19.54 25.26 12.   16.1  19.33 17.9  15.24 11.34]
bullseye hit rate: 17 / 1442 = 1.18%
done
'''



