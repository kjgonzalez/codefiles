'''
want to do a quick demo of astrologer example in agresti statistics book

source: Agresti-Statistics book, ch9, pg 434 (pdf number)
"can astrologers predict personality better than random guessing?"

NOTE: typically, to disprove the null hypothesis (usually some sort of negative
    / disbelief prediction stating that something is NOT true), a p-value
    (probability value) with a "significance level" of 0.05 or lower is desired,
    which simply means that given the sample results, there's a 95% chance that
    the null hypothesis is wrong beyond a reasonable doubt.

'''

import numpy as np
import scipy.stats as st

''' in this example, the values are as such:
there were 116 attempts, n=116
astrologers had to choose one of three options, so p0 = 1/3 (random guess)
astrologers guessed correctly 40 times
null hypothesis: astrologers are no better than guessing

'''

p0 = 1/3
n=116
nCorrect = 40
p = nCorrect / n
stdErr0 = (p0*(1-p0)/n)**0.5 # standard error if p0 is correct, must be disproven
zstat = (p-p0)/stdErr0
pvalue = st.t.sf(zstat,n-1)
# pvalue is the "survival function" (1-tail distribution) of the student
#   distribution, given zvalue and degrees of freedom
print('astronomers got {} correct, zstat {}, and pvalue {}'.format(nCorrect,zstat,pvalue))

# given the original numbers, pvalue is 0.396, meaning that the null hypothesis
# is still valid, aka astronomers cannot be assumed to do better than random
# guessing. they would have needed to get 48 guesses correct at minimum.
