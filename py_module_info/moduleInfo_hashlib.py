'''
basic information how to use the hashlib
'''

import hashlib

def toHash(textstring):
    ''' Use hash to verify information'''
    # note: "encode()" is needed to make bytes string
    return hashlib.md5(textstring.encode()).hexdigest()

HASH_text = '5eb63bbbe01eeed093cb22bb8f5acdc3'
good_text = 'hello world'
bad_text  = 'helloworld'

print('given a string:',good_text)
print('with hash:',HASH_text)
print('verify that matching:',toHash(good_text) == HASH_text)
print('verify with bad text:',toHash(bad_text) == HASH_text)

