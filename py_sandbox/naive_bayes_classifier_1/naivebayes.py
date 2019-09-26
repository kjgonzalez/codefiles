'''
datecreated: 190926
objective: first practice with naive bayes classification
source: https://www.youtube.com/watch?v=CPqOCI0ahss



'''

import numpy as np
import matplotlib.pyplot as plt

def filt(column,condition,arr=dat):
    return arr[:,column]==condition

# pseudo dataset: probability to play golf, given variables
# outlook: sunny,overcast,rainy = 0,1,2
# temperture: cool, mild, hot = 0,1,2
# humidity: normal,high = 0,1
# windy: false,true = 0,1
# play: no, yes = 0,1

dat=np.array(
# outlook | temperature | humidity | windy | play
[[0,2,1,0,0],
[0,2,1,1,0],
[1,2,1,0,1],
[2,1,1,0,1],
[2,0,0,0,1],
[2,0,0,1,0],
[1,0,0,1,1],
[0,1,1,0,0],
[0,0,0,0,1],
[2,1,0,0,1],
[0,1,0,1,1],
[1,1,1,1,1],
[1,2,0,0,1],
[2,1,1,1,0]
])

# first, get p(yes) and p(no):
ntot = dat.shape[0]
nyes = dat[:,-1].sum()
nno  = ntot-nyes # binary

p_yes = nyes/ntot
p_no  = 1-p_yes # binary outcome

print(p_yes,p_no)

# look at probabilities that we can play given all variable combinations

# outlook table
# should have as seen in temp.png

# sunny    2,3,2/9,3/5
# overcast 4,0,4/9,0/5
# rainy    3,2,3/9,2/5

# temperature table
# hot   2,2,2/9,2/5
# mild  4,2,4/9,2/5
# cold  3,1,3/9,1/5










if(__name__=='__main__'):
    print('done')



# eof
