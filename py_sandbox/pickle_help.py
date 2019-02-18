'''
how to pickle data (any object)
'''

import pickle

a={letter:num for num,letter in enumerate(list('abcdef'))}

with open('delme.pkl','wb') as f:
    pickle.dump(a,f)

with open('delme.pkl','rb') as f2:
    b=pickle.load(f2)

print('original:',a)
print('compare original and loaded:',a==b)