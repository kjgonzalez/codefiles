'''
created: 190320
objective: teach yourself basis of using the argparse module.

want to learn about:
    * initialization
    * optional / required args
    * valid types

valid arguments for add_argument:
    dest: name of argument. if not used, default is stripped arg value
    help: quick help text should user type python file.py --help
    default: assumed value if not declared
    type: primitive variable types
    action: ('store_true', 'store_false', 'count')

sources:
https://docs.python.org/3.7/howto/argparse.html
https://docs.python.org/3/library/argparse.html
https://github.com/jwyang/faster-rcnn.pytorch/blob/master/trainval_net.py
'''

import argparse

# p=argparse.ArgumentParser() # like this, doesn't give default values on --help
p=argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
p.add_argument('--a',dest='int1',type=int,help='first int',default=0)
p.add_argument('--b',dest='int2',type=int,help='second int',default=1)
p.add_argument('--s',type=str,default="it's a nice day",help='string to print')
p.add_argument('--cuda',default=False,action='store_true',help='enable cuda')
p.add_argument('--list', nargs='+', help='<Required> Set flag', required=True)
args=p.parse_args()

print(args.int1+args.int2)
print(args.s)
if(args.cuda):
    print('using cuda')
else:
    print('cuda disabled')

print('list of arguments:',args.list)
# eof
