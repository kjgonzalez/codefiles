'''
created: 190320
objective: teach yourself basis of using the argparse module. 

want to learn about:
    * initialization
    * optional / required args
    * valid types
'''

import argparse

parser=argparse.ArgumentParser()
parser.add_argument('--arg1',dest='int1',type=int)
parser.add_argument('--arg2',dest='int2',type=int)
parser.add_argument('--str1',type=str,default='nice day',required=False)
args=parser.parse_args()

print(args.int1+args.int2)
print(args.str1)

# eof

