'''
want to see if rolling dice with advantage / disadvantage significantly changes
    odds

UPDATE: from running this code, have come to realize that an 'advantage' roll
    will give on average a 30% better score, and 'disadvantage' gives a 30%
    worse score. for example, a d20 die will roll an average of 10.5, but with
    advantage will give about 13.8 and with disadvantage 7.18. This was found to
    be quite consistent across each type of die.
'''

import numpy as np

r=lambda x:np.random.randint(1,x+1)
rd=lambda x:min(r(x),r(x))
ra=lambda x:max(r(x),r(x))
get_mean=lambda fn:np.array([fn() for i in range(100000)]).mean().round(2)

# because have copy/pasted this for multiple dice, will instead create function
def printdata(nSides):
    # specific to a certain die
    print('= for a d{}'.format(nSides),'='*30)
    reg=get_mean(lambda:r(nSides))
    dis=get_mean(lambda:rd(nSides))
    adv=get_mean(lambda:ra(nSides))
    print('average roll:',reg)
    print('disadvantage:',dis,'| ratio:',round(dis/reg,3))
    print('w/ advantage:',adv,'| ratio:',round(adv/reg,3))

printdata(4)
printdata(6)
printdata(8)
printdata(10)
printdata(12)
printdata(20)



# eof
