'''
will review list comprehension, including nested comprehensions
'''
from klib import Stopwatch
st=Stopwatch()



print(
'\nsimple list comprehension is when you have something iterated on in a single line of code:')

yvals = [ix*2 for ix in range(10)]
print(yvals)

print(
'\nlist comprehensions will basically do anything to the individual item, just like in a forloop')
def pyt(a):
    return (3*3+a*a)**0.5

yvals = [pyt(ix) for ix in range(10)]
print(yvals)

print(
"\nsometimes it's a good idea to nest list comprehensions:")

# first, generate some fake data
letters='a b c d e f g'.split(' ')
values={}
i=2
for iletter in letters:
    values[iletter] = list(range(i))
    i+=1

# next, show how it's done in the nested forloop way:
st.tik()
out1=[]
for iletter in letters:
    for ivalue in values[iletter]:
        out1.append(iletter+str(ivalue))
t1=st.tok()
#print(out1) # should go from 'a0' to 'd4'

# finally, show how it's done in a nested forloop way:
st.tik()
out2=[iletter+str(ivalue) 
        for iletter in letters 
            for ivalue in values[iletter]]
t2=st.tok()
#t2=print(out2)

print('time ratio: about {} times as fast'.format(t1/t2))