'''
datecreated: 190926
objective: first practice with naive bayes classification
source: https://www.youtube.com/watch?v=CPqOCI0ahss
KJG191119: use this to prep for bayes with iris dataset


'''

import numpy as np
# import matplotlib.pyplot as plt

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


def filt(arr,column,condition):
    return arr[arr[:,column]==condition,:]

def p(arr,col0,cond0,col1,cond1):
    ''' What is the probability col0 is at cond0, given col1 is at cond1?
    Ex: What is the probability the weather outlook is
        sunny, given that we will play golf? '''
    n0 = len(filt(filt(arr,col0,cond0),col1,cond1)) # ex: P(sunny|yes)
    nT = len(filt(arr,col1,cond1)) # ex: P(yes)
    return n0/nT
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
print('outlook:')
print('sunny & yes:',p(dat,0,0,-1,1))
print('ocast & yes:',p(dat,0,1,-1,1))
print('rainy & yes:',p(dat,0,2,-1,1))
print('sunny &  no:',p(dat,0,0,-1,0))
print('ocast &  no:',p(dat,0,1,-1,0))
print('rainy &  no:',p(dat,0,2,-1,0))

print('example set of factors.')
print('sunny, cool, humid, windy')

p_x_yes=(p(dat,0,0,-1,1)* # outlook
         p(dat,1,0,-1,1)* # temp
         p(dat,2,1,-1,1)* # humidity
         p(dat,3,1,-1,1)* # wind
         1)
p_x_no =(p(dat,0,0,-1,0)* # outlook
         p(dat,1,0,-1,0)* # temp
         p(dat,2,1,-1,0)* # humidity
         p(dat,3,1,-1,0)* # wind
         1)
p_x = ( len(filt(dat,0,0))/ntot*
        len(filt(dat,1,0))/ntot*
        len(filt(dat,2,1))/ntot*
        len(filt(dat,3,1))/ntot*
        1)
print('P(x) = ',p_x)
print('P(play|factors):   ',p_x_yes*p_yes/p_x)
print('P(noplay|factors): ',p_x_no*p_no/p_x)

# print('ocast & yes:',p(dat,0,0,-1,1))
# print('ocast & yes:',p(dat,0,0,-1,1))
# print('ocast & yes:',p(dat,0,0,-1,1))
# sunny    2,3,2/9,3/5 -- p(sunny|golf)
# overcast 4,0,4/9,0/5
# rainy    3,2,3/9,2/5

# temperature table
# hot   2,2,2/9,2/5
# mild  4,2,4/9,2/5
# cold  3,1,3/9,1/5










if(__name__=='__main__'):
    print('done')



# eof
